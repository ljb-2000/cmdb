#coding=utf-8
from app.models import db, Product
from app.utils import *

def create(**kwargs):
    #1.获取参数信息
    check_field_exists(Product, kwargs)
    #2.传参个数验证
    pid = kwargs.get('pid')[0] if isinstance(kwargs.get('pid'), list) else kwargs.get('pid')
    if int(pid) != 0:
        check_value_exists(Product, "id", pid)

    obj = Product(**kwargs)
    #3.插入数据库
    db.session.add(obj)
    db.session.commit()
    return obj.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')


    check_ouput_field(Product, output)

    check_order_by(Product, order_by)
    check_limit(limit)

    data = db.session.query(Product).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = process_result(data, output)

    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    check_update_params(Product, data, where)

    #如果传入了pid且值不是0,则进行参数验证
    if data.get("pid",None) is not None and data['pid'] != 0:
        check_value_exists(Product, "id", kwargs.get("pid", None))

    ret = db.session.query(Product).filter_by(**where).update(data)
    db.session.commit()
    return ret

