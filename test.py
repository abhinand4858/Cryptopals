import base64

def do_xor(x,y):
    res = int(x,16) ^ int(y,16)
    #print int(x,16)
    #print str(res) + "\n length" + str(len(str(res)))
    print hex(res)[2:-1]
    #print int(x,16)
    #print res
    return


x= raw_input()
y = raw_input()
do_xor(x,y)

