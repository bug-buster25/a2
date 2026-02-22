# 8. Clean up
mysql_cursor.close()
mysql_conn.close()
mongo_client.close()

print("✅ Migration complete!")
