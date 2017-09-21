# -*- coding:utf8 -*-

import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

debug = True
loglevel = 'debug'
bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
accesslog = 'logs/access.log'
logfile = 'logs/debug.log'
pidfile = 'logs/gunicorn.pid'
