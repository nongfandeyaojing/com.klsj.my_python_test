


if __name__ == "__main__":
    tbs=[
        {"id":"1001", "project_name":"米莫说｜MiMO Show", "speed_progress":"0.52/1.561", "task":"20%", "datetime":"2014-11-11"},
        {"id":"1002", "project_name":"商家与购物用户的交互试衣应用", "speed_progress":"0.52/1.561", "task":"40%", "datetime":"2014-11-11"},
        {"id":"1003", "project_name":"天狼---智能硬件项目", "speed_progress":"0.52/1.561", "task":"75%", "datetime":"2014-11-11"},
        {"id":"1004", "project_name":"线下超市+线上商城+物流配送互联系统", "speed_progress":"0.52/1.561", "task":"18%", "datetime":"2014-11-11"},
        {"id":"1005", "project_name":"线下超市+线上商城", "speed_progress":"0.52/1.561", "task":"20%", "datetime":"2014-11-11"},
        {"id":"1006", "project_name":"线下超市+线上商城", "speed_progress":"0.52/1.561", "task":"20%", "datetime":"2014-11-11"},
    ]

    getTableListBySearchPosttb = {
        "keyword": "",
        "id": ["1006", "1004", "1003"],
        "datetime": ""
    }

    ls = tbs
    if getTableListBySearchPosttb["keyword"] != "":
        ls = list(filter(lambda x: getTableListBySearchPosttb["keyword"] in x["project_name"], ls))
    if getTableListBySearchPosttb["id"] != "":
        ls = list(filter(lambda x: x["id"] in getTableListBySearchPosttb["id"], ls))
    if getTableListBySearchPosttb["datetime"] != "":
        ls = list(filter(lambda x: x["datetime"] >= getTableListBySearchPosttb["datetime"], ls))

