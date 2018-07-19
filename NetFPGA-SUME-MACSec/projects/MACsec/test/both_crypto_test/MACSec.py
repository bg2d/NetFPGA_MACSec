#!/usr/bin/env python

from scapy.all import *
from scapy.layers.all import *
import sys, os

MACSEC_TYPE = 0x88E5

class MACSec(Packet):
    name = "MACSec"
    # Note:
    # EtherType = 0x88E5, set in ETH packet
    # SCI, not yed modeled Secure Channel Identifier

    fields_desc = [
        # TAG Control Information
        BitField("v",   1, 0),      # VLAN
        BitField("es",  1, 0),      # End Station
        BitField("sc",  1, 0),      # SCI Present
        BitField("scb", 1, 0),      # Simple Copy Broadcast
        BitField("e",   1, 0),      # Encrypted Payload
        BitField("c",   1, 0),      # Change Text
        BitField("an",  2, 0),      # Association Number

        XByteField("sl", 4),        # Short Length, currently payload above
        XIntField("pn", 0),         # Packet Number

        XIntField("content", 0xabcd)
    ]

bind_layers(Ether, MACSec, type=MACSEC_TYPE)
# bind_layers(MACSec, Raw)

def generate_load(length):
    load = ''
    for i in range(length):
        load += '0'
	return load

def make_MACSec_pkt(dst_MAC, src_MAC, encrypted=False, pn = 0, sl = 4, content = 0xabcd):
    e = 0;
    if encrypted == True:
        e = 1

    pkt = Ether(dst=dst_MAC, src=src_MAC) / MACSec(e = e, pn = pn, sl = sl, content = content) /"AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDD"
    return pkt



