# 7. Migrate each table
for table in tables:
    print(f"Processing table: {table}")

    mysql_cursor.execute(f"SELECT * FROM {table}")
    rows = mysql_cursor.fetchall()

    # Transform records
    documents = [transform_types(row) for row in rows]

    if documents:
        mongo_collection = mongo_db[table]
        mongo_collection.insert_many(documents)
        print(f"Inserted {len(documents)} records into {table} collection.")
    else:
        print(f"No records found in {table}.")
