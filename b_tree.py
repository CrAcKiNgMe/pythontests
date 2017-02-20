#-*- coding: utf-8 -*-
import os
import socket
import sys
import httplib
import sqlite3
import random
from OpenSSL import SSL, crypto
import requests

import multiprocessing
from multiprocessing import Pool
import threading
import os

import timeit
import datetime




#的
#r = requests.get('https://baidu.com/')

import threading
import time

exitFlag = 0

class mythread(threading.Thread):
    def __init__(self, target = None,args = None, interval = 0.01,delay = 0, counter = 0):
        threading.Thread.__init__(self)
        self.interval = interval
        self.delay    = delay
        self.counter  = counter
        self.target  = target
        self.arg     = args
        self.runFlag = 1
    def end(self):
        self.runFlag = 0



    def run(self):
        def runwithtimer():
            if(self.delay > 0):
                time.sleep(self.delay)
            if(self.counter == 0):
                while 1 and self.runFlag:
                    if(self.target):
                        self.target(self)
                    if(self.interval > 0):
                        time.sleep(self.interval)
            else:
                while self.counter and self.runFlag:
                    if(self.target):
                        self.target(self.arg)
                    if(self.interval > 0):
                        time.sleep(self.interval)
                    self.counter = self.counter - 1
        runwithtimer()







class MyPool:
    def print_time(self, threadobj):

        header = {"user-agent": "my-app/0.0.1"}
        # r = requests.get("http://httpbin.org/get?asdf=asdf", headers=header)
        # r= requests.get("http://bbs.hupu.com/")#, headers=header)
        # print u"thread{0},response{1}".format(threading._get_ident(), r.headers)
        self.lock.acquire()
        self.tickcnt += 1
        print self.tickcnt
        if (self.tickcnt > 100000):
            self.lock.release()
            threadobj.end()
            return
        tmp = (self.tickcnt,"str", random.random(), str(datetime.datetime.now()))

        self.data.append(tmp)
        self.lock.release()


    def __init__(self, cnt = 20, maxcnt = 50):
        self.cnt = cnt
        self.maxcnt = maxcnt
        self.threads = [None]*cnt
        self.lock    = threading.Lock()
        self.tickcnt = 0
        self.data = []



        self.con = sqlite3.connect("C:/abc/test.db", check_same_thread=False)
        with self.con:
            cur = self.con.cursor()
            cur.execute("create table if not exists test(\
            A interger,\
            B vchar(256),\
            C numeric(256,3),\
            D interger\
            )")

        if self.con:
            self.con.commit()
        for i in range(self.cnt):
            self.threads[i] = mythread(target=self.print_time,args=None, interval=0);




    def start(self):
        for i in range(self.cnt):
            self.threads[i].start()
    def join(self):
        for i in range(self.cnt):
            self.threads[i].join()

    def finalize(self):
        with self.con:
            cur = self.con.cursor()
            cur.executemany("""INSERT INTO test
             VALUES(?, ?, ?, ?)""",self.data)

        if self.con:
            self.con.commit()
            self.con.close()







pool = MyPool(100, 100)
pool.start()
pool.join()
pool.finalize()









# Create new threads







"""

def verify_cb(conn, cert, errnum, depth, ok):
    certsubject = crypto.X509Name(cert.get_subject())
    commonname = certsubject.commonName
    print('Got certificate: ' + commonname)
    return ok


if len(sys.argv) < 3:
    print('Usage: python client.py HOST PORT')
    sys.exit(1)


dir = os.path.dirname(sys.argv[0])
if dir == '':
    dir = os.curdir




# Initialize context
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.set_options(SSL.OP_NO_SSLv2)
ctx.set_options(SSL.OP_NO_SSLv3)
#ctx.set_verify(SSL.VERIFY_PEER, verify_cb)  # Demand a certificate
#ctx.use_privatekey_file(os.path.join(dir, 'client.pkey'))
#ctx.use_certificate_file(os.path.join(dir, 'client.cert'))
#ctx.load_verify_locations(os.path.join(dir, 'CA.cert'))

# Set up client
sock = SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
sock.connect((sys.argv[1], int(sys.argv[2])))

while 1:
    line = sys.stdin.readline()
    if line == '':
        break
    try:
        print line
        sock.send(line)
        sys.stdout.write(sock.recv(1024).decode('utf-8'))
        sys.stdout.flush()
#    except SSL.Error:
#        print(" SSL.Error")
    except SSL.ZeroReturnError:
        print "ZeroReturnError"
        break
    except SSL.WantReadError:
        print "WantReadError"
        break
    except SSL.WantWriteError:
        print "WantWriteError"
        break
    except SSL.WantX509LookupError:
        print "WantX509LookupError"
        break
    except SSL.SysCallError:
        print "SysCallError"
        break




sock.shutdown()
sock.close()

"""