# 6. Define a transformation function
def transform_types(record):
    transformed = {}
    for key, value in record.items():
        if isinstance(value, Decimal):
            transformed[key] = float(value)
        elif isinstance(value, datetime):
            transformed[key] = value  # Already compatible
        elif isinstance(value, set):
            transformed[key] = list(value)  # 🔥 Convert sets to lists
        else:
            transformed[key] = value
    return transformed
