from dotenv import dotenv_values

import psycopg2

conf = dotenv_values()

sqlHost = conf['HOST']
sqlPort = conf['PORT']
sqlDB   = conf['DB']
sqlUser = conf['USER']
sqlPass = conf['PASS']

def sqlQuery(query):
    """
    Выполняет запрос в базе PostgreSQL\n
    Строка запроса должна быть передана на входе, на выходе в случаи:\n
    - Успеха - результат вывода или "no results to fetch"\n
    - Ошибки - описание ошибки\n

    При каждом отключении от базы, будет уведомление в консоль
    """
    try:
        sqlConnect = psycopg2.connect(
            host = sqlHost,
            port = sqlPort,
            user = sqlUser, 
            password = sqlPass,
            dbname = sqlDB
        )

        with sqlConnect.cursor() as cursor:
            cursor.execute(query)
            sqlConnect.commit()
            show = cursor.fetchall()
            return show
    except (Exception, psycopg2.Error) as error:
        print (error)
        return error
    finally:
        if sqlConnect:
            sqlConnect.close()
            #print("Connection closed")

def sqlUpdate(data):
    key = str(list(data.keys())).replace("'", '').replace('[', '').replace(']','')
    val = str(list(data.values())).replace('[', '').replace(']','').replace('None', 'null')
    string = 'INSERT INTO posts (%s) VALUES (%s);' % (key, val)
    return sqlQuery(string)