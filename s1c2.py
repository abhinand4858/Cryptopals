import base64

def do_xor(x,y):
    res = int(x,16) ^ int(y,16)
    print hex(res)[2:-1]
    return


x= raw_input()
y = raw_input()
do_xor(x,y)

