from collections import defaultdict
import pandas as pd
from odps import ODPS


class Read_ODPS_Data:


    def __init__(self,access_id,secret_access_key,project,endpoint):
        self.odps= ODPS(access_id=access_id,
                    secret_access_key=secret_access_key,
                    project=project,
                    endpoint=endpoint)

    def sql_odps(self,sql):

        with self.odps.execute_sql(sql).open_reader() as reader:
            print("odps_sql查询成功")
            d = defaultdict(list)  # collection默认一个dict
            # record一行数据，res一个元组
            for record in reader:
                for res in record:
                    d[res[0]].append(res[1])  # 解析record中的每一个元组，存储方式为(k,v)，以k作为key，存储每一列的内容；
            data = pd.DataFrame.from_dict(d, orient='index').T  # 转换为数据框，并转置，不转置的话是横条数据
            return data

