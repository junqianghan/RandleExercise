#!/usr/bin/python
#coding:utf-8
import eventlet
import datetime
from eventlet import wsgi


def hello_world(env, start_response):
    if env['PATH_INFO'] != '/':
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['Not Found\r\n']
    rsp_string = 'Hello world !'+ str(datetime.datetime.now())
    start_response('200 OK', [('Content-Type', 'text/plain')])

    return [rsp_string]

wsgi.server(eventlet.listen(('', 8090)), hello_world)