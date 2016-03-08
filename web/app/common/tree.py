#!/usr/bin/env python
# coding:utf-8

from app.common import api_action


class Treeview():
    def __init__(self):
        self.idc_info = api_action('idc.get', {'output': ['id', 'name']})
        self.product_info = api_action('product.get', {'output': ['id', 'module_letter', 'pid']})


    def get_child_node(self):
        ret = []
        for product in filter(lambda x: True if x.get('pid', None) == 0 else False, self.product_info):
            node = {}
            node['text'] = product['module_letter']
            node['id'] = product['id']
            node['type'] = 'service'
            node['nodes'] = self.get_grant_node(product['id'])
            ret.append(node)
        return ret

    def get_grant_node(self, pid):
        ret = []
        for product in filter(lambda x: True if x.get('pid', None) == pid else False, self.product_info):
            node = {}
            node['text'] = product['module_letter']
            node['id'] = product['id']
            node['type'] = 'product'
            node['pid'] = pid
            ret.append(node)
        return ret

    def get_node(self, idc):
        child = self.get_child_node()
        if not idc:
            return child
        ret = []
        for idc in self.idc_info:
            node = {}
            node['text'] = idc['name']
            node['id'] = idc['id']
            node['type'] = 'idc'
            node['nodes'] = child
            ret.append(node)
        return ret

    def get(self, idc):
        return self.get_node(idc)

def get_treeview(idc=True):
    return Treeview().get(idc)




