#coding=utf-8
from app.models import db, Raid
from app.utils import *

def create(**kwargs):
    #1.获取参数信息
    check_field_exists(Raid, kwargs)
    #2.传参个数验证
    obj = Raid(**kwargs)
    #3.插入数据库
    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')


    check_ouput_field(Raid, output)

    check_order_by(Raid, order_by)
    check_limit(limit)

    data = db.session.query(Raid).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(Raid, data, where)

    ret = db.session.query(Raid).filter_by(**where).update(data)
    db.session.commit()
    return ret

