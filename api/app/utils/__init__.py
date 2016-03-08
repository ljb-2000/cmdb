#coding=utf-8


def check_field_exists(obj, data, field_none=[]):
    '''
    验证字段是否合法
    验证字段不能为空
    :param data: 需要验证的数据
    :param field_none: 可以为空的字段
    :return:
    '''
    for field in data.keys():
        if not hasattr(obj, field):
            #验证字段是否存在
            raise Exception("params error")
        if not data.get(field, None) and data[field] not in field_none:
            #如果传入字段的值为“空”（也就是假） 并且 并没有在field_none中添加该字段以表示允许其为空
            #验证字段是否为None
            raise Exception(" {} 不能为空".format(data[field]))

def process_result(data, output):
    black = ["_sa_instance_state"]
    ret = []
    for obj in data:
        if output:
            tmp = {}
            for f in output:
                tmp[f] = getattr(obj, f)
            ret.append(tmp)
        else:
            tmp = obj.__dict__
            for p in black:
                try:
                    tmp.pop(p)
                except:
                    pass
            ret.append(tmp)
    return ret

def check_order_by(obj, order_by=''):
    order_by = order_by.split()
    if len(order_by) != 2:
        raise Exception("order by 参数必须为2个")

    field, order = order_by

    order_list = ['asc', 'desc']
    if order.lower() not in order_list:
        raise Exception("排序参数不对，值只能为： {}".format(order_list))

    if not hasattr(obj, field.lower()):
        raise Exception("排序字段不在该表中")

def check_limit(limit):
    if not str(limit).isdigit():
        raise Exception("limit值必须为数字")


def check_ouput_field(obj, output=[]):
    #如果output不是list，异常
    if not isinstance(output, list):
        raise Exception('output must is list!')
    #如果output中的字段在Idc中没有，异常
    for field in output:
        if not hasattr(obj, field):
            raise Exception('%s not found' % field)


def check_update_params(obj, data, where):
    if not data:
        raise Exception("no update data")

    for field in data.keys():
        if not hasattr(obj, field):
            raise Exception("%s 字段不存在" % field)

    if not where:
        raise Exception("没提供where条件")

    if  where.get('id', None) is None:
        if where.get('uuid', None) is None:
            raise Exception('需要提供id或uuid作为where条件')

    try:
        id = int(where['id'])
        if int(id) <= 0:
            raise Exception("条件id不能为负数")
    except:
        raise Exception("id必须为int")

def check_value_exists(obj, name, value):
    from app.models import db
    where = {name : value}
    ret = db.session.query(obj).filter_by(**where).first()
    if not ret:
        raise Exception("{} 不存在".format(value))
