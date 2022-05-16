from flask import redirect
response= redirect("http://localhost:8888/zoobar/index.cgi/transfer")
print(response)

def back():
    print("<html> <body> we are connecting you to the world</body></html>")
