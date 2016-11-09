import MySQLdb
import settings

database = settings.DATABASE 
conn = None
cur = None

def sql_context(database, conn, cur):
        def decorator(func):
            def wrapper(*args, **kwargs):
                global database, conn, cur
                conn = MySQLdb.connect(host=database['ip'], port=database['port'], \
                                             user=database['username'], passwd=database['password'], \
                                             db=database['db'])
                cur = conn.cursor(MySQLdb.cursors.DictCursor)
                retval = func(*args, **kwargs)
                conn.commit()
                conn.close()
                return retval
            return wrapper
        return decorator 



@sql_context(database, conn, cur)
def uc_sql(sql):
    cur.execute(sql)
    result = cur.fetchall()
    return result

if __name__ == '__main__':
    print uc_sql('select * from account_security limit 1')
