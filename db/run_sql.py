import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    #  accounting for unsuccesful connection in 'finally' statement
    conn = None
    # in case of an error, and no results are returned
    results = []
    
    try:
        # connection to the database
        conn=psycopg2.connect("dbname='task_manager'")
        # cursor is a control structure that lets us go through records in a db 
        cur = conn.cursor(cursor_factory=ext.DictCursor) 
        # cursor allows us to use execute to run sql statement  
        cur.execute(sql, values)
        #  makes changes in db transaction permanent/persist
        conn.commit()
        # 'fetchall()' method gets all rows returned from running a query
        results = cur.fetchall()
        # closing the cursor
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # 'finally' will run regardless
    finally:
        if conn is not None:
            conn.close()
    return results