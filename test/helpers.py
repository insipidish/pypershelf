def get_sql_results_factory(conn):
    def f(sql):
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    return f

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
