#!/usr/bin/python
#coding:utf-8

import httplib
import json
import webob.dec

from webob import Response
import datetime

class Controller(object):
    def __init__(self):
        # TODO
        self.version = "0.1"

    def index(self, req):
        print(req)
        print(req.environ["PATH_INFO"])
        response = Response(request=req,
                            status=httplib.MULTIPLE_CHOICES,
                            content_type='application/json')
        cur_time = datetime.datetime.now()
        response.body = json.dumps(dict(versions=self.version,
                                        name="hanjunqiang",
                                        time=str(cur_time)))
        return response

    @webob.dec.wsgify
    def __call__(self, request):
        # TODO
        return self.index(request)


def create_resource():
    return Controller()