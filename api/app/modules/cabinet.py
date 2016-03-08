#coding=utf-8
from app.models import db, Cabinet,Idc,Power
from app.utils import *


def create(**kwargs):
    #1.获取参数信息
    check_field_exists(Cabinet, kwargs)
    check_value_exists(Idc, "name", kwargs.get("idc_id", None))
    check_value_exists(Power, "server_power", kwargs.get("power", None))

    #2.传参个数验证
    obj = Cabinet(**kwargs)

    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')

    check_ouput_field(Cabinet,output)

    check_order_by(Cabinet, order_by)
    check_limit(limit)

    data = db.session.query(Cabinet).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(Cabinet, data, where)

    ret = db.session.query(Cabinet).filter_by(**where).update(data)
    db.session.commit()
    return ret

