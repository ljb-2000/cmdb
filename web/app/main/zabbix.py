#coding=utf-8
from __future__ import unicode_literals
from . import  main
from flask import render_template, request
import json
from app.common import api_action


@main.route('/monitor/ajax/get_zabbix_host_groups', methods=['POST'])
def get_zabbix_host_groups():
    from app.common.zabbix import zabbix_server
    hostgroups = zabbix_server.get_hostgroup()
    return json.dumps(hostgroups)


@main.route('/monitor/ajax/get_zabbix_data_by_group', methods=['POST'])
def get_zabbix_data_by_group():
    from app.common.zabbix import get_zabbix_data, init_zbhost
    #init_zbhost()
    params = dict(request.form) #{'server_purpose':[u'4'], 'service_id':[u'1']}
    hosts = api_action('server.get', {"output": ['id'],
                              'where': {"server_purpose":params['server_purpose'][0], 'service_id':params['service_id'][0]}})
    ret = get_zabbix_data(hosts)
    return json.dumps(ret)

@main.route('/monitor/ajax/link_zabbix_template', methods=['POST'])
def link_zabbix_template():
    data = dict(request.form)
    from app.common.zabbix import Zabbix
    z = Zabbix()

    hostids = data['hostids'][0].split(',') #  #[u'10111', u'10113']
    print hostids
    template_ids =  data['template_ids']
    print template_ids
    exist_templdate_ids = [i['templateid']for i in z.get_template(hostids)] #[{u'name': u'Template OS Linux', u'templateid': u'10001'}]
    new_template_ids = set(template_ids[0].split(',')+ exist_templdate_ids)

    if not new_template_ids:
        return '2'
    ret = []
    try:
        for h in hostids:
            data = {
                        'hostid' : h,
                        'templates' : [{'templateid': i} for i in new_template_ids]
                   }
            ret.append(z.update_host(data))
        return '1'
    except:
        return '3'

    # if ret == hostids:
    #     return '1'
    # else:
    #     return '3'

@main.route('/monitor/ajax/unlink_zabbix_template', methods=['POST'])
def unlink_zabbix_template():
    data = dict(request.form) #{'hostid': [u'10112'], 'templateid': [u'10050']}
    from app.common.zabbix import Zabbix
    z = Zabbix()
    template_id =  data['templateid']

    hostid = data['hostid'][0]

    data = {
                    'hostid' : hostid,
                    'templates_clear' : template_id
               }
    z.update_host(data)

    ret =  z.update_host(data)

    if ret['hostids'][0] == hostid:
        return "1"
    else:
        return ''






