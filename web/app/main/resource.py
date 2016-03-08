#!/usr/bin/env python
# coding:utf-8

from __future__ import unicode_literals
from flask import render_template, request

from app.common import api_action
from app.common.tree import get_treeview
from app.models import ZbHost, Server, db
from . import main

import json
import time

@main.route("/resource/index", methods=['GET'])
def resource_index():
    return render_template("resource/index.html")



@main.route('/resource/idc', methods=['GET'])
def resource_idc():
    return render_template("resource/server_add_idc.html")

@main.route("/resource/server_list", methods=['GET'])
def resource_server_list():
    servers = api_action("server.get")
    return render_template("resource/server_list.html",
                           servers=servers)



@main.route("/resource/server_add", methods=['GET'])
def resource_server_add():
    # 获取idc信息
    idc_info = api_action("idc.get", {"output": ['name', 'id']})
    status = api_action("status.get", {"outout":["id", "name"]})
    manufacturers = api_action("manufacturers.get", {"outout":["id", "name"]})
    ret = api_action("product.get", {"output":["id","service_name", "pid"]})

    product = [item for item in ret if item['pid'] == 0]
    powers = api_action("power.get")
    raids = api_action("raid.get")
    raidtype = api_action("raidtype.get")
    managementcardtype = api_action("management_card.get")
    supplier = api_action("supplier.get")
    return render_template("resource/server_add.html",
                           idc_info=idc_info,
                           status = status,
                           manufacturers = manufacturers,
                           products = product,
                           powers = powers,
                           raids = raids,
                           raidtypes = raidtype,
                           managementcardtypes = managementcardtype,
                           suppliers = supplier)


@main.route("/resource/server_doadd", methods=['POST'])
def resource_server_doadd():
    ret = api_action("server.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"


"""
    添加IDC页面
"""
@main.route("/resource/server_idc_add", methods=['GET'])
def resource_server_idc_add():
    return render_template("resource/server_add_idc.html")

"""
    执行IDC添加
"""
@main.route("/resource/server_idc_doadd", methods=['POST'])
def resource_server_idc_doadd():
    ret = api_action("idc.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"


"""
    添加服务器状态
"""
@main.route("/resource/server_status_add", methods=['GET'])
def resource_server_status_add():
    return render_template("resource/server_add_status.html")


"""
    执行服务器状态添加
"""
@main.route("/resource/server_status_doadd", methods=['POST'])
def resource_server_status_doadd():
    ret = api_action("status.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"


"""
    添加制造商
"""
@main.route("/resource/server_manufacturers_add", methods=['GET'])
def resource_server_manufacturers_add():
    return render_template("resource/server_add_manufacturers.html")

"""
    执行制造商添加
"""
@main.route("/resource/server_manufacturers_doadd", methods=['POST'])
def resource_server_manufacturers_doadd():
    ret = api_action("manufacturers.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"

"""
    添加服务器类型
"""
@main.route("/resource/server_servertype_add", methods=['GET'])
def resource_server_servertype_add():
    manufacturers = api_action("manufacturers.get", {"outout":["id", "name"]})
    return render_template("resource/server_add_servertype.html",
                           manufacturers=manufacturers)

"""
    执行服务器类型添加
"""
@main.route("/resource/server_servertype_doadd", methods=['POST'])
def resource_server_servertype_doadd():
    ret = api_action("servertype.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"



"""
    添加业务线,产品线
"""
@main.route("/resource/server_product_add", methods=['GET'])
def resource_server_product_add():
    ret = api_action("product.get")
    product = [item for item in ret if item['pid'] == 0]
    return render_template("resource/server_add_product.html",
                           products = product)



"""
    执行业务线,产品线的添加
"""
@main.route("/resource/server_product_doadd", methods=['POST'])
def resource_server_product_doadd():
    ret = api_action("product.create", dict(request.form))
    #print ret
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret




"""
    添加机柜
"""
@main.route("/resource/server_cabinet_add", methods=['GET'])
def resource_server_cabinet_add():
    idcs = api_action("idc.get", {"output":['id', 'name']})
    powers = api_action("power.get")
    return render_template("resource/server_add_cabinet.html",
                           idcs = idcs,
                           powers = powers)



"""
    执行机柜的添加
"""
@main.route("/resource/server_cabinet_doadd", methods=['POST'])
def resource_server_cabinet_doadd():
    ret = api_action("cabinet.create", dict(request.form))
    #print ret
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret




"""
    添加电源功率
"""
@main.route("/resource/server_power_add", methods=['GET'])
def resource_server_power_add():
    return render_template("resource/server_add_power.html")



"""
    执行电源功率添加
"""
@main.route("/resource/server_power_doadd", methods=['POST'])
def resource_server_power_doadd():
    ret = api_action("power.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret



"""
    添加raid信息
"""
@main.route("/resource/server_raid_add", methods=['GET'])
def resource_server_raid_add():
    return render_template("resource/server_add_raid.html")

"""
    执行raid信息添加
"""
@main.route("/resource/server_raid_doadd", methods=['POST'])
def resource_server_raid_doadd():
    ret = api_action("raid.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret


"""
    添加raid信息
"""
@main.route("/resource/server_raidcardtype_add", methods=['GET'])
def resource_server_raidcardtype_add():
    return render_template("resource/server_add_raidcardtype.html")


"""
    执行raid信息添加
"""
@main.route("/resource/server_raidcardtype_doadd", methods=['POST'])
def resource_server_raidcardtype_doadd():
    ret = api_action("raidtype.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret



"""
    添加远程管理卡信息信息
"""
@main.route("/resource/server_managementcardtype_add", methods=['GET'])
def resource_server_managementcardtype_add():
    return render_template("resource/server_add_managementcardtype.html")

"""
    执行远程管理卡添加
"""
@main.route("/resource/server_managementcardtype_doadd", methods=['POST'])
def resource_server_managementcardtype_doadd():
    ret = api_action("management_card.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret


"""
    添加供应高
"""
@main.route("/resource/server_supplier_add", methods=['GET'])
def resource_server_supplier_add():
    return render_template("resource/server_add_supplier.html")


"""
    执行添加供应高
"""
@main.route("/resource/server_supplier_doadd", methods=['POST'])
def resource_server_supplier_doadd():
    ret = api_action("supplier.create", dict(request.form))
    if str(ret).isdigit():
        return "操作成功"
    else:
        return ret












"""
    ajax操作
    根据制造商,获取服务器类型
"""
@main.route("/resource/ajax/get_server_type", methods=['GET'])
def resource_ajax_get_servertype():
    if request.method == 'GET':
        manufacturers_id = int(request.args.get('manufacturers_id',0))
        if manufacturers_id:
            servertypes = api_action("servertype.get",{})
            ret = [item for item in servertypes if item['manufacturers_id'] == manufacturers_id]
            return json.dumps(ret)
    return ""


"""
    ajax 操作
    要怕一级业务线,获取它的二级业务线
"""
@main.route("/resource/ajax/get_server_product", methods=['GET'])
def resource_ajax_get_product():
    if request.method == 'GET':
        pid = int(request.args.get('pid',0))
        if pid:
            servertypes = api_action("product.get",{"output": ["id", "service_name", "pid"]})
            ret = [item for item in servertypes if item['pid'] == pid]
            return json.dumps(ret)
    return ""

"""
    ajax 操作
    根据idc条件,获取机柜信息,
"""
@main.route("/resource/ajax/get_cabinet", methods=['GET'])
def resource_ajax_get_cabinet():
    if request.method == 'GET':
        idc_id = request.args.get('idc_id',0)
        if idc_id:
            cabinets = api_action("cabinet.get", {"output":['id', 'name', "idc_id"]})
            ret = [item for item in cabinets if item['idc_id'] == idc_id]
            return json.dumps(ret)
    return ''


'''
主机数据自动采集入库
'''
#from app.models import Product, db
@main.route("/resource/server/auto/collection", methods=['POST'])
def resource_server_collection():
    #1 接收传入的主机数据
    if request.method == "POST":
        data = dict(request.form)
        data['check_update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))



    #2 更新数据(先更新是为了显示出更新成功与否0/1,0代表无该主机记录再执行插入，1代表存在从而更新)

        ret = api_action("server.update", {"data":data, "where":{"uuid": data['uuid']}})

        if int(ret) == 0:
             api_action("server.create", data)

    #3 插入数据


    return ""

'''获取不在zabbix中的主机'''
@main.route('/resource/monitor/ajax/get_sync_zabbix_hosts', methods=['POST'])
def get_sync_zabbix_hosts():
    from app.common.zabbix import init_zbhost
    init_zbhost()
    zabbix_hosts = db.session.query(ZbHost).all()
    db.session.close()
    #不在zbhost表里
    #select * from server where id not in zbhost.cmdb_id
    hostid = [zb.cmdb_hostid for zb in zabbix_hosts] #在zbhost中的id
    servers = db.session.query(Server).filter(~Server.id.in_(hostid)).all()
    return json.dumps([{"hostname": s.hostname, 'id': s.id} for s in servers])

'''同步主机到zabbix'''
@main.route('/resource/monitor/ajax/sync_host_to_zabbix', methods=['POST'])
def sync_host_to_zabbix():
    #hostid  groupid
    if request.method == "POST":
        from app.common.zabbix import create_zabbix_host
        params = dict(request.form) #{'hostids': [u'1,2'], 'groupid': [u'2']}
        hostids = params['hostids'][0].split(',')
        ret = create_zabbix_host(hostids=hostids, groupid=params['groupid'][0])
        if len(ret) == len(hostids):
            return '1'
        else:
            return json.dumps(ret)

    return '500'

'''根据是否在产品线中，展示主机名'''
@main.route('/resource/server_group', methods=['GET'])
def resource_server_group():
    servers = api_action('server.get', {})
    hosts = []
    for s in servers:
        if not s['service_id'] and not s['server_purpose']:
            hosts.append({'value': s['id'], 'text': s['hostname']})
    treeview = get_treeview(idc=False)
    return render_template('resource/server_group.html', treeview=json.dumps(treeview), hosts=json.dumps(hosts))


'''把无组的主，添加进相应的产品线'''
@main.route('/resource/ajax/host_to_hostgroup', methods=['POST'])
def host_to_hostgroup():
    params = dict(request.form) # {'server_purpose': [u'2'], 'service_id': [u'1'], 'id': [u'12']}
    where = {'id': params['id'][0]}
    data = {
        'server_purpose': params['server_purpose'][0],
        'service_id': params['service_id'][0],
        'check_update_time': time.strftime("%Y-%m-%d %H:%I:%S", time.localtime(time.time()))
    }

    ret = api_action('server.update', {'where': where, 'data':data})
    if ret == 1:
        return str(ret)
    return '500'

#---------------------------------------------------
'''获取指定产品线里的主机'''
@main.route('/resources/ajax/gethostsbyhostgroup', methods=['POST'])
def get_hosts_bygroup():
    data = dict(request.form) # {'server_purpose':[u'4'], 'service_id': [u'1']}
    where = {'server_purpose': data['server_purpose'][0], 'service_id': data['service_id'][0]}
    ret = api_action('server.get', {'where': where, 'output': ['id', 'hostname']})

    hosts = []
    for r in ret:
        hosts.append({"value": r['id'], "text": r['hostname']})
    return json.dumps(hosts)


'''把产品线中的主机移除'''
@main.route('/resources/ajax/del_host_from_group', methods=['POST'])
def del_host_from_group():
    data = dict(request.form) # {'id': [u'2']}
    id = data['id'][0]
    ret = api_action('server.update', {'where': {'id': id}, 'data': {'server_purpose': None, 'service_id': None}})
    if ret == 1:
        return str(ret)
    return '200'
