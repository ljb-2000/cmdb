#!/usr/bin/env python
# coding:utf-8

from __future__ import unicode_literals
from flask import render_template, request
from . import main
import json

from app.common import tree

@main.route('/monitor/zabbix/index', methods=['GET'])
def monitor_zabbix():
    from app.common.zabbix  import zabbix_server
    zb_templates = zabbix_server.zb.template.get(output=['templateid', 'name'])
    templates = [{'value': i['templateid'], 'label': i['name']} for i in zb_templates]
    a = tree.get_treeview(idc=False)
    return render_template('monitor/monitor_zabbix.html', treeview=json.dumps(a), templates=json.dumps(templates))

@main.route('/monitor/zabbix/get/hosts', methods=['POST'])

def monitor_get_hosts():
    request.form
    ret = [
        {'id':1, 'hostname':'yz-ms-web-01', 'template':[{'id':1,'name':'t1'},{'id':1,'name':'t1'}]},
        {'id':2, 'hostname':'yz-ms-web-02', 'template':[{'id':1,'name':'t1'},{'id':1,'name':'t1'}]},
    ]
    return json.dumps(ret)