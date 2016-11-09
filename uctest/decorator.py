def sql_context(database, conn, cur):
        def decorator(func):
            def wrapper(*args, **kwargs):
                conn = MySQLdb.connect(host=database['ip'], port=database['port'], \
                                             user=database['username'], passwd=database['password'], \
                                             db=database['db'])
                cur = conn.cursor(MySQLdb.cursors.DictCursor)
                return func(*args, **kwargs)
            return wrapper
