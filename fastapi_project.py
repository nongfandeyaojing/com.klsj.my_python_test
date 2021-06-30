from fastapi import FastAPI, Query
from enum import Enum
from typing import List,Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# 首先应该安装fastapi，sqlalchemy
from sqlalchemy import Boolean, Column, Integer, String,DateTime,BIGINT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# uvicorn fastapi_project:app --reload
app = FastAPI() # 创建API实例

# 设置允许访问的域名
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许进行跨域请求的来源列表，*作为通配符
    allow_credentials=True,  # 跨域请求支持cookie，默认为否
    allow_methods=["*"],  # 允许跨域请求的HTTP方法
    allow_headers=["*"],  # 允许跨域请求的HTTP头列表
)

# 与mysql连接
# 格式为 'mysql+pymysql://账号名:密码@ip:port/数据库名'
SQLALCHEMY_DATABASE_URI:str = 'mysql+pymysql://root:aptx4869@localhost:3306/mybatis'
# username: root
# password: aptx4869
# jdbc:mysql://localhost:3306/mybatis?useUnicode=true&characterEncoding=utf-8&useSSL=true&serverTimezone=UTC

# 生成一个SQLAlchemy引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI,pool_pre_ping=True)
# 生成sessionlocal类，这个类的每一个实例都是一个数据库的会话
# 注意命名为SessionLocal，与sqlalchemy的session分隔开
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
session = SessionLocal()

Base = declarative_base()
# Base是用来给模型类继承的，类似django中的models.Model

# 模型类，tablename指表名，如果数据库中没有这个表会自动创建，有表则会沿用
class order_order(Base):
    __tablename__ = "apimonitor"
    id = Column(BIGINT, primary_key=True)
    # Column就类似django里的Table.objects
    # 里面放字段，字段必须在上面先导入
    is_enable = Column(String(225))
    api_uid = Column(String(225))
    api_name = Column(String(225))
    api_describe = Column(String(225))
    APPKEY = Column(String(225))
    APPSECRET = Column(String(225))
    group_host = Column(String(225))
    _apiPath = Column(String(225))
    method = Column(String(225))
    headers = Column(String(225))
    queryparams = Column(String(225))
    body = Column(String(225))
    repeats = Column(String(225))
    is_rely = Column(String(225))
    rely_id = Column(String(225))
    rely_api_name = Column(String(225))
    headers_model = Column(String(225))
    headers_packing = Column(String(225))
    queryparams_model = Column(String(225))
    queryparams_packing = Column(String(225))
    body_model = Column(String(225))
    body_packing = Column(String(225))
    remarks = Column(String(225))
# 此步也必不可少
Base.metadata.create_all(bind=engine)

print(session.query(order_order).get(1).id)
print(session.query(order_order).get(1).is_enable)
print(session.query(order_order).get(1).api_uid)
print(session.query(order_order).get(1).api_name)
print(session.query(order_order).get(1).api_describe)
print(session.query(order_order).get(1).APPKEY)

# class Monitor(BaseModel):
#     pass
#
class MonitorBody(BaseModel):
    api_name : str
    method: str

@app.get("/getMonitorList")
async def getMonitorList():
    '''
    :param request_data: json字段（Item类）
    :return: 返回tbs数据
    '''
    order_list = []
    for i in session.query(order_order).all():
        order_list.append({
            'id': i.id,
            'is_enable': i.is_enable,
            'api_uid': i.api_uid,
            'api_name': i.api_name,
            'api_describe': i.api_describe,
            'APPKEY': i.APPKEY,
        })
    return {"result": order_list}

#
@app.get("/monitor/{monitor_id}")
async def getMonitorByID(monitor_id: int):
    order = session.query(order_order).get(monitor_id)
    return {"result": order}
#
#
@app.post("/getMonitorByPostBody")
async def getTableListBySearchPost(monitorBody: MonitorBody):


    order_list = session.query(order_order).filter(order_order.api_name == monitorBody.api_name,
                                      order_order.method == monitorBody.method).all()

    return {"tbs": order_list}
