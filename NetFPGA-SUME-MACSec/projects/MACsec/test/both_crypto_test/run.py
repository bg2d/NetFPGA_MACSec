#!/usr/bin/env python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from NFTest import *
import sys
import os
from reg_defines_MACsec import *
from MACSec import *

# ---------------------------------------------------------------------------------------------------------------------
# Setup

phy2loop0 = ('../connections/conn', [])
nftest_init(sim_loop = [], hw_config = [phy2loop0])

SMAC="08:11:11:11:11:08"
DMAC="08:22:22:22:22:08"

if isHW():
   # reset_counters (triggered by Write only event) for all the modules 
   nftest_regwrite(SUME_INPUT_ARBITER_0_RESET(), 0x1)
   nftest_regwrite(SUME_OUTPUT_PORT_LOOKUP_0_RESET(), 0x101)
   nftest_regwrite(SUME_OUTPUT_QUEUES_0_RESET(), 0x1)
   nftest_regwrite(SUME_NF_10G_INTERFACE_SHARED_0_RESET(), 0x1)
   nftest_regwrite(SUME_NF_10G_INTERFACE_1_RESET(), 0x1)
   nftest_regwrite(SUME_NF_10G_INTERFACE_2_RESET(), 0x1)
   nftest_regwrite(SUME_NF_10G_INTERFACE_3_RESET(), 0x1)
   nftest_regwrite(SUME_NF_RIFFA_DMA_0_RESET(), 0x1)

   # Reset the switch table lookup counters (value is reset every time is read)
   nftest_regread(SUME_OUTPUT_PORT_LOOKUP_0_LUTHIT())
   nftest_regread(SUME_OUTPUT_PORT_LOOKUP_0_LUTMISS())

# Test reset registers
nftest_start()

routerMAC = []
routerIP = []
for i in range(4):
    routerMAC.append("00:ca:fe:00:00:0%d"%(i+1))
    routerIP.append("192.168.%s.40"%i)

# ---------------------------------------------------------------------------------------------------------------------
# Test counters

# Check if "other_pkts" counter increases by one
other_pkts = nftest_regread(SUME_CRYPTO_0_OTHER_PKTS())
pkt = make_IP_pkt(src_MAC="aa:bb:cc:dd:ee:ff", dst_MAC=routerMAC[0], EtherType=0x800, src_IP="192.168.0.1", dst_IP="192.168.1.1", pkt_len=60)
nftest_send_phy('nf0', pkt)
nftest_barrier()

nftest_regread_expect(SUME_CRYPTO_0_OTHER_PKTS(), other_pkts + 1)

# Check if "macsec_pkts" counter increases by one
macsec_pkts = nftest_regread(SUME_CRYPTO_0_MACSEC_PKTS())
pkt = make_MACSec_pkt(src_MAC=SMAC, dst_MAC=DMAC)
nftest_send_phy('nf0', pkt)
nftest_barrier()

nftest_regread_expect(SUME_CRYPTO_0_MACSEC_PKTS(), macsec_pkts + 1)

pkt = make_IP_pkt(src_MAC="aa:aa:aa:dd:dd:dd", dst_MAC=routerMAC[0], EtherType=0x800, src_IP="192.168.0.1", dst_IP="192.168.1.1", pkt_len=60)
nftest_send_phy('nf0', pkt)
nftest_barrier()

# Test reset registers
nftest_regwrite(SUME_CRYPTO_0_RESET(), 0xffff)
nftest_regread_expect(SUME_CRYPTO_0_MACSEC_PKTS(), 0)
nftest_regread_expect(SUME_CRYPTO_0_OTHER_PKTS(), 0)



"""
# ---------------------------------------------------------------------------------------------------------------------
# Test validation
nftest_regwrite(SUME_CRYPTO_0_RESET(), 0xffffffff)
pkt = make_MACSec_pkt(src_MAC=SMAC, dst_MAC=DMAC, sl=4, content = 0xabcd)

nftest_send_phy('nf0', pkt)

nftest_regread_expect(SUME_CRYPTO_0_ETHERTYPE(), 0x88E5)
nftest_regread_expect(SUME_CRYPTO_0_SLEN(), 4)

# ---------------------------------------------------------------------------------------------------------------------
# Test valid MACSec paket recognition
pkts = []
num_broadcast = 1

for i in range(num_broadcast):
    pkt = make_MACSec_pkt(src_MAC=SMAC, dst_MAC=routerMAC[0])
    pkt.time = ((i*(1e-8)) + (2e-6))
    pkts.append(pkt)

    if isHW():
        nftest_send_phy('nf0', pkt)
        nftest_expect_phy('nf1', pkt)
    
if not isHW():
    nftest_send_phy('nf0', pkts)
    nftest_expect_phy('nf1', pkts)
    nftest_expect_phy('nf2', pkts)
    nftest_expect_phy('nf3', pkts)
"""
nftest_barrier()
mres = []

nftest_finish(mres)




