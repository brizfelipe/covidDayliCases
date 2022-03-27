import psycopg2

from . import connection

class Postgres:
    
    def consultaAPI(location,date1,date2):
        #connection with postgres
        conn = psycopg2.connect(connection.AccessPostgres.connectionString)
        conn.autocommit = False
        cursor= conn.cursor()

        consultaAPI = f"""
            select 
                c.*
            from public.api_covidcases as c
                where 
                    c.location =  '{location}'
                and
                    c.date between  '{date1}' and '{date2}'
        """

        try:
            cursor.execute(consultaAPI)
            retornoQuery:dict = cursor.fetchall()

            cursor.execute("Select * FROM public.api_covidcases LIMIT 0")
            colnames = [desc[0] for desc in cursor.description]
            
            retorno:list=[]
            for row in retornoQuery:
                createDict= [{colnames[index]:value} for index,value in enumerate(row)]
                for index,value in createDict.items():
                    retorno[index]=value
        except:
            
            conn.commit()
            cursor.close()
            conn.autocommit = True
            return -1
        
        conn.commit()
        cursor.close()
        conn.autocommit = True
        return retorno
    
    def runCopyCSVCommand(filepath, tableName, sep, columns=False):

        # Connection to database
        conn = psycopg2.connect(connection.AccessPostgres.connectionString)
        conn.autocommit = False
        cursor = conn.cursor()
        columnsCorrigido:list = []

        with open(filepath) as f:
            try:
                if not columns or len(columns) == 0:
                    columns = ''
                else:
                    for column in columns:
                        columnsCorrigido.append('"'+column+'"')
                        
                    columns = '(' + ','.join(columnsCorrigido) + ')'

                cursor.copy_expert('copy public.' + tableName + ' ' + columns + ' from stdin with csv delimiter as ' + "\'" + sep + "\'" + " encoding \'utf-8\' ", f)

            except psycopg2.DatabaseError as err:
                conn.rollback()
                return print('Base import error : '+str(err))

        conn.commit()
        cursor.close()
        conn.autocommit = True
        return  print(f'successfully imported base: {tableName}')
