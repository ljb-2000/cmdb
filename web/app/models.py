#!/usr/bin/env python
# coding:utf-8
from app import db




class ZbHost(db.Model):
    __tablename__ = 'zbhost'
    id = db.Column(db.Integer, primary_key=True)
    cmdb_hostid = db.Column(db.Integer, index=True, unique=True)
    hostid = db.Column(db.Integer, index=True, unique=True)
    host = db.Column(db.String(50))
    ip = db.Column(db.String(32))



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

