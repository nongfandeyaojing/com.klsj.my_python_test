import pymysql

#获取数据、取字段名

def sql_data(host, port, user, password, db, sql_content):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql_content)
    datas = cursor.fetchall()
    title = cursor.description
    print("sql查询成功")

    cursor.close()
    return(datas,title)


host = '127.0.0.1'
port = 3306
user = 'root'
password = 'aptx4869'
db = 'mybatis'
sql_content = 'select * from user'
datas,table_title = sql_data(host, port, user, password, db, sql_content)
# print(table_title)

conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, use_unicode=True, charset="utf8")
cursor = conn.cursor()

for row  in datas:
    print()
    print(table_title[0][0],'=',row[0])
    print(table_title[1][0],'=',row[1])
    print(table_title[2][0],'=',row[2])
    insertSql = 'INSERT INTO user('+table_title[1][0]+', '+table_title[2][0]+') VALUES("%s", "%s")'%(row[1],row[2])
    print(insertSql)
    cursor.execute(insertSql)
    # 提交操作
    conn.commit()
    
cursor.close()
