# SQL Python Demo

Korte demo voor sollicitatie: laad CSV in SQLite, voer SQL-queries uit en verwerk resultaten met Python.

Structuur:
- data/sample_customers.csv : voorbeelddata
- sql/schema_and_queries.sql : creatie en voorbeeld-queries
- src/load_and_query.py : script dat CSV inlaadt, queryt en output schrijft

Gebruik:
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt    # (requirements worden hieronder genoemd)
4. python src/load_and_query.py

Outputs:
- customers.db (SQLite database)
- output/results.csv (queryresultaat)

