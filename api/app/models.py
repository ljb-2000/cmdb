#!/usr/bin/env python
# coding:utf-8
from app import db

'''
表名： user
字段说明 字段类型 属性
Id int 自增，主键
用户名，拼音 name String(50) 不为空
用户名，中文，username String(50) 不为空
email 邮件 email String(50) 不为空
所在部门 department_id Int Key
是否是 leader is_leader Int Key, default 0

0不是leader, 1是leader
'''

class switch_pirpost(db.Model):
    __tablename__       = 'reboot_test'
    id                  = db.Column(db.Integer,primary_key=True)
    purpose             = db.Column(db.String(100),nullable=False,default='')




class Switch(db.Model):
    __tablename__ = 'switch'
    id = db.Column(db.Integer, primary_key=True)
    switch_name = db.Column(db.String(50), nullable=False, default='')
    switch_type = db.Column(db.String(50), nullable=False, default='')
    manager_ip = db.Column(db.String(50), nullable=False, default='')
    category = db.Column(db.String(50), nullable=False, default='')
    idc_id = db.Column(db.Integer, nullable=False)
    cabinet_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    expire = db.Column(db.Date)
    remark = db.Column(db.Text)
    manufacturers = db.Column(db.String(50), nullable=False, default='')
    last_op_time = db.Column(db.Date)
    last_op_people = db.Column(db.String(30), nullable=False, default='')
    switch_port_nums = db.Column(db.Integer)


class IpInfo(db.Model):
    __tablename__ = 'ip_info'
    id = db.Column(db.Integer, primary_key=True)
    ip_type = db.Column(db.String(32), default='')
    ip = db.Column(db.String(50), nullable=False, default='')
    mac = db.Column(db.String(50), nullable=False, default='')
    device = db.Column(db.String(50), nullable=False, default='')
    server_id = db.Column(db.Integer, nullable=False, default=0)
    switch_id = db.Column(db.Integer, nullable=False, default=0)
    server_port = db.Column(db.Integer, nullable=False, default=0)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    department_id = db.Column(db.Integer, index=True , nullable=False, default=0)
    is_leader = db.Column(db.Integer, index=True , nullable=False, default=0)
    status = db.Column(db.Integer, index=True , nullable=False, default=0)

class Department(db.Model):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(32), nullable=False)
    superior = db.Column(db.String(32), nullable=False)
    path = db.Column(db.String(200))


class Iptype(db.Model):
    __tablename__ = 'iptype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Idc(db.Model):
    __tablename__ = 'idc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    idc_name =db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    user_interface = db.Column(db.String(50), nullable=False)
    user_phone = db.Column(db.String(50), nullable=False)
    rel_cabinet_num = db.Column(db.Integer, nullable=False)
    pact_cabinet_num = db.Column(db.Integer, nullable=False)

class Cabinet(db.Model):
    __tablename__ = 'cabinet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True,nullable=False,)
    idc_id = db.Column(db.String(50), index=True, nullable=False,)
    power = db.Column(db.Integer)

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Manufacturers(db.Model):
    __tablename__ = 'manufacturers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, default='')

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, default='')

class Raid(db.Model):
    __tablename__ ='raid'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, default='')

class RaidType(db.Model):
    __tablename__ ='raidtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, default='')

class ServerType(db.Model):
    __tablename__ = 'server_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False, default='')
    manufacturers_id = db.Column(db.Integer, index=True, default=0)

class ManagementCard(db.Model):
    __tablename__ = 'management_card'
    id = db.Column(db.Integer, primary_key=True)
    m_type = db.Column(db.String(50), unique=True, default='')

class Power(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    server_power = db.Column(db.String(50), unique=True, default='')

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), nullable=False, default='')
    pid = db.Column(db.Integer, index=True, nullable=False)
    module_letter = db.Column(db.String(15), nullable=False, default='')
    dev_interface = db.Column(db.String(100), nullable=False, default='')
    op_interface = db.Column(db.String(100), nullable=False, default='')

class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(400), nullable=True, default='')
    manufacturers = db.Column(db.String(200), nullable=True, default='')
    manufacture_date = db.Column(db.Date)
    server_type = db.Column(db.String(50), nullable=True, default='')
    st = db.Column(db.String(50), nullable=True, default='')
    assets_no = db.Column(db.String(50), nullable=True, default='')
    idc_id = db.Column(db.Integer, nullable=True, index=True, default='')
    cabinet_id = db.Column(db.Integer, nullable=True, index=True, default='')
    uuid = db.Column(db.String(50), index=True, default='')
    cabinet_pos = db.Column(db.String(15), nullable=True, default='')
    expire = db.Column(db.Date)
    ups = db.Column(db.Integer, nullable=True, default=0)
    parter = db.Column(db.String(50), nullable=True)
    parter_type = db.Column(db.String(50), nullable=True)
    server_up_time = db.Column(db.Date)
    os = db.Column(db.String(30), index=True, nullable=True, default='')
    hostname = db.Column(db.String(30), index=True, unique=True,default='')
    inner_ip = db.Column(db.String(50), index=True, nullable=True, unique=True, default='')
    mac_address = db.Column(db.String(50), nullable=True, default='')
    ipinfo = db.Column(db.String(50), nullable=True, default='')
    server_cpu = db.Column(db.String(50), nullable=True, default='')
    server_mem = db.Column(db.String(50), nullable=True, default='')
    server_disk = db.Column(db.String(50), nullable=True, default='')
    raid = db.Column(db.String(50), nullable=True, default='')
    raid_card_type = db.Column(db.String(50), nullable=True, default=0)
    remote_card = db.Column(db.String(50), nullable=True, default=0)
    remote_cardip = db.Column(db.String(50), nullable=True, default='')
    status = db.Column(db.Integer, nullable=True, default=0)
    remark = db.Column(db.Text, nullable=True, default='')
    last_op_time = db.Column(db.DateTime, nullable=True)
    last_op_people = db.Column(db.Integer, nullable=True, default=0)
    monitor_mail_group = db.Column(db.String(50), nullable=True, default='')
    service_id = db.Column(db.Integer, nullable=True, default=0)
    server_purpose = db.Column(db.Integer, nullable=True, default=0)
    trouble_resolve = db.Column(db.Integer, nullable=True, default=0)
    op_interface_other = db.Column(db.Integer, nullable=True, default=0)
    dev_interface = db.Column(db.Integer, nullable=True, default=0)
    check_update_time = db.Column(db.DateTime)
    vm_status = db.Column(db.Integer, index=True, nullable=True, default=0)
    power = db.Column(db.String(30), nullable=True, default='')
    host = db.Column(db.Integer, default=0)


class ZbHost(db.Model):
    __tablename__ = 'zbhost'
    id = db.Column(db.Integer, primary_key=True)
    cmdb_hostid = db.Column(db.Integer, index=True, unique=True)
    hostid = db.Column(db.Integer, index=True, unique=True)
    host = db.Column(db.String(50))
    ip = db.Column(db.String(32))




