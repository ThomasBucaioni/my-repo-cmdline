import binascii

val = b"\x01\x0234"
ser = binascii.hexlify (val)
unser = binascii.unhexlify (ser)
print (val, ser, unser)
print(len(val),len(ser),len(unser))

print('-----')

import base64

val = b"\x01\x0234"
ser = base64.b64encode(val)
print (ser)
print (ser.decode())
ori = base64.b64decode(ser)
print (ori)

# https://www.asciitohex.com/
# https://www.irif.fr/~carton/Enseignement/XML/Cours/Schemas/index.html

print('-----')

import json
import pprint

struct_python = {
    "Image": {
        "Width": 800,
        "Height": 600,
      "Title": "View from 15th Floor",
        "Thumbnail": {
            "Url": "http://www.example.com/image/481989943",
            "Height": 125,
            "Width": 100
        },
        "Animated" : False,
        "Copyright" : None,
        "IDs": [0x11, 0x943, 234, 38793],
        "Title": "Empty picture"
    }
}

print (struct_python)
pprint.pprint(struct_python)

struct_json = json.dumps(struct_python)

print('Json: ', struct_json)

struct_python2 = json.loads(struct_json)

pprint.pprint (struct_python2)

print('-----')

import cbor2 as cbor
from bitstring import BitArray

def mybin(s):
    t = s[0:8] + '-'
    for i in range(1,int(len(s)/8)):
        t = t + s[i*8:i*8+8] + '-'
#    print (f'{t=}', t[:-1])
    return t[:-1]

v = 1

for i in range (0, 33):
    if v < 256 :
        c = cbor.dumps(v)
        vt = v
    else :
        c = cbor.dumps(v+1)
        vt = v+1
    c2 = BitArray(c)
    print ("{0:3} {1:30} {2} \t=\t {4}".format(i, vt, c.hex(), c2.bin, mybin(c2.bin)))
    v *= 2

print('-----')

import cbor2 as cbor

for i in range (1, 10):
    c = cbor.dumps("LoRaWAN"*i)

    print ("{0:3} {1}".format(i, c.hex()))

bs = cbor.dumps(b"\x01\x02\x03")
print (bs.hex())

print('-----')

import cbor2 as cbor
from datetime import date, timezone

print (date.today())
c1 = cbor.dumps(date.today(), timezone=timezone.utc, date_as_datetime=True)

print (c1.hex())

print (cbor.loads(c1))
print (type(cbor.loads(c1)))

print('-----')

# http://cbor.me
