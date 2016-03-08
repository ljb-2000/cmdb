#!/usr/bin/python
#coding=utf8

import requests
import json

url = "http://127.0.0.1:5000/api"
headers = {"Content-type": "application/json"}

data = {
    "jsonrpc":2.0,
    "method": "product.get",
    "id":1,
    "auth":None,
    "params":{
        "name": 'yz',
        'idc_name': 'beijing yizhuang jifang',
        'address': 'beijing yizhuang',
        'phone': '12312345678',
        'email': 'gzy@xx.com',
        'user_interface': 'panda',
        'user_phone': '23144322222',
        'rel_cabinet_num': 30,
        'pact_cabinet_num': 44,
    }

}


'''
data = {
    "jsonrpc":2.0,
    "method": "server.update",
    "id":1,
    "auth":None,
    'params':{
        'data':{
        'server_disk': '10',
        'uuid': '1C268A26-9AAF-4529-95C8-B60088181B72',
        'server_type': 'VirtualBox',
        'server_cpu': 'Intel(R) Core(TM) i3-4130 CPU @ 3.40GHz 1',
        'hostname': 'h1',
        'st': '0',
        'vm_status': '0',
        'manufacturers': 'innotek GmbH',
        'inner_ip': '192.168.2.247',
        'mac_address': '08:00:27:42:58:76',
        'manufacture_date': '2006-12-01',
        'os': 'CentOS 6.4 Final',
        'check_update_time':'2016-02-12 11:11:13'},

        "where":{'uuid':'1C268A26-9AAF-4529-95C8-B60088181B72'}

    }

}
'''
r = requests.post(url, headers=headers, json=json.dumps(data))
print r.status_code
print r.content