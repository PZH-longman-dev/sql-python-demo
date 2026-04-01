#!/usr/bin/env python3
# load_and_query.py
# Laadt CSV in SQLite, voert query uit en schrijft resultaat naar CSV.

import sqlite3
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SQL_FILE = os.path.join(BASE_DIR, "sql", "schema_and_queries.sql")
DB_PATH = os.path.join(BASE_DIR, "customers.db")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CSV_FILE = os.path.join(BASE_DIR, "data", "sample_customers.csv")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "results.csv")


os.makedirs(OUTPUT_DIR, exist_ok=True)

def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Lees en executeer schema (DROP + CREATE)
    with open(SQL_FILE, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    cur.executescript(schema_sql)

    # Laad CSV in tabel
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [(int(r['id']), r['first_name'], r['last_name'], r['email'],
                 r['signup_date'], r['country'], float(r['spend'])) for r in reader]
    cur.executemany(
        "INSERT INTO customers (id, first_name, last_name, email, signup_date, country, spend) VALUES (?, ?, ?, ?, ?, ?, ?)",
        rows
    )
    conn.commit()

    # Voorbeeldquery: totale bestede per land
    cur.execute("""
        SELECT country, SUM(spend) AS total_spend, COUNT(*) AS customers
        FROM customers
        GROUP BY country
        ORDER BY total_spend DESC
    """)
    results = cur.fetchall()

    # Schrijf output naar CSV
    with open(OUTPUT_CSV, "w", newline='', encoding='utf-8') as out:
        writer = csv.writer(out)
        writer.writerow(["country", "total_spend", "customers"])
        writer.writerows(results)

    print(f"Database aangemaakt: {DB_PATH}")
    print(f"Resultaten geschreven: {OUTPUT_CSV}")

    conn.close()

if __name__ == "__main__":
    run()

