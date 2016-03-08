#!/usr/bin/env python
#coding=utf-8
import os, imp

class AutoLoad():
    def __init__(self, module_name):
        dir = os.path.abspath(os.path.dirname(__file__))
        self.moduleDir = os.path.join(os.path.dirname(dir), "modules")
        self.module_name = module_name
        self.method = None

    def isValidModule(self):
        return self._load_module()

    def isValidMethod(self, func=None):
        self.method = func

        return hasattr(self.module, self.method)

    def getCallMethod(self):
        if hasattr(self.module, self.method):
            return getattr(self.module, self.method)
        return None

    def _load_module(self):
        ret = False
        for filename in os.listdir(self.moduleDir):
            if filename.endswith('.py'):
                module_name = filename.rstrip('.py')
                if self.module_name == module_name:
                    fp, pathname, desc = imp.find_module(module_name, [self.moduleDir])
                    if not fp:
                        continue
                    try:
                        self.module = imp.load_module(module_name, fp, pathname, desc)
                        print self.module
                        ret = True
                    finally:
                        fp.close()
                    break
                else:
                    print "not found"
        return ret


class JsonRpc():
    def __init__(self, jsonData):
        self.VERSION = '2.0'
        self._error = True
        self.jsonData = jsonData
        self._response = {}

    def execute(self):
        if not self.jsonData.get('id', None):
            self.jsonData['id'] = None

        if self.validate():
            params = self.jsonData.get('params', None)
            auth = self.jsonData.get('auth', None)
            module, func = self.jsonData.get('method', "").split(".")
            ret = self.callMethod(module, func, params, auth)
            self.processResult(ret)

        return self._response

    def processResult(self, response):
        if response.errorCode != 0:
            self.jsonError(self.jsonData.get('id'), response.errorCode, response.errorMessage)
        else:
            self._response = {'jsonrpc': self.VERSION,
                              'result': response.data,
                              'id':self. jsonData.get('id')
                            }


    def callMethod(self, module, func, params, auth):
        module_name = module.lower()
        func = func.lower()
        response = Response()
        autoload = AutoLoad(module_name)

        if not autoload.isValidModule():
            response.errorCode = 106
            response.errorMessage = "指定module不存在"
            return response

        if not autoload.isValidMethod(func):
            response.errorCode = 107
            response.errorMessage = "%s 模块没有 %s 方法" % (module_name, func)
            return response

        flag = self.requireAuthentication(module_name, func)
        if flag:
            if auth is None:
                response.errorCode = 108
                response.errorMessage = "该操作需要token"
                return response
            else:
                pass

        try:
            called = autoload.getCallMethod()
            if callable(called):
                response.data = called(**params)
            else:
                response.errorCode = 109
                response.errorMessage = "%s.%s不能被调用 " % (module_name, func)
        except Exception, e:
            response.errorCode = -1
            response.errorMessage = e.message
            return response
        return response

    def requireAuthentication(self, module, func):
        if module == "user" and func == "login":
            return False
        if module == "reboot":
            return False
        return False  # all allow



    def validate(self):
        if not self.jsonData.get('jsonrpc', None):
            self.jsonError(self.jsonData.get('id', 0), 101, "参数jsonrpc没有传")
            return False
        if str(self.jsonData.get('jsonrpc')) != self.VERSION:
            self.jsonError(self.jsonData.get('id', 0), 101, "参数jsonrpc版本错误，应该为 %s" % self.VERSION)
            return False
        if not self.jsonData.get('method', None):
            self.jsonError(self.jsonData.get('id', 0), 102, "参数method没有传")
            return False
        if self.jsonData.get('params', None) is None:
            self.jsonError(self.jsonData.get('id', 0), 103, "params没有传")
            return False
        if "." not in self.jsonData.get('method', None):
            self.jsonError(self.jsonData.get('id', 0), 104, "模块与方法间请用点号分隔")
            return False
        if not isinstance(self.jsonData.get('params'), dict):
            self.jsonError(self.jsonData.get('id',0), 105, "params应为字典")
            return False

        return True

    def jsonError(self, id, errno, errmsg):
        self._error = True
        format_err= {'jsonrpc':self.VERSION, 'id':id, 'errno':errno, 'errmsg':errmsg}
        self._response = format_err

class Response():
    def __init__(self):
        self.data = None
        self.errorCode = 0
        self.errorMessage = None

'''
101 jsonrpc版本，或没有参数
102 参数method没有传
103 params没有传
104 参数method格式不正确
105 params应该为dict
106 指定的module不存在
107 {}下没有{}该方法
108 该操作需要token
109 不能调用
-1 api有except

'''

if __name__ == "__main__":
    data = {'jsonrpc':2.0, 'method':'reboot.get','params':{}}
    jrpc = JsonRpc(data)
    print jrpc.execute()




