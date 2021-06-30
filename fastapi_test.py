from fastapi import FastAPI, Query
from enum import Enum
from typing import List,Optional

# from flask_cors import cross_origin
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# uvicorn fastapi_test:app --reload
app = FastAPI() # 创建API实例

# #设置允许访问的域名
# origins = ["*"]  #也可以设置为"*"，即为所有。
#
# app.add_middleware(CORSMiddleware, allow_origins=origins,  #设置允许的origins来源
#                    allow_credentials=True,
#                    allow_methods=["get", "post", "put"],  # 设置允许跨域的http方法*，比如 get、post、put等。
#                    # allow_headers=["Access-Control-Allow-Origin:*"])  #允许跨域的headers，可以用来鉴别来源等作用。)
#                    allow_headers=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#允许进行跨域请求的来源列表，*作为通配符
    allow_credentials=True,#跨域请求支持cookie，默认为否
    allow_methods=["*"],#允许跨域请求的HTTP方法
    allow_headers=["*"],#允许跨域请求的HTTP头列表
)

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    a: int = None
    b: int = None

class Search_Body(BaseModel):
    keyword: str = None
    id_no: list = []
    star_time: str = None
    star_time: str = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/item1s/{item_id}")
async def read_item1(item_id: int):
    return {"item_id": item_id}

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: str = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/")
async def read_items(q: List[str] = Query(None)):
    query_items = {"q": q}
    return query_items

@app.get("/items1/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/post_info2")
async def post_info2(a: int,b:int):
    '''
    一个带有参数的get请求
    :param a:
    :param b:
    :return: a + b
    '''
    c = a + b
    result = {'a': a, 'b': b, 'a+b': c}
    return result

@app.post("/post_info1")
async def post_info1(request_data: Item):
    '''
    必须传json的post接口
    :param request_data: json字段（Item类）
    :return: 返回a+b的和
    '''
    a = request_data.a
    b = request_data.b
    c = a + b
    result = {'a': a, 'b': b, 'a+b': c}
    return result

tbs=[
    {"id":"1001", "project_name":"米莫说｜MiMO Show", "speed_progress":"0.52/1.561", "task":"20%", "datetime":"2014-11-11"},
    {"id":"1002", "project_name":"商家与购物用户的交互试衣应用", "speed_progress":"0.52/1.561", "task":"40%", "datetime":"2014-11-11"},
    {"id":"1003", "project_name":"天狼---智能硬件项目", "speed_progress":"0.52/1.561", "task":"75%", "datetime":"2014-11-11"},
    {"id":"1004", "project_name":"线下超市+线上商城+物流配送互联系统", "speed_progress":"0.52/1.561", "task":"18%", "datetime":"2014-11-11"},
    {"id":"1005", "project_name":"线下超市+线上商城", "speed_progress":"0.52/1.561", "task":"20%", "datetime":"2014-11-11"},
    {"id":"1006", "project_name":"线下超市+线上商城", "speed_progress":"0.52/1.561", "task":"20%", "datetime":"2014-11-11"},
]

@app.get("/getTableList")
async def getTableList():
    '''
    :param request_data: json字段（Item类）
    :return: 返回tbs数据
    '''
    return {"tbs": tbs}

@app.get("/getTableListBySearch")
async def getTableListBySearch(keyworld: str):
    getTableListBySearchtb = []
    for i in tbs:
        if keyworld in i["project_name"]:
            getTableListBySearchtb.append(i)

    return {"getTableListBySearchtb":getTableListBySearchtb}

@app.post("/getTableListBySearchPost")
async def getTableListBySearchPost(search_body: Search_Body):

    search_result = tbs

    if search_body.keyword != "":
        search_result = list(filter(lambda x: search_body.keyword in x["project_name"], search_result))
    if search_body.id_no != "":
        search_result = list(filter(lambda x: x["id"] in search_body.id_no, search_result))
    if search_body.star_time != "":
        search_result = list(filter(lambda x: x["datetime"] >= search_body.star_time, search_result))

    return {"tbs": search_result}


@app.post("/getTableListBySearchPost1")
def getTableList1(search_body: Search_Body):
    '''
    :param request_data: json字段（Item类）
    :return: 返回tbs数据
    '''
    return {"tbs": search_body}

class GetTablePost(BaseModel):
    keyword: str = 'hao'
    id_no: int = 10

@app.post("/getTablePost")
def getTablePost(getTablePost: GetTablePost):
    '''
    :param request_data: json字段（Item类）
    :return: 返回tbs数据
    '''

    return {"tbs": getTablePost.keyword}
