#!/usr/bin/env python
#coding:utf-8

import sys
import os
from main import MonitorClient

def daemonize(stdin='/dev/null',stdout='/dev/null',stderr='/dev/null'):
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError,e:
        sys.stderr.write("fork #1 failed:(%d) %s\n"%(e.errno,e.strerror))
        sys.exit(1)

    os.chdir("/")
    os.umask(0)
    os.setsid()
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError,e:
        sys.stderr.write("fork #2 failed:(%d) %s\n"%(e.errno,e.strerror))
        sys.exit(1)
    for f in sys.stdout,sys.stderr:f.flush()
    si = file(stdin,'r')
    so = file(stdout,'a+')
    se = file(stderr,'a+',0)
    os.dup2(si.fileno(),sys.stdin.fileno())
    os.dup2(so.fileno(),sys.stdout.fileno())
    os.dup2(se.fileno(),sys.stderr.fileno())


def run():
    sys.stdout.write('daemon started with pid %d\n'%os.getpid())
    pid = os.getpid()
    with open(process_pid,"w") as f:
        f.write("%d"%pid)
    sys.stdout.flush()
    dk = MonitorClient()
    dk.start()



if __name__ == '__main__':
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    process_pid = "%s/%s.pid"%(BASE_DIR,sys.argv[0].strip(".py"))
    process_log = "%s/%s.log"%(BASE_DIR,sys.argv[0].strip(".py"))
    if len(sys.argv) != 2:
        print "参数数目输入错误,ps:python %s start|stop|restart"%sys.argv[0]
    elif sys.argv[1] != "start" and sys.argv[1] != "stop" and sys.argv[1] != "restart":
        print "参数输入错误,ps:start|stop|restart"
    elif sys.argv[1] == "start":
        print "the process is start"
        daemonize('/dev/null',process_log,process_log)
        run()
    elif sys.argv[1] == "stop":
        with open(process_pid,"r") as f:
            pid = f.read()
        os.kill(int(pid),9)
        print "the process is stop"
    elif sys.argv[1] == "restart":
        try:
            with open(process_pid,"r") as f:
                pid = f.read()
                os.kill(int(pid),9)
            print "the process is stop"
            print "the process is start"
            daemonize('/dev/null',process_log,process_log)
            run()
        except OSError,e:
            print e
            print "the process is start"
            daemonize('/dev/null',process_log,process_log)
            run()
        except:
            print "error"

