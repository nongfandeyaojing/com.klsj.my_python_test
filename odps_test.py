from collections import defaultdict
import pandas as pd
from odps import ODPS



def sql_odps(access_id,secret_access_key,project,endpoint,sql):

    odps = ODPS(access_id=access_id,
                secret_access_key=secret_access_key,
                project=project,
                endpoint=endpoint)
    with odps.execute_sql(sql).open_reader() as reader:
        print("odps_sql查询成功")
        d = defaultdict(list)  # collection默认一个dict
        # record一行数据，res一个元组
        for record in reader:
            for res in record:
                d[res[0]].append(res[1])  # 解析record中的每一个元组，存储方式为(k,v)，以k作为key，存储每一列的内容；
        data = pd.DataFrame.from_dict(d, orient='index').T  # 转换为数据框，并转置，不转置的话是横条数据
        return data

# access_id = '0SIh4yYSwi7RqOPg'
# secret_access_key = 'GoeK0vlb5HhyaM9158CW3xX8BXslIW'
# project = 'api_gateway'
# endpoint = 'http://service.cn-haikou-hkzw01-d01.odps.yunwei.haikou.cn/api'
# sql = 'select * from api_gateway.ca_api where pt="20210416"'
#
# data  = sql_odps(access_id,secret_access_key,project,endpoint,sql)
#
# print(data)
def get_tbinfo():
    access_id = '0SIh4yYSwi7RqOPg'
    secret_access_key = 'GoeK0vlb5HhyaM9158CW3xX8BXslIW'
    project = 'api_gateway'
    endpoint = 'http://service.cn-haikou-hkzw01-d01.odps.yunwei.haikou.cn/api'

    odps = ODPS(access_id=access_id,
                secret_access_key=secret_access_key,
                project=project,
                endpoint=endpoint)
    result = {
        'id':[],
        'tb_name' : [],
        'tb_size' : [],
        'tb_comment' : [],
        'last_partition' : [],
        'tbp_recently_count' : [],
        'tbp_recently_size' : [],
        'tb_schema': []

    }

    id = 0
    for tb in odps.list_tables():
        id = id+1
        tb_name = tb.name
        tb_size = tb.size
        tb_comment = tb.comment
        last_partition = [i.name for i in tb.iterate_partitions()][-1]
        tbp_recently_count = 0
        tbp_recently_size = 0
        tb_schema = tb.schema
        if tb.exist_partition(last_partition):
            tbp_recently_size = tb.get_partition(last_partition).size
            with tb.get_partition(last_partition).open_reader() as reader:
                tbp_recently_count = reader.count

        result['id'].append(id)
        result['tb_name'].append(tb_name)
        result['tb_size'].append(tb_size)
        result['tb_comment'].append(tb_comment)
        result['last_partition'].append(last_partition)
        result['tbp_recently_count'].append(tbp_recently_count)
        result['tbp_recently_size'].append(tbp_recently_size)
        result['tb_schema'].append(tb_schema)
        print(id,',',tb_name,',',tb_size,',',tb_comment,',',last_partition,',',tbp_recently_count,',',tbp_recently_size,',',tb_schema)
    result_df = pd.DataFrame(result)
    result_df.to_csv("opds_result.csv")

if __name__ == "__main__":
    get_tbinfo()
