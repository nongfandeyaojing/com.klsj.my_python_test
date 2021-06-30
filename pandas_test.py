
import pandas as pd
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()  #需要先开启引擎

##将数据写入mysql的数据库，但需要先通过sqlalchemy.create_engine建立连接,且字符编码设置为utf8，否则有些latin字符不能处理
yconnect = create_engine('mysql+mysqldb://root:aptx4869@localhost:3306/mybatis?charset=utf8')
print(yconnect)
# pd.io.sql.to_sql(thedataframe,'tablename', yconnect, schema='mybatis', if_exists='append')