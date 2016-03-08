#coding=utf-8
from app.models import db, IpInfo,Server,Switch
from app.utils import check_field_exists, process_result, check_order_by, check_limit,check_update_params,check_ouput_field

def create(**kwargs):
    #1.获取参数信息
    check_field_exists(IpInfo, kwargs)
    #2.传参个数验证
    check_value_exists(Server, "id", kwargs.get("server_id", None))
    check_value_exists(Switch, "id", kwargs.get("switch_id", None))

    obj = IpInfo(**kwargs)
    #3.插入数据库
    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')


    check_ouput_field(IpInfo, output)

    check_order_by(IpInfo, order_by)
    check_limit(limit)

    data = db.session.query(IpInfo).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(IpInfo, data, where)

    if data.get("server_id", None):
        check_value_exists(Server, "id", kwargs.get("server_id", None))
    if data.get("switch_id", None):
        check_value_exists(Switch, "id", kwargs.get("switch_id", None))

    ret = db.session.query(IpInfo).filter_by(**where).update(data)
    db.session.commit()
    return ret

