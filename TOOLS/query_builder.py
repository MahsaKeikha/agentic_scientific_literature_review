def build(concepts):
    return " AND ".join(f"({c})" for c in concepts if c)
