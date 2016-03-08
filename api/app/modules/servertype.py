#coding=utf-8
from app.models import db, ServerType,Manufacturers
from app.utils import *


def create(**kwargs):
    #1.获取参数信息
    check_field_exists(ServerType, kwargs)
    check_value_exists(Manufacturers, "id", kwargs.get("manufacturers_id", None))
    

    #2.传参个数验证
    obj = ServerType(**kwargs)

    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')

    check_ouput_field(ServerType,output)

    check_order_by(ServerType, order_by)
    check_limit(limit)

    data = db.session.query(ServerType).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(ServerType, data, where)

    ret = db.session.query(ServerType).filter_by(**where).update(data)
    db.session.commit()
    return ret

