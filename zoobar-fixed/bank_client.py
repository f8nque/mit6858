from debug import *
import rpclib
import os
sys.path.append(os.getcwd())
import readconf
def transfer(sender,recepient,zoobars,token,caller=None):
    host =readconf.read_conf().lookup_host("bank")

    with rpclib.client_connect(host) as c:
        c.call("transfer",sender=sender,recepient=recepient,zoobars=zoobars,token=token,caller=caller)

        

        
def balance(username):
    host = readconf.read_conf().lookup_host("bank")
    with rpclib.client_connect(host)as c:
        response=c.call("balance",username=username)
        return response

def get_log(username):
    host = readconf.read_conf().lookup_host("bank")
    with rpclib.client_connect(host) as c:
        response =c.call("get_log",username=username)
        return response
