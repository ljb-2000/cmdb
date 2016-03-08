#!/usr/bin/env python
#coding=utf-8

from flask import current_app
from zabbix_client import ZabbixServerProxy
from app.models import ZbHost, Server, db
from app.common import api_action
conf = current_app.config


ZABBIX_URI = conf.get('SQLALCHEMY_ZABBIX_API_URL')
ZABBIX_USER = conf.get('SQLALCHEMY_ZABBIX_API_USER')
ZABBIX_PASS = conf.get('SQLALCHEMY_ZABBIX_API_PASS')






class Zabbix():
    def __init__(self):
        self.zb = ZabbixServerProxy(ZABBIX_URI)
        self.zb.user.login(user=ZABBIX_USER, password=ZABBIX_PASS)


    def get_hosts(self):
        return self.zb.host.get(output=['hostid', 'host'])

    def get_hostinterface(self,hostids):
        data = self.zb.hostinterface.get(hostids=hostids, output=['hostid', 'ip'])
        #重组数据格式: {hostid: ip}
        ret = {}
        for i in data:
            ret[i['hostid']] = i['ip']
        return ret

    def get_hostgroup(self,hostids):
        return self.zb.hostgroup.get(hostids=hostids, output=['groupid', 'name'])

    def get_template(self, hostid):
        return self.zb.template.get(hostids=hostid,output=['templateid','name'])

    def create_host(self, params):
        return self.zb.host.create(**params)

    def update_host(self,params):
        return self.zb.host.update(**params)


zabbix_server = Zabbix()

#def get_zabbix_template(hostid):
#    return zabbix_server.zb.get_template(hostid=hostid)


def init_zbhost():
    db.session.execute("truncate zbhost")
    init_zabbix()
    init_cmdb()
    return ''

def init_zabbix():
    #取出host：ip，host，id
    #获取zabbix的主机列表
    zb_hosts = zabbix_server.get_hosts()
    #同样的，也一次取出所有zabbix主机的interface的信息
    zb_hosts_interface = zabbix_server.get_hostinterface([z['hostid']for z in zb_hosts])

    for h in zb_hosts:
        h['ip'] = zb_hosts_interface[h['hostid']]
        db.session.add(ZbHost(**h))
    db.session.commit()

def init_cmdb():
    #获取server表中的host
    hosts = api_action("server.get")
    #更新zbhost表, ip
    for i in hosts:
        data = {'cmdb_hostid': i['id']}
        db.session.query(ZbHost).filter_by(ip=i['inner_ip']).update(data)
    db.session.commit()

def get_zabbix_data(hosts):
    #获取zabbix的主机及模板
    data = db.session.query(ZbHost).filter(ZbHost.cmdb_hostid.in_([h['id']for h in hosts])).all()
    ret = []
    for z in data:
        tmp = {}
        tmp['hostname'] = z.host
        tmp['templates'] = zabbix_server.get_template(z.hostid)
        tmp['hostid'] = z.hostid
        ret.append(tmp)

    return ret




def create_zabbix_host(hostids, groupid):
    servers = db.session.query(Server).filter(Server.id.in_(hostids)).all()
    ret = []
    for h in servers:
        data = {
            'host': h.hostname,
            'interfaces':[
                {
                    'type': 1,
                    'main': 1,
                    'useip': 1,
                    'ip': h.inner_ip,
                    'dns': "",
                    "port": '10050'
                }
            ],
            'groups':[
                {
                    'groupid':groupid
                }
            ]
        }
        ret.append(zabbix_server.create_host(data))
    return ret