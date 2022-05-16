
import socket
import json
def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("10.1.5.4",8081))
    code = """
    #!python\nprint("Hello Everybody")
    """
    request = json.dumps(["run",{"pcode":code,"user":"frank","visitor":"root"}]).encode('ascii') + b"\n"
    client.sendall(request)
    response = client.recv(1024)
    print("the server response %s"%response)
    client.close()

main()
    

