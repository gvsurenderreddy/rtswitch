#!/usr/bin/env python
#-*-encoding:utf-8 -*-
import ConfigParser
import string, os, sys
import argparse

PROGRAM = "rtswitch"
VERSION = "v0.1"

def readConfig():
    cf = ConfigParser.ConfigParser()
    cf.read("sample.conf")
    # 返回所有的section
    s = cf.sections()
    print 'section:', s
"""
    o = cf.options("db")
    print 'options:', o

    v = cf.items("db")
    print 'db:', v

    print '-'*60
    #可以按照类型读取出来
    db_host = cf.get("db", "db_host")
    db_port = cf.getint("db", "db_port")
    db_user = cf.get("db", "db_user")
    db_pass = cf.get("db", "db_pass")

    # 返回的是整型的
    threads = cf.getint("concurrent", "thread")
    processors = cf.getint("concurrent", "processor")

    print "db_host:", db_host
    print "db_port:", db_port
    print "db_user:", db_user
    print "db_pass:", db_pass

    print "thread:", threads
    print "processor:", processors
    #修改一个值，再写回去
    cf.set("db", "db_pass", "zhaowei")
    cf.write(open("sample.conf", "w"))
"""
def usage():
    print "rtswitch ipsec to tun1"
    print "rtswitch ipsec to tun1"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "some information here")
    parser.add_argument("-l", "--list", help="list input node or tunnels", action='store_true')
    parser.add_argument("-A", "--add", help="add a tunnel", dest="new_tun")
    parser.add_argument("-D", "--del", help="delete a tunnel", dest= "del_tun")

    args = parser.parse_args()
    print args.del_tun

    cf = ConfigParser.ConfigParser()
    cf.read("sample.conf")
    s = cf.sections()
    cf.remove_section(args.del_tun)
    cf.write(open("sample.conf", "w"))
    cf.add_section(args.add)
    cf.set(args.add, "host", "172.16.18.11")
    cf.write(open("sample.conf", "a+w"))


    readConfig()
