#coding=utf-8
from app.models import db, Department
from app.utils import *

def create(**kwargs):
    #1.获取参数信息
    check_field_exists(Department, kwargs)
    #2.传参个数验证
    if kwargs.get("pid", 0) != 0:
        check_value_exists(Department, "id", kwargs.get("pid", None))

    obj = Department(**kwargs)
    #3.插入数据库
    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')


    check_ouput_field(Department, output)

    check_order_by(Department, order_by)
    check_limit(limit)

    data = db.session.query(Department).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(Department, data, where)

    if data.get("pid",None) is not None and data['pid'] != 0:
        check_value_exists(Department, "id", kwargs.get("pid", None))

    ret = db.session.query(Department).filter_by(**where).update(data)
    db.session.commit()
    return ret

