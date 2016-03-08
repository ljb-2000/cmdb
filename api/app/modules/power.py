#coding=utf-8
from app.models import db, Power
from app.utils import check_field_exists, process_result, check_order_by, check_limit,check_update_params,check_ouput_field

def create(**kwargs):
    #1.获取参数信息
    check_field_exists(Power, kwargs)
    #2.传参个数验证
    obj = Power(**kwargs)
    #3.插入数据库
    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')


    check_ouput_field(Power, output)

    check_order_by(Power, order_by)
    check_limit(limit)

    data = db.session.query(Power).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(Power, data, where)

    ret = db.session.query(Power).filter_by(**where).update(data)
    db.session.commit()
    return ret

