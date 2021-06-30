import pandas as pd
from sqlalchemy import create_engine  #pd.to_sql需要开启引擎
import pymysql


class Data_To_Mysql:

    pymysql.install_as_MySQLdb()  #需要先开启引擎

    def __init__(self, host, port, user,password,db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.yconnect = create_engine('mysql+mysqldb://'+user+':'+password+'@'+host+':'+port+'/'+db+'')

    def dataFrame_to_msql(self,df, sql_table,dtype,index_label=None,insert_type='append'):

        df.to_sql(name=sql_table, con=self.yconnect,dtype=dtype,index=False, schema=self.db, index_label=index_label, if_exists=insert_type)

        print('成功写入到',sql_table,'中！')
