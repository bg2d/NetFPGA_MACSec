#from NFTest import *

from scapy.layers.all import Ether, IP, TCP

# Where should we start encrypting/decrypting?
START_POS = 14 + 20

def encrypt_pkt(key, pkt):
    key_ary = [0, 0, 0, 0]
    for i in range(4):
        key_ary[i] = (key >> (24 - i * 8)) & 0xff

    # Identify the packet type and break up the packet as appropriate
    str_pkt = str(pkt)
    str_hdr = str_pkt[:START_POS]
    load = str_pkt[START_POS:]
    str_load = ''
    for i in range(len(str_pkt)-START_POS):
        str_load += chr(ord(load[i]) ^ key_ary[(i+START_POS)%4])        
    ret_pkt = Ether(str_hdr+str_load)
    return ret_pkt

def decrypt_pkt(key, pkt):
    return encrypt_pkt(key, pkt)
