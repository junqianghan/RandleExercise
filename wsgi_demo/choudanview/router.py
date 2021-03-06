#!/usr/bin/python
#coding:utf-8

import routes

from choudanview import wsgi
from choudanview import versions


class API(wsgi.Router):
    def __init__(self, mapper=None):
        if (mapper == None):  # 创建mapper对象
            mapper = routes.Mapper()

        versions_resource = versions.create_resource()  # 创建资源
        mapper.connect("/", controller=versions_resource,  # 建立对应关系
                       action="index")
        mapper.connect("/index/{id}",controller=versions_resource,
                       action="index")
        super(API, self).__init__(mapper)