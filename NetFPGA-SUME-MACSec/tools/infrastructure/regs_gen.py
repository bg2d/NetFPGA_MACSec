#! /usr/bin/env python
# Copyright (c) 2015 Noa Zilberman
# All rights reserved.
#
# This software was developed by Stanford University and the University of Cambridge Computer Laboratory
# under National Science Foundation under Grant No. CNS-0855268,
# the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and
# by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 (),
# as part of the DARPA MRC research programme.
#
# @NETFPGA_LICENSE_HEADER_START@
#
# Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  NetFPGA licenses this
# file to you under the NetFPGA Hardware-Software License, Version 1.0 (the
# ); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#   http://www.netfpga-cic.org
#
# Unless required by applicable law or agreed to in writing, Work distributed
# under the License is distributed on an ``AS IS'' BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
# @NETFPGA_LICENSE_HEADER_END@
#

##################################################################
#Define the list of registers (busses) and their characteristics
##################################################################
 
module_name='crypto'

block_name=module_name.upper()
 
def create_regs_list():
  regsDict=[
{'reg':"ID",'type':"RO",'endian':"little", 'name':"id",'bits':"31:0",'width':"32",'addr':"32'h0",'default':"32'h0000DA01"},

{'reg':"Version",'type':"RO",'endian':"little", 'name':"version",'bits':"31:0",'width':"32",'addr':"32'h4",'default':"32'h1"},

{'reg':"Reset",'type':"WOE",'endian':"little", 'name':"reset",'bits':"15:0",'width':"16",'addr':"32'h8",'default':"16'h0"},

{'reg':"Flip",'type':"RWA",'endian':"little", 'name':"flip",'bits':"31:0",'width':"32",'addr':"32'hC",'default':"32'h0"},

{'reg':"Debug",'type':"RWA",'endian':"little", 'name':"debug",'bits':"31:0",'width':"32",'addr':"32'h10",'default':"32'h0"},

{'reg':"PktIn",'type':"ROC",'endian':"little", 'name':"pktin",'bits':"31:0",'width':"32",'addr':"32'h14",'default':"32'h0"},

{'reg':"PktOut",'type':"ROC",'endian':"little", 'name':"pktout",'bits':"31:0",'width':"32",'addr':"32'h18",'default':"32'h0"},

{'reg':"EtherType",'type':"RWA",'endian':"little", 'name':"ethertype",'bits':"15:0",'width':"16",'addr':"32'h1C",'default':"16'h0"},

{'reg':"TCI",'type':"RWA",'endian':"little", 'name':"tci",'bits':"7:0",'width':"8",'addr':"32'h20",'default':"8'h0"},

{'reg':"SLEN",'type':"RWA",'endian':"little", 'name':"slen",'bits':"7:0",'width':"8",'addr':"32'h24",'default':"8'h0"},

{'reg':"PNUM",'type':"RWA",'endian':"little", 'name':"pnum",'bits':"31:0",'width':"32",'addr':"32'h28",'default':"32'h0"},

{'reg':"ICV",'type':"RWA",'endian':"little", 'name':"icv",'bits':"31:0",'width':"32",'addr':"32'h2C",'default':"32'h0"},

{'reg':"MACSEC_PKTS",'type':"RWA",'endian':"little", 'name':"macsec_pkts",'bits':"31:0",'width':"32",'addr':"32'h30",'default':"32'h0"},

{'reg':"OTHER_PKTS",'type':"RWA",'endian':"little", 'name':"other_pkts",'bits':"31:0",'width':"32",'addr':"32'h34",'default':"32'h0"},

]
  return(regsDict)
 
def create_mems_list():
  memsDict=[
{'mem':"Testmem", 'name':"testmem",'data_bits':"31:0",'addr_bits':"9:0",'width':"32",'address':"32'h0"},

]
  return(memsDict)
#
# Copyright (c) 2015 Noa Zilberman, Jingyun Zhang, Salvator Galea
# All rights reserved.
#
# This software was developed by Stanford University and the University of Cambridge Computer Laboratory 
# under National Science Foundation under Grant No. CNS-0855268,
# the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and
# by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"), 
# as part of the DARPA MRC research programme.
#
# @NETFPGA_LICENSE_HEADER_START@
#
# Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  NetFPGA licenses this
# file to you under the NetFPGA Hardware-Software License, Version 1.0 (the
# "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#   http://www.netfpga-cic.org
#
# Unless required by applicable law or agreed to in writing, Work distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
# @NETFPGA_LICENSE_HEADER_END@
#

##################################################################
# a function that writes the header of regs file
##################################################################
def write_regs_header(regsFile):
      regsFile.write('\
//\n\
// Copyright (c) 2015 University of Cambridge\n\
// All rights reserved.\n\
//\n\
//\n\
//  File:\n\
//        '+module_name+'_cpu_regs.v\n\
//\n\
//  Module:\n\
//        '+module_name+'_cpu_regs\n\
//\n\
//  Description:\n\
//        This file is automatically generated with the registers towards the CPU/Software\n\
//\n\
// This software was developed by Stanford University and the University of Cambridge Computer Laboratory\n\
// under National Science Foundation under Grant No. CNS-0855268,\n\
// the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and\n\
// by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"),\n\
// as part of the DARPA MRC research programme.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_START@\n\
//\n\
// Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor\n\
// license agreements.  See the NOTICE file distributed with this work for\n\
// additional information regarding copyright ownership.  NetFPGA licenses this\n\
// file to you under the NetFPGA Hardware-Software License, Version 1.0 (the\n\
// "License"); you may not use this file except in compliance with the\n\
// License.  You may obtain a copy of the License at:\n\
//\n\
//   http://www.netfpga-cic.org\n\
//\n\
// Unless required by applicable law or agreed to in writing, Work distributed\n\
// under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\n\
// CONDITIONS OF ANY KIND, either express or implied.  See the License for the\n\
// specific language governing permissions and limitations under the License.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_END@\n\
//\n\
\n')
#end of write_regs_headerdefault

##################################################################
# a function that writes the header of regs defines file
##################################################################

def write_defs_header(defsFile):
      defsFile.write('\
//\n\
// Copyright (c) 2015 University of Cambridge\n\
// All rights reserved.\n\
//\n\
//\n\
//  File:\n\
//        '+module_name+'_cpu_regs_defines.v\n\
//\n\
//  Module:\n\
//        '+module_name+'_cpu_regs_defines\n\
//\n\
//  Description:\n\
//        This file is automatically generated with the registers defintions towards the CPU/Software\n\
//\n\
// This software was developed by Stanford University and the University of Cambridge Computer Laboratory\n\
// under National Science Foundation under Grant No. CNS-0855268,\n\
// the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and\n\
// by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"),\n\
// as part of the DARPA MRC research programme.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_START@\n\
//\n\
// Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor\n\
// license agreements.  See the NOTICE file distributed with this work for\n\
// additional information regarding copyright ownership.  NetFPGA licenses this\n\
// file to you under the NetFPGA Hardware-Software License, Version 1.0 (the\n\
// "License"); you may not use this file except in compliance with the\n\
// License.  You may obtain a copy of the License at:\n\
//\n\
//   http://www.netfpga-cic.org\n\
//\n\
// Unless required by applicable law or agreed to in writing, Work distributed\n\
// under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\n\
// CONDITIONS OF ANY KIND, either express or implied.  See the License for the\n\
// specific language governing permissions and limitations under the License.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_END@\n\
//\n\
\n')

#end of write_defs_header


##################################################################
# a function that writes the header of regs tcl file
##################################################################

def write_tcl_header(tclFile):
      tclFile.write('\
#\n\
# Copyright (c) 2015 University of Cambridge\n\
# All rights reserved.\n\
#\n\
#\n\
#  File:\n\
#        '+module_name+'_regs_defines.tcl\n\
#\n\
#  Description:\n\
#        This file is automatically generated with tcl defines for the software\n\
#\n\
# This software was developed by Stanford University and the University of Cambridge Computer Laboratory\n\
# under National Science Foundation under Grant No. CNS-0855268,\n\
# the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and\n\
# by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"),\n\
# as part of the DARPA MRC research programme.\n\
#\n\
# @NETFPGA_LICENSE_HEADER_START@\n\
#\n\
# Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor\n\
# license agreements.  See the NOTICE file distributed with this work for\n\
# additional information regarding copyright ownership.  NetFPGA licenses this\n\
# file to you under the NetFPGA Hardware-Software License, Version 1.0 (the\n\
# "License"); you may not use this file except in compliance with the\n\
# License.  You may obtain a copy of the License at:\n\
#\n\
#   http://www.netfpga-cic.org\n\
#\n\
# Unless required by applicable law or agreed to in writing, Work distributed\n\
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\n\
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the\n\
# specific language governing permissions and limitations under the License.\n\
#\n\
# @NETFPGA_LICENSE_HEADER_END@\n\
#\n\
\n')

#end of write_tcl_header


##################################################################
# a function that writes the header of regs tcl file
##################################################################

def write_hFile_header(hFile):
      hFile.write('\
//\n\
// Copyright (c) 2015 University of Cambridge\n\
// All rights reserved.\n\
//\n\
//\n\
//  File:\n\
//        '+module_name+'_regs_defines.h\n\
//\n\
//  Description:\n\
//        This file is automatically generated with header defines for the software\n\
//\n\
// This software was developed by Stanford University and the University of Cambridge Computer Laboratory\n\
// under National Science Foundation under Grant No. CNS-0855268,\n\
// the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and\n\
// by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"),\n\
// as part of the DARPA MRC research programme.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_START@\n\
//\n\
// Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor\n\
// license agreements.  See the NOTICE file distributed with this work for\n\
// additional information regarding copyright ownership.  NetFPGA licenses this\n\
// file to you under the NetFPGA Hardware-Software License, Version 1.0 (the\n\
// "License"); you may not use this file except in compliance with the\n\
// License.  You may obtain a copy of the License at:\n\
//\n\
//   http://www.netfpga-cic.org\n\
//\n\
// Unless required by applicable law or agreed to in writing, Work distributed\n\
// under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\n\
// CONDITIONS OF ANY KIND, either express or implied.  See the License for the\n\
// specific language governing permissions and limitations under the License.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_END@\n\
//\n\
\n')

#end of write_h_header


##################################################################
# a function that writes the header of regs table file
##################################################################
def write_tbFile_header(tbFile):
      tbFile.write('\
//\n\
// Copyright (c) 2015 University of Cambridge\n\
// All rights reserved.\n\
//\n\
//\n\
//  File:\n\
//        '+module_name+'_regs_defines.txt\n\
//\n\
//  Description:\n\
//        This file is automatically generated with header defines for the software\n\
//\n\
// This software was developed by Stanford University and the University of Cambridge Computer Laboratory\n\
// under National Science Foundation under Grant No. CNS-0855268,\n\
// the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and\n\
// by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"),\n\
// as part of the DARPA MRC research programme.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_START@\n\
//\n\
// Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor\n\
// license agreements.  See the NOTICE file distributed with this work for\n\
// additional information regarding copyright ownership.  NetFPGA licenses this\n\
// file to you under the NetFPGA Hardware-Software License, Version 1.0 (the\n\
// "License"); you may not use this file except in compliance with the\n\
// License.  You may obtain a copy of the License at:\n\
//\n\
//   http://www.netfpga-cic.org\n\
//\n\
// Unless required by applicable law or agreed to in writing, Work distributed\n\
// under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\n\
// CONDITIONS OF ANY KIND, either express or implied.  See the License for the\n\
// specific language governing permissions and limitations under the License.\n\
//\n\
// @NETFPGA_LICENSE_HEADER_END@\n\
//\n\
\n')

##################################################################
#A funtion that writes the ports of the regs moduledefault
##################################################################

def write_regs_ports(regsFile,regsDict, memsDict):

   regsFile.write('`include "'+module_name+'_cpu_regs_defines.v"\n\
\
module '+module_name+'_cpu_regs #\n\
(\n\
parameter C_BASE_ADDRESS        = 32\'h00000000,\n\
parameter C_S_AXI_DATA_WIDTH    = 32,\n\
parameter C_S_AXI_ADDR_WIDTH    = 32\n\
)\n\
(\n\
    // General ports\n\
    input       clk,\n\
    input       resetn,\n\
    // Global Registers\n\
    input       cpu_resetn_soft,\n\
    output reg  resetn_soft,\n\
    output reg  resetn_sync,\n\
\n\
   // Register ports\n')

   for entry in regsDict:
     if entry['type']=="RO" :
       regsFile.write('    input      [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg,\n')
     if entry['type']=="ROC" :
       regsFile.write('    input      [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg,\n')
       regsFile.write('    output reg                          '+entry['name']+'_reg_clear,\n')
     if entry['type']=="RWS" :
       regsFile.write('    output reg [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg,\n')
     if entry['type']=="WO" :
       regsFile.write('    output reg [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg,\n')
     if entry['type']=="WOE" :
       regsFile.write('    output reg [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg,\n')
     if entry['type']=="RWA" :
       regsFile.write('    input      [`REG_'+(entry['name']).upper()+'_BITS]    ip2cpu_'+entry['name']+'_reg,\n')
       regsFile.write('    output reg [`REG_'+(entry['name']).upper()+'_BITS]    cpu2ip_'+entry['name']+'_reg,\n')
     if entry['type']=="RWCR" :
       regsFile.write('    input      [`REG_'+(entry['name']).upper()+'_BITS]    ip2cpu_'+entry['name']+'_reg,\n')
       regsFile.write('    output reg [`REG_'+(entry['name']).upper()+'_BITS]    cpu2ip_'+entry['name']+'_reg,\n')
       regsFile.write('    output reg                          cpu2ip_'+entry['name']+'_reg_clear,\n')
     if entry['type']=="RWCW" :
       regsFile.write('    input      [`REG_'+(entry['name']).upper()+'_BITS]    ip2cpu_'+entry['name']+'_reg,\n')
       regsFile.write('    output reg [`REG_'+(entry['name']).upper()+'_BITS]    cpu2ip_'+entry['name']+'_reg,\n')
       regsFile.write('    output reg                          cpu2ip_'+entry['name']+'_reg_clear,\n')

   for entry in memsDict:
       regsFile.write('    output  reg [`MEM_'+(entry['name']).upper()+'_ADDR_BITS]    '+entry['name']+'_addr,\n')
       regsFile.write('    output  reg [`MEM_'+(entry['name']).upper()+'_DATA_BITS]    '+entry['name']+'_data,\n')
       regsFile.write('    output  reg                         '+entry['name']+'_rd_wrn,\n')
       regsFile.write('    output  reg                         '+entry['name']+'_cmd_valid,\n')
       regsFile.write('    input       [`MEM_'+(entry['name']).upper()+'_DATA_BITS]    '+entry['name']+'_reply,\n')
       regsFile.write('    input                               '+entry['name']+'_reply_valid,\n')       
  
   regsFile.write('\n\
    // AXI Lite ports\n\
    input                                     S_AXI_ACLK,\n\
    input                                     S_AXI_ARESETN,\n\
    input      [C_S_AXI_ADDR_WIDTH-1 : 0]     S_AXI_AWADDR,\n\
    input                                     S_AXI_AWVALID,\n\
    input      [C_S_AXI_DATA_WIDTH-1 : 0]     S_AXI_WDATA,\n\
    input      [C_S_AXI_DATA_WIDTH/8-1 : 0]   S_AXI_WSTRB,\n\
    input                                     S_AXI_WVALID,\n\
    input                                     S_AXI_BREADY,\n\
    input      [C_S_AXI_ADDR_WIDTH-1 : 0]     S_AXI_ARADDR,\n\
    input                                     S_AXI_ARVALID,\n\
    input                                     S_AXI_RREADY,\n\
    output                                    S_AXI_ARREADY,\n\
    output     [C_S_AXI_DATA_WIDTH-1 : 0]     S_AXI_RDATA,\n\
    output     [1 : 0]                        S_AXI_RRESP,\n\
    output                                    S_AXI_RVALID,\n\
    output                                    S_AXI_WREADY,\n\
    output     [1 :0]                         S_AXI_BRESP,\n\
    output                                    S_AXI_BVALID,\n\
    output                                    S_AXI_AWREADY\n\
\n\
);\n');
#end of write_regs_ports

##################################################################
#A funtion that writes the wires and regs of the registers module
##################################################################
def write_regs_wires(regsFile,regsDict,memsDict):

    regsFile.write('\n\
    // AXI4LITE signals\n\
    reg [C_S_AXI_ADDR_WIDTH-1 : 0]      axi_awaddr;\n\
    reg                                 axi_awready;\n\
    reg                                 axi_wready;\n\
    reg [1 : 0]                         axi_bresp;\n\
    reg                                 axi_bvalid;\n\
    reg [C_S_AXI_ADDR_WIDTH-1 : 0]      axi_araddr;\n\
    reg                                 axi_arready;\n\
    reg [C_S_AXI_DATA_WIDTH-1 : 0]      axi_rdata;\n\
    reg [1 : 0]                         axi_rresp;\n\
    reg                                 axi_rvalid;\n\
\n\
    reg                                 resetn_sync_d;\n\
    wire                                reg_rden;\n\
    wire                                reg_wren;\n\
    reg [C_S_AXI_DATA_WIDTH-1:0]        reg_data_out;\n\
    integer                             byte_index;\n');

    for entry in regsDict:
        if entry['type']=="RWCW" :
            regsFile.write('\
    reg                                 cpu2ip_'+entry['name']+'_reg_clear_d;\n')

    for entry in regsDict:
        if entry['type']=="ROC" :
            regsFile.write('\
    reg                                 '+entry['name']+'_reg_clear_d;\n')

    for entry in regsDict:
            if entry['type']=="RWSI" or entry['type']=="ROI" :
                regsFile.write('\
    reg      [`REG_'+(entry['name']).upper()+'_BITS] '+entry['name']+'_reg;\n')

    for entry in regsDict:
            if entry['type']=="RWI" :
                regsFile.write('\
    reg      [`REG_'+(entry['name']).upper()+'_BITS] '+entry['name']+'_reg;\n\
    reg      [`REG_'+(entry['name']).upper()+'_BITS] '+entry['name']+'_reg_internal;\n\
    reg      '+entry['name']+'_reg_update;\n') 
    
    for entry in regsDict:
        if entry['endian']=="big" :
            regsFile.write('\n\
    // assign default little endian\n');
            regsFile.write('\
    wire [C_S_AXI_DATA_WIDTH-1 : 0]     reg_'+entry['name']+'_default_little;\n');

    for entry in regsDict:
        if entry['endian']=="big" :
            regsFile.write('\
    assign  reg_'+entry['name']+'_default_little = `REG_'+entry['name'].upper()+'_DEFAULT;\n');

    regsFile.write('\n\
    // I/O Connections assignments\n\
    assign S_AXI_AWREADY    = axi_awready;\n\
    assign S_AXI_WREADY     = axi_wready;\n\
    assign S_AXI_BRESP      = axi_bresp;\n\
    assign S_AXI_BVALID     = axi_bvalid;\n\
    assign S_AXI_ARREADY    = axi_arready;\n\
    assign S_AXI_RDATA      = axi_rdata;\n\
    assign S_AXI_RRESP      = axi_rresp;\n\
    assign S_AXI_RVALID     = axi_rvalid;\n\
\n');


#end of write_regs_wires


##################################################################
#sync reset signal for better timing
##################################################################
def sync_reset(regsFile):

    regsFile.write('\n\
    //Sample reset (not mandatory, but good practice)\n\
    always @ (posedge clk) begin\n\
        if (~resetn) begin\n\
            resetn_sync_d  <=  1\'b0;\n\
            resetn_sync    <=  1\'b0;\n\
        end\n\
        else begin\n\
            resetn_sync_d  <=  resetn;\n\
            resetn_sync    <=  resetn_sync_d;\n\
        end\n\
    end\n\
\n');

# for now, only global reset is supported, to demonstrate usage
    regsFile.write('\n\
    //global registers, sampling\n\
    always @(posedge clk) resetn_soft <= #1 cpu_resetn_soft;\n');


#end of sync_reset

##################################################################
# a function that writes the logic behind the registers access
##################################################################
def write_logic(regsFile,regsDict):
# boolean first_item;


# axi protocol generation

    regsFile.write('\n\
    // Implement axi_awready generation\n\
\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_awready <= 1\'b0;\n\
        end\n\
      else\n\
        begin\n\
          if (~axi_awready && S_AXI_AWVALID && S_AXI_WVALID)\n\
            begin\n\
              // slave is ready to accept write address when\n\
              // there is a valid write address and write data\n\
              // on the write address and data bus. This design\n\
              // expects no outstanding transactions.\n\
              axi_awready <= 1\'b1;\n\
            end\n\
          else\n\
            begin\n\
              axi_awready <= 1\'b0;\n\
            end\n\
        end\n\
    end\n\
\n\
    // Implement axi_awaddr latching\n\
\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_awaddr <= 0;\n\
        end\n\
      else\n\
        begin\n\
          if (~axi_awready && S_AXI_AWVALID && S_AXI_WVALID)\n\
            begin\n\
              // Write Address latching\n\
              axi_awaddr <= S_AXI_AWADDR ^ C_BASE_ADDRESS;\n\
            end\n\
        end\n\
    end\n\
\n\
    // Implement axi_wready generation\n\
\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_wready <= 1\'b0;\n\
        end\n\
      else\n\
        begin\n\
          if (~axi_wready && S_AXI_WVALID && S_AXI_AWVALID)\n\
            begin\n\
              // slave is ready to accept write data when\n\
              // there is a valid write address and write data\n\
              // on the write address and data bus. This design\n\
              // expects no outstanding transactions.\n\
              axi_wready <= 1\'b1;\n\
            end\n\
          else\n\
            begin\n\
              axi_wready <= 1\'b0;\n\
            end\n\
        end\n\
    end\n\
\n\
    // Implement write response logic generation\n\
\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_bvalid  <= 0;\n\
          axi_bresp   <= 2\'b0;\n\
        end\n\
      else\n\
        begin\n\
          if (axi_awready && S_AXI_AWVALID && ~axi_bvalid && axi_wready && S_AXI_WVALID)\n\
            begin\n\
              // indicates a valid write response is available\n\
              axi_bvalid <= 1\'b1;\n\
              axi_bresp  <= 2\'b0; // OKAY response\n\
            end                   // work error responses in future\n\
          else\n\
            begin\n\
              if (S_AXI_BREADY && axi_bvalid)\n\
                //check if bready is asserted while bvalid is high)\n\
                //(there is a possibility that bready is always asserted high)\n\
                begin\n\
                  axi_bvalid <= 1\'b0;\n\
                end\n\
            end\n\
        end\n\
    end\n\
\n\
    // Implement axi_arready generation\n\
\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_arready <= 1\'b0;\n\
          axi_araddr  <= 32\'b0;\n\
        end\n\
      else\n\
        begin\n\
          if (~axi_arready && S_AXI_ARVALID)\n\
            begin\n\
              // indicates that the slave has acceped the valid read address\n\
              // Read address latching\n\
              axi_arready <= 1\'b1;\n\
              axi_araddr  <= S_AXI_ARADDR ^ C_BASE_ADDRESS;\n\
            end\n\
          else\n\
            begin\n\
              axi_arready <= 1\'b0;\n\
            end\n\
        end\n\
    end\n\
\n\
\n\
    // Implement axi_rvalid generation\n\
\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_rvalid <= 0;\n\
          axi_rresp  <= 0;\n\
        end\n\
      else\n\
        begin\n\
          if (axi_arready && S_AXI_ARVALID && ~axi_rvalid)\n\
            begin\n\
              // Valid read data is available at the read data bus\n\
              axi_rvalid <= 1\'b1;\n\
              axi_rresp  <= 2\'b0; // OKAY response\n\
            end\n\
          else if (axi_rvalid && S_AXI_RREADY)\n\
            begin\n\
              // Read data is accepted by the master\n\
              axi_rvalid <= 1\'b0;\n\
            end\n\
        end\n\
    end\n\
\n\
\n');


    regsFile.write('\
    // Implement memory mapped register select and write logic generation\n\
\n\
    assign reg_wren = axi_wready && S_AXI_WVALID && axi_awready && S_AXI_AWVALID;\n\
\n\
//////////////////////////////////////////////////////////////\n\
// write registers\n\
//////////////////////////////////////////////////////////////\n\
\n');

#Handle write only registers
    first_item=True; 

    for entry in regsDict:
        if entry['type']=="WO" :
            if first_item:
                regsFile.write('\n\
//Write only register, not cleared\n\
    //static\n\
    always @(posedge clk)\n\
        if (!resetn_sync) begin\n');
                first_item=False;

                if entry['endian']=="little" :
                    regsFile.write('\
            '+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

                if entry['endian']=="big" :
                    regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

    if not(first_item):
        regsFile.write('        end\n\
        else begin\n\
            if (reg_wren) begin //write event\n\
                case (axi_awaddr)\n');


    for entry in regsDict:
        if entry['type']=="WO" :
            if entry['endian']=="little" :
                regsFile.write('                //'+entry['name'].capitalize()+' Register\n\
                    `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                        for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                            if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                                '+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8];\n\
                            end\n\
                    end\n');
            if entry['endian']=="big" :
                regsFile.write('                //'+entry['name'].capitalize()+' Register\n\
                    `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                            if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                                '+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                            end\n\
                    end\n');

    if not(first_item):
        regsFile.write('\
                endcase\n\
            end\n\
        end\n');


#Handle write only event registers

    first_item=True; 

    for entry in regsDict:
        if entry['type']=="WOE" :
            if first_item:
                first_item= False;
                regsFile.write('\n\
//Write only register, clear on write (i.e. event)\n\
    always @(posedge clk) begin\n\
        if (!resetn_sync) begin\n');
                if entry['endian']=="little" :
                    regsFile.write('\
            '+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');
                if entry['endian']=="big" :
                    regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

    if not(first_item):
        regsFile.write('        end\n\
        else begin\n\
            if (reg_wren) begin\n\
                case (axi_awaddr)\n');

    for entry in regsDict:
        if entry['type']=="WOE" :
            if entry['endian']=="little" :
                regsFile.write('\
                    //'+entry['name'].capitalize()+' Register\n\
                        `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                                for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                                    if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                                        '+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8];\n\
                                    end\n\
                        end\n');
            if entry['endian']=="big" :
                regsFile.write('\
                    //'+entry['name'].capitalize()+' Register\n\
                        `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                                for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                                    if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                                        '+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                                    end\n\
                        end\n');

    if not(first_item):
        regsFile.write('\
                endcase\n\
            end\n\
            else begin\n');
        
        for entry in regsDict:
            if entry['type']=="WOE" :
                if entry['endian']=="little" :
                    regsFile.write('\
                '+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

                if entry['endian']=="big" :
                    regsFile.write('\
                for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

        regsFile.write('\
            end\n\
        end\n\
    end\n');


#Handle Read/write registers, not cleared

    first_item=True;

    for entry in regsDict:
        if first_item and (entry['type']=="RWS" or entry['type']=="RWA"):
            first_item = False;
            regsFile.write('\n\
//R/W register, not cleared\n\
    always @(posedge clk) begin\n\
        if (!resetn_sync) begin\n\
\n');

        if entry['type']=="RWS" :
            if entry['endian']=="little" :
                regsFile.write('\
            '+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

            if entry['endian']=="big" :
                regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

        if entry['type']=="RWA" :
            if entry['endian']=="little" :
                regsFile.write('\
            cpu2ip_'+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

            if entry['endian']=="big" :
                regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');


        if entry['type']=="RWSI" :
            if entry['endian']=="little" :
                regsFile.write('\
            '+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');
            
        if entry['endian']=="big" :
                regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');
            

        if entry['type']=="RWI" :      
            if entry['endian']=="little" :
                regsFile.write('\
            '+entry['name']+'_reg_internal <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

            if entry['endian']=="big" :
                regsFile.write('\
             for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                '+entry['name']+'_reg_internal[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');


    if not(first_item):
        regsFile.write('\
        end\n\
        else begin\n\
           if (reg_wren) //write event\n\
            case (axi_awaddr)\n');

    for entry in regsDict:
        if entry['type']=="RWS" :
            if entry['endian']=="little" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            '+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //static register;\n\
                        end\n\
                end\n');
            if entry['endian']=="big" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            '+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                        end\n\
                end\n');
                
        if entry['type']=="RWA" :
            if entry['endian']=="little" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;\n\
                        end\n\
                end\n');
            if entry['endian']=="big" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                        end\n\
                end\n');

        if entry['type']=="RWSI" :
            if entry['endian']=="little" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            '+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //static register;\n\
                        end\n\
                end\n');
            if entry['endian']=="big" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            '+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                        end\n\
                end\n');

        if entry['type']=="RWI" :
            if entry['endian']=="little" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            '+entry['name']+'_reg_internal[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //static register;\n\
                        end\n\
                end\n');
            if entry['endian']=="big" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
                `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                    for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            '+entry['name']+'_reg_internal[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                        end\n\
                end\n');

    if not (first_item):
        regsFile.write('\
                default: begin\n\
                end\n\
\n\
            endcase\n\
        end\n');
                        
    for entry in regsDict:
       if entry['type']=="RWI" :
          regsFile.write('   '+entry['name']+'_reg_update <= reg_wren && (axi_awaddr == `REG_'+entry['name'].upper()+'_ADDR);\n');
    
    if not (first_item):
             regsFile.write('  end\n');
    
#Handle Read/write registers, clear on read

    first_item=True;

    for entry in regsDict:
        if entry['type']=="RWCR" :
            if first_item:
                first_item = False;
                regsFile.write('\n\
//R/W register, clear on read\n\
    always @(posedge clk) begin\n\
        if (!resetn_sync) begin\n\
\n');

            if entry['endian']=="little" :
                regsFile.write('\
            cpu2ip_'+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

            if entry['endian']=="big" :
                regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

    if not (first_item):
        regsFile.write('\
        end\n\
        else begin\n\
            if (reg_wren)\n\
                case (axi_awaddr)\n');

    for entry in regsDict:
        if entry['type']=="RWCR" :
            if entry['endian']=="little" :
                regsFile.write('\
                    //'+entry['name'].capitalize()+' Register\n\
                    `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                        for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                            if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                                cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8];\n\
                            end\n\
                    end\n');
            if entry['endian']=="big" :
                regsFile.write('\
                    //'+entry['name'].capitalize()+' Register\n\
                    `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                            if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                                cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                            end\n\
                    end\n');

    if not(first_item):
        regsFile.write('\
                endcase\n\
        end\n\
    end\n\
\n\
\n\
//clear assertions\n\
    always @(posedge clk) begin\n\
        if (!resetn_sync) begin\n');

    for entry in regsDict:
        if entry['type']=="RWCR" :
            regsFile.write('\
            cpu2ip_'+entry['name']+'_reg_clear <=  #1 1\'b0;\n');

    if not(first_item):
        regsFile.write('\
        end\n\
        else begin\n');

    for entry in regsDict:
        if entry['type']=="RWCR" :
            regsFile.write('\
             cpu2ip_'+entry['name']+'_reg_clear <=  #1 reg_rden && (axi_awaddr==`REG_'+entry['name'].upper()+'_ADDR) ? 1\'b1 : 1\'b0;\n');
        
    if not(first_item):
        regsFile.write('\n\
        end\n\
    end\n');



#Handle Read/write registers, clear on write

    first_item= True;

    for entry in regsDict:
        if entry['type']=="RWCW" :
            first_item = False;
            regsFile.write('\n\
//R/W register, clear on write, dynamic\n\
// i.e. on write - write, next clock - write default value\n\
    always @(posedge clk) begin\n\
        if (!resetn_sync) begin\n');

            if entry['endian']=="little" :
                regsFile.write('\
            cpu2ip_'+entry['name']+'_reg <= #1 `REG_'+entry['name'].upper()+'_DEFAULT;\n');

            if entry['endian']=="big" :
                regsFile.write('\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

            regsFile.write('\
            cpu2ip_'+entry['name']+'_reg_clear_d <= #1 1\'b0;\n\
            cpu2ip_'+entry['name']+'_reg_clear   <= #1 1\'b0;\n');

    if not(first_item):
        regsFile.write('\
        end\n\
        else begin\n');

    for entry in regsDict:
        if entry['type']=="RWCW" :
            regsFile.write('\
            cpu2ip_'+entry['name']+'_reg_clear   <=  cpu2ip_'+entry['name']+'_reg_clear_d;\n\
            cpu2ip_'+entry['name']+'_reg_clear_d <=  reg_wren && (axi_awaddr==`REG_'+entry['name'].upper()+'_ADDR) ? 1\'b1 :  1\'b0;\n');

    if not(first_item):
        regsFile.write('\
            if (reg_wren) begin\n');

    for entry in regsDict:
        if entry['type']=="RWCW" :
            if entry['endian']=="little" :
                regsFile.write('\
                if (axi_awaddr==`REG_'+entry['name'].upper()+'_ADDR) begin\n\
                    for ( byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index+1 )\n\
                        if ( S_AXI_WSTRB[byte_index] == 1 ) begin\n\
                            cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8];\n\
                        end\n\
                end\n');
            if entry['endian']=="big" :
                regsFile.write('\
                if (axi_awaddr==`REG_'+entry['name'].upper()+'_ADDR) begin\n\
                    for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                        if (S_AXI_WSTRB[byte_index] == 1) begin\n\
                            cpu2ip_'+entry['name']+'_reg[byte_index*8 +: 8] <= S_AXI_WDATA[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8]; //dynamic register;\n\
                        end\n\
                end\n');

    if not(first_item):
        regsFile.write('\
            end\n\
        end\n\
    end\n');

    regsFile.write('\
\n\
\n\
\n\
/////////////////////////\n\
//// end of write\n\
/////////////////////////\n');

    regsFile.write('\n\
    // Implement memory mapped register select and read logic generation\n\
    // Slave register read enable is asserted when valid address is available\n\
    // and the slave is ready to accept the read address.\n\
\n\
    // reg_rden control logic\n\
    // temperary no extra logic here\n\
    assign reg_rden = axi_arready & S_AXI_ARVALID & ~axi_rvalid;\n');

#return read data 
    regsFile.write('\n\
    always @(*)\n\
    begin\n\
\n\
        case ( axi_araddr /*S_AXI_ARADDR ^ C_BASE_ADDRESS*/)\n');
    
    for entry in regsDict:
        if  entry['type']=="RO" or entry['type']=="ROC" or entry['type']=="RWS" or entry['type']=="RWI" or entry['type']=="RWSI" or entry['type']=="ROI":
            if entry['endian']=="little" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
            `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                reg_data_out [`REG_'+entry['name'].upper()+'_BITS] =  '+entry['name']+'_reg;\n');
                
            if entry['endian']=="big" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
            `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                    reg_data_out [byte_index*8 +: 8] = '+entry['name']+'_reg [(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

            if int(entry['width'])<32:
                regsFile.write('\
                reg_data_out [31:`REG_'+entry['name'].upper()+'_WIDTH] =  \'b0;\n');
            
            regsFile.write('\
            end\n');
        
        if entry['type']=="RWCW" or entry['type']=="RWA" or entry['type']=="RWCR":
            if entry['endian']=="little" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
            `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                reg_data_out [`REG_'+entry['name'].upper()+'_BITS] =  ip2cpu_'+entry['name']+'_reg;\n');
                
            if entry['endian']=="big" :
                regsFile.write('\
            //'+entry['name'].capitalize()+' Register\n\
            `REG_'+entry['name'].upper()+'_ADDR : begin\n\
                for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                    reg_data_out [byte_index*8 +: 8] = ip2cpu_'+entry['name']+'_reg[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');
            
            if int(entry['width']) < 32 :
                regsFile.write('\
                reg_data_out [31:`REG_'+entry['name'].upper()+'_WIDTH] =  \'b0;\n');
            
            regsFile.write('\
            end\n');
    
    regsFile.write('\
            //Default return value\n\
            default: begin\n\
                reg_data_out [31:0] =  32\'hDEADBEEF;\n\
            end\n\
\n\
        endcase\n\
\n\
    end//end of assigning data to IP2Bus_Data bus\n');

#Handle read only registers
    first_item=True;

    for entry in regsDict:
        if entry['type']=="ROC" :
            if first_item:
                first_item=False;
                regsFile.write('\n\
    //Read only registers, not cleared\n\
    //Nothing to do here....\n\
\n\
//Read only registers, cleared on read (e.g. counters)\n\
    always @(posedge clk)\n\
    if (!resetn_sync) begin\n');

            regsFile.write('\
        '+entry['name']+'_reg_clear <= #1 1\'b0;\n\
        '+entry['name']+'_reg_clear_d <= #1 1\'b0;\n');

    if not(first_item):
        regsFile.write('    end\n\
    else begin\n');

    for entry in regsDict:
        if entry['type']=="ROC" :
            regsFile.write('\
        '+entry['name']+'_reg_clear <= #1 '+entry['name']+'_reg_clear_d;\n\
        '+entry['name']+'_reg_clear_d <= #1(reg_rden && (axi_araddr==`REG_'+entry['name'].upper()+'_ADDR)) ? 1\'b1 : 1\'b0;\n');

    if not(first_item):
        regsFile.write('    end\n\n');

    regsFile.write('\n\
// Output register or memory read data\n\
    always @( posedge S_AXI_ACLK )\n\
    begin\n\
      if ( S_AXI_ARESETN == 1\'b0 )\n\
        begin\n\
          axi_rdata  <= 0;\n\
        end\n\
      else\n\
        begin\n\
          // When there is a valid read address (S_AXI_ARVALID) with\n\
          // acceptance of read address by the slave (axi_arready),\n\
          // output the read dada\n\
          if (reg_rden)\n\
            begin\n\
              axi_rdata <= reg_data_out/*ip2bus_data*/;     // register read data /* some new changes here */\n\
            end\n\
        end\n\
    end\n');

# end of write_logic

##################################################################
# a function that writes the logic behind the indirect registers access
##################################################################
def write_indirect(regsFile,memsDict):
  regsFile.write('\n\
    //////////////////////////////////\n\
    // Implement Indirect Access\n\
	//////////////////////////////////\n\
	\n');
	
  regsFile.write('\n\
  //--------------------- Internal Parameters-------------------------\n\
   localparam NUM_INDIRECT_STATES                = 6;\n\
   localparam IDLE_INDIRECT_STATE                = 1;\n\
   localparam WRITE_INDIRECT_STATE               = 2;\n\
   localparam WRITE_WAIT_INDIRECT_STATE          = 4;\n\
   localparam READ_INDIRECT_STATE                = 8;\n\
   localparam READ_WAIT_INDIRECT_STATE           = 16;\n\
   localparam INDIRECT_DONE_STATE                = 32;\n\
   localparam INDIRECT_WRITE                     = 0;\n\
   localparam INDIRECT_READ                      = 1;\n\
   localparam INDIRECT_WRITE_TA                  = 1;\n\
   localparam INDIRECT_WRITE_WS                  = 0;\n\
  //------------------------------------------------------------------\n\
   \n\
   reg  [NUM_INDIRECT_STATES-1:0]           indirect_state, indirect_state_next, indirect_state_last;\n\
   wire                            indirect_trigger;\n\
   wire                            indirect_type;\n\
   reg                             indirect_status, indirect_status_next;\n\
   wire [3:0]                      indirect_address_increment;\n\
   wire                            indirect_write_type;\n\
   wire [10:0]                     indirect_timeout;\n\
   wire [15:0]                     indirect_repeat_count;\n\
   reg  [15:0]                     indirect_remaining,indirect_remaining_next;\n\
   reg  [10:0]                     indirect_timeout_count, indirect_timeout_count_next;\n\
   reg                             indirect_reply_valid;\n\
   reg  [31:0]                     indirect_address,indirect_address_next;\n\
   reg  [3:0]                      indirect_memory_select,indirect_memory_select_next;\n\
   wire                             indirect_command_done;\n\
   \n\
   assign   indirect_trigger = indirectcommand_reg[0];\n\
   assign   indirect_type    = indirectcommand_reg[4];\n\
   assign   indirect_address_increment = indirectconfig_reg[3:0];\n\
   assign   indirect_write_type = indirectconfig_reg[4];\n\
   assign   indirect_timeout    = indirectconfig_reg[15:5];\n\
   assign   indirect_repeat_count = indirectconfig_reg[31:16];\n\
   \n\
 always @(*) begin\n\
      indirect_state_next   = indirect_state;\n\
      indirect_status_next  = indirect_status;\n\
      indirect_remaining_next = indirect_remaining;\n\
      indirect_timeout_count_next = indirect_timeout_count;\n\
      indirect_address_next      = indirect_address;\n\
      indirect_memory_select_next = indirect_memory_select;\n\
      case(indirect_state)\n\
        IDLE_INDIRECT_STATE: begin\n\
     	   if(indirect_trigger) begin\n\
     	      indirect_state_next= (indirect_type == INDIRECT_WRITE) ? WRITE_INDIRECT_STATE : READ_INDIRECT_STATE;\n\
     	      indirect_remaining_next = (indirect_repeat_count == 0) ? 16\'h1 : indirect_repeat_count;\n\
     	      indirect_timeout_count_next   = indirect_timeout;\n\
     	      indirect_address_next   =  indirectaddress_reg; //This is the address in the user register\n\
     	      indirect_memory_select_next = indirectaddress_reg[31:28];\n\
     	   end\n\
	    end\n\
	    \n\
	    READ_INDIRECT_STATE: begin\n\
		     indirect_state_next = READ_WAIT_INDIRECT_STATE;\n\
	    end\n\
	    READ_WAIT_INDIRECT_STATE: begin\n\
	         if (indirect_reply_valid) begin\n\
	            indirect_state_next = INDIRECT_DONE_STATE;\n\
	            indirect_status_next =0;\n\
	         end\n\
	         if (indirect_timeout_count==0) begin\n\
	            indirect_state_next = INDIRECT_DONE_STATE;\n\
	            indirect_status_next = 1; \n\
	         end\n\
	         indirect_timeout_count_next = indirect_timeout_count-1;\n\
	     end\n\
	     WRITE_INDIRECT_STATE: begin\n\
	         indirect_state_next = WRITE_WAIT_INDIRECT_STATE;\n\
	     end\n\
	     WRITE_WAIT_INDIRECT_STATE:  begin\n\
	         if (((indirect_write_type == INDIRECT_WRITE_TA) && (indirect_reply_valid)) || ((indirect_write_type == INDIRECT_WRITE_WS) && (indirect_timeout_count==0))) begin\n\
	           indirect_remaining_next = indirect_remaining - 1;\n\
	           indirect_address_next = indirect_address+indirect_address_increment;\n\
	           if (indirect_remaining==1) begin\n\
	              indirect_state_next = INDIRECT_DONE_STATE;\n\
	           end\n\
	         end\n\
	         else \n\
	           if (indirect_timeout_count==0) begin\n\
	         	indirect_state_next = INDIRECT_DONE_STATE;\n\
	         	indirect_status_next = 1; \n\
	         end\n\
             indirect_timeout_count_next = indirect_timeout_count==0 ? 0 : indirect_timeout_count-1;\n\
	     end\n\
	     INDIRECT_DONE_STATE: begin\n\
	        indirect_state_next= IDLE_INDIRECT_STATE;\n\
	     end\n\
	     default: begin\n\
	         indirect_state_next= IDLE_INDIRECT_STATE;\n\
	     end\n\
      endcase // case(state)\n\
   end // always @ (*)\n\
   \n\
    assign indirect_command_done = (indirect_state==INDIRECT_DONE_STATE);\n\
   \n\
   always @(posedge clk) begin\n\
      if(~resetn_sync) begin\n\
         indirect_state <= #1 IDLE_INDIRECT_STATE;\n\
         indirect_state_last <= #1 IDLE_INDIRECT_STATE;\n\
         indirect_status <= #1 1\'b0;\n\
         indirect_remaining <= #1 0;\n\
         indirect_timeout_count <= #1 0;\n\
         indirect_address   <= #1 0;\n\
         indirect_memory_select <= #1 0;\n\
         indirectcommand_reg <= #1 `REG_INDIRECTCOMMAND_DEFAULT;\n\
      end\n\
      else begin\n\
         indirect_state <= #1 indirect_state_next;\n\
         indirect_state_last <= #1 indirect_state;\n\
         indirect_status <= #1 indirect_status_next;\n\
         indirect_remaining <= #1 indirect_remaining_next;\n\
         indirect_timeout_count <= #1 indirect_timeout_count_next;\n\
         indirect_address   <= #1  indirect_address_next;\n\
         indirect_memory_select <= #1 indirect_memory_select_next;\n\
         indirectcommand_reg <= #1  indirect_command_done ? {indirect_status,indirectcommand_reg[7:4],4\'h0} : \n\
                                    indirectcommand_reg_update ? indirectcommand_reg_internal: \n\
                                    indirectcommand_reg;\n\
      end\n\
   end   \n\
   \n');


  for entry in memsDict:
     regsFile.write('\n\
       \n\
       always @(posedge clk) begin\n\
         if  (~resetn_sync) begin\n\
           '+entry['name']+'_addr <= #1 0;\n\
           '+entry['name']+'_data <= #1 0;\n\
           '+entry['name']+'_rd_wrn<= #1 0;\n\
           '+entry['name']+'_cmd_valid <= #1 0;\n\
         end \n\
         else begin\n\
           '+entry['name']+'_addr <= #1 indirect_address;\n\
           '+entry['name']+'_data <= #1 indirectwrdata_reg;\n\
           '+entry['name']+'_rd_wrn<= #1 indirect_type;\n\
           '+entry['name']+'_cmd_valid <= #1 ('+entry['address']+'==(indirect_memory_select<<28)) && ((indirect_state == WRITE_INDIRECT_STATE) || (indirect_state == READ_INDIRECT_STATE));\n\
         end \n\
       end\n');
       
  regsFile.write('\n\
       always @(posedge clk) begin\n\
          if  (~resetn_sync) begin\n\
             indirectreply_reg <= #1 0;\n\
             indirect_reply_valid <= #1 0; \n\
          end \n\
          else begin \n\
             indirectreply_reg <= #1 ' );
  for entry in memsDict:
      regsFile.write(entry['address']+'==(indirect_memory_select<<28) ? '+entry['name']+'_reply :');
  regsFile.write(' 0;\n\
      indirect_reply_valid <= #1 ');
  for entry in memsDict:
      regsFile.write(entry['address']+'==(indirect_memory_select<<28) ? '+entry['name']+'_reply_valid :');
  regsFile.write(' 0;\n\
          end \n\
        end\n\
  \n');
# end of write_indirect

##################################################################
#write all the defines to the defs module
##################################################################
def write_defines(defsFile,regsDict, memsDict):

   for entry in regsDict:
      defsFile.write(	'\n`define  REG_'+entry['name'].upper()+'_BITS\t\t\t\t'+entry['bits']+
			'\n`define  REG_'+entry['name'].upper()+'_WIDTH\t\t\t\t'+entry['width']+
			'\n`define  REG_'+entry['name'].upper()+'_DEFAULT\t\t\t\t'+entry['default']+
			'\n`define  REG_'+entry['name'].upper()+'_ADDR\t\t\t\t'+entry['addr']+'\n');

   for entry in memsDict:
      defsFile.write(	'\n`define  MEM_'+entry['name'].upper()+'_DATA_BITS\t\t\t\t'+entry['data_bits']+
			'\n`define  MEM_'+entry['name'].upper()+'_ADDR_BITS\t\t\t\t'+entry['addr_bits']+
			'\n`define  MEM_'+entry['name'].upper()+'_WIDTH\t\t\t\t'+entry['width']+
			'\n`define  MEM_'+entry['name'].upper()+'_DEPTH\t\t\t\t'+str(2**(int(entry['addr_bits'].split(':')[0])+1))+
			'\n`define  MEM_'+entry['name'].upper()+'_ADDR\t\t\t\t'+entry['address']+'\n');
 
#end of write_defines


##################################################################
#write all the register offsets to the h template (to be included)
##################################################################
def write_h(hFile,regsDict,memsDict):

   hFile.write('##########This text should be copied to the head file #############\n\
   #Registers offset definitions\n\n');
   
   for entry in regsDict:
      hFile.write('#define SUME_'+block_name+'_'+entry['name'].upper()+'_0_OFFSET 0x'+entry['addr'][4:]+'\n');
      hFile.write('#define SUME_'+block_name+'_'+entry['name'].upper()+'_0_DEFAULT 0x'+entry['default'].split("'h")[-1]+'\n');
      hFile.write('#define SUME_'+block_name+'_'+entry['name'].upper()+'_0_WIDTH '+entry['width']+'\n');

   for entry in memsDict:
     hFile.write('#define SUME_'+block_name+'_MEM_'+entry['name'].upper()+'_0_WIDTH '+entry['width']+'\n');
     hFile.write('#define SUME_'+block_name+'_MEM_'+entry['name'].upper()+'_0_DEPTH '+str(2**(int(entry['addr_bits'].split(':')[0])+1))+'\n');
     hFile.write('#define SUME_'+block_name+'_MEM_'+entry['name'].upper()+'_0_ADDRESS 0x'+entry['address'].split("'h")[-1]+'\n');

#end of write_h

##################################################################
#write all the register offsets to the tcl file
##################################################################
def write_tcl(tclFile,regsDict,memsDict):

   for entry in regsDict:
     tclFile.write('set '+block_name+'_REGS_'+entry['name'].upper()+'_0_OFFSET 0x'+entry['addr'][4:]+'\n');
     tclFile.write('set '+block_name+'_REGS_'+entry['name'].upper()+'_0_DEFAULT 0x'+entry['default'].split("'h")[-1]+'\n');
     tclFile.write('set '+block_name+'_REGS_'+entry['name'].upper()+'_0_WIDTH '+entry['width']+'\n');

   for entry in memsDict:
     tclFile.write('set '+block_name+'_MEM_'+entry['name'].upper()+'_0_WIDTH '+entry['width']+'\n');
     tclFile.write('set '+block_name+'_MEM_'+entry['name'].upper()+'_0_DEPTH '+str(2**(int(entry['addr_bits'].split(':')[0])+1))+'\n');
     tclFile.write('set '+block_name+'_MEM_'+entry['name'].upper()+'_0_ADDRESS 0x'+entry['address'].split("'h")[-1]+'\n');
     

#end of write_tcl

##################################################################
#write all the register offsets to table
##################################################################

def write_tb(tbFile,regsDict,memsDict):
   for entry in regsDict:
      tbFile.write('#define SUME '+block_name+' '+entry['name'].upper()+' OFFSET 0x'+entry['addr'][4:]+'\n');
      tbFile.write('#define SUME '+block_name+' '+entry['name'].upper()+' DEFAULT 0x'+entry['default'].split("'h")[-1]+'\n');
      tbFile.write('#define SUME '+block_name+' '+entry['name'].upper()+' WIDTH '+entry['width']+'\n');

   for entry in memsDict:
      tbFile.write('#define  SUME '+block_name+' MEM_'+entry['name'].upper()+' WIDTH '+entry['width']+'\n');
      tbFile.write('#define  SUME '+block_name+' MEM_'+entry['name'].upper()+' DEPTH '+str(2**(int(entry['addr_bits'].split(':')[0])+1))+'\n');
      tbFile.write('#define  SUME '+block_name+' MEM_'+entry['name'].upper()+' ADDRESS 0x'+entry['address'].split("'h")[-1]+'\n');
#end of write_tb

##################################################################
#write top module's template (i.e. include this in your module)
##################################################################
def write_module_template(moduleFile,regsDict,memsDict):

#first write static inclusions....
  moduleFile.write('`include "'+module_name+'_cpu_regs_defines.v"\n\
\n\
//parameters to be added to the top module parameters\n\
#(\n\
    // AXI Registers Data Width\n\
    parameter C_S_AXI_DATA_WIDTH    = 32,\n\
    parameter C_S_AXI_ADDR_WIDTH    = 32\n\
)\n\
//ports to be added to the top module ports\n\
(\n\
// Signals for AXI_IP and IF_REG (Added for debug purposes)\n\
    // Slave AXI Ports\n\
    input                                     S_AXI_ACLK,\n\
    input                                     S_AXI_ARESETN,\n\
    input      [C_S_AXI_ADDR_WIDTH-1 : 0]     S_AXI_AWADDR,\n\
    input                                     S_AXI_AWVALID,\n\
    input      [C_S_AXI_DATA_WIDTH-1 : 0]     S_AXI_WDATA,\n\
    input      [C_S_AXI_DATA_WIDTH/8-1 : 0]   S_AXI_WSTRB,\n\
    input                                     S_AXI_WVALID,\n\
    input                                     S_AXI_BREADY,\n\
    input      [C_S_AXI_ADDR_WIDTH-1 : 0]     S_AXI_ARADDR,\n\
    input                                     S_AXI_ARVALID,\n\
    input                                     S_AXI_RREADY,\n\
    output                                    S_AXI_ARREADY,\n\
    output     [C_S_AXI_DATA_WIDTH-1 : 0]     S_AXI_RDATA,\n\
    output     [1 : 0]                        S_AXI_RRESP,\n\
    output                                    S_AXI_RVALID,\n\
    output                                    S_AXI_WREADY,\n\
    output     [1 :0]                         S_AXI_BRESP,\n\
    output                                    S_AXI_BVALID,\n\
    output                                    S_AXI_AWREADY\n\
)\n\n');

  first_item = True;
  for entry in regsDict:
    if first_item and (entry['endian']=="big") :
        first_item = False;
        moduleFile.write('\n\
    // define and assign default little endian\n');

  for entry in regsDict:
     if entry['endian']=="big" :
            moduleFile.write('\
    wire                                      reg_'+entry['name']+'_default_little;\n');

  for entry in regsDict:
     if entry['endian']=="big" :
            moduleFile.write('\
    assign  reg_'+entry['name']+'_default_little = `REG_'+entry['name'].upper()+'_DEFAULT;\n');

#then add design specific wires/regs:

  moduleFile.write('\n\
    // define registers\n');

  for entry in regsDict:
     if entry['type']=="RO" :
       moduleFile.write('    reg      [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg;\n')
     if entry['type']=="ROC" :
       moduleFile.write('    reg      [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg;\n')
       moduleFile.write('    wire                             '+entry['name']+'_reg_clear;\n')
     if entry['type']=="RWS" :
       moduleFile.write('    wire     [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg;\n')
     if entry['type']=="WO" :
       moduleFile.write('    wire     [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg;\n')
     if entry['type']=="WOE" :
       moduleFile.write('    wire     [`REG_'+(entry['name']).upper()+'_BITS]    '+entry['name']+'_reg;\n')
     if entry['type']=="RWA" :
       moduleFile.write('    reg      [`REG_'+(entry['name']).upper()+'_BITS]    ip2cpu_'+entry['name']+'_reg;\n')
       moduleFile.write('    wire     [`REG_'+(entry['name']).upper()+'_BITS]    cpu2ip_'+entry['name']+'_reg;\n')
     if entry['type']=="RWCR" :
       moduleFile.write('    reg      [`REG_'+(entry['name']).upper()+'_BITS]    ip2cpu_'+entry['name']+'_reg;\n')
       moduleFile.write('    wire     [`REG_'+(entry['name']).upper()+'_BITS]    cpu2ip_'+entry['name']+'_reg;\n')
       moduleFile.write('    wire                             cpu2ip_'+entry['name']+'_reg_clear;\n')
     if entry['type']=="RWCW" :
       moduleFile.write('    reg      [`REG_'+(entry['name']).upper()+'_BITS]    ip2cpu_'+entry['name']+'_reg;\n')
       moduleFile.write('    wire     [`REG_'+(entry['name']).upper()+'_BITS]    cpu2ip_'+entry['name']+'_reg;\n')
       moduleFile.write('    wire                             cpu2ip_'+entry['name']+'_reg_clear;\n')
       moduleFile.write('    wire                             cpu2ip_'+entry['name']+'_reg_clear_d;\n')

  for entry in memsDict:
       moduleFile.write('    wire      [`MEM_'+(entry['name']).upper()+'_ADDR_BITS]    '+entry['name']+'_addr;\n')
       moduleFile.write('    wire      [`MEM_'+(entry['name']).upper()+'_DATA_BITS]    '+entry['name']+'_data;\n')
       moduleFile.write('    wire                              '+entry['name']+'_rd_wrn;\n')
       moduleFile.write('    wire                              '+entry['name']+'_cmd_valid;\n')
       moduleFile.write('    reg       [`MEM_'+(entry['name']).upper()+'DATA_BITS]    '+entry['name']+'_reply;\n')
       moduleFile.write('    reg                               '+entry['name']+'_reply_valid;\n')       


#instantiate registers module
  moduleFile.write('\n//Registers section\n\
 '+module_name+'_cpu_regs\n\
 #(\n\
     .C_BASE_ADDRESS        (C_BASEADDR ),\n\
     .C_S_AXI_DATA_WIDTH    (C_S_AXI_DATA_WIDTH),\n\
     .C_S_AXI_ADDR_WIDTH    (C_S_AXI_ADDR_WIDTH)\n\
 ) '+module_name+'_cpu_regs_inst\n\
 (\n\
   // General ports\n\
    .clk                    (axis_aclk),\n\
    .resetn                 (axis_resetn),\n\
   // AXI Lite ports\n\
    .S_AXI_ACLK             (S_AXI_ACLK),\n\
    .S_AXI_ARESETN          (S_AXI_ARESETN),\n\
    .S_AXI_AWADDR           (S_AXI_AWADDR),\n\
    .S_AXI_AWVALID          (S_AXI_AWVALID),\n\
    .S_AXI_WDATA            (S_AXI_WDATA),\n\
    .S_AXI_WSTRB            (S_AXI_WSTRB),\n\
    .S_AXI_WVALID           (S_AXI_WVALID),\n\
    .S_AXI_BREADY           (S_AXI_BREADY),\n\
    .S_AXI_ARADDR           (S_AXI_ARADDR),\n\
    .S_AXI_ARVALID          (S_AXI_ARVALID),\n\
    .S_AXI_RREADY           (S_AXI_RREADY),\n\
    .S_AXI_ARREADY          (S_AXI_ARREADY),\n\
    .S_AXI_RDATA            (S_AXI_RDATA),\n\
    .S_AXI_RRESP            (S_AXI_RRESP),\n\
    .S_AXI_RVALID           (S_AXI_RVALID),\n\
    .S_AXI_WREADY           (S_AXI_WREADY),\n\
    .S_AXI_BRESP            (S_AXI_BRESP),\n\
    .S_AXI_BVALID           (S_AXI_BVALID),\n\
    .S_AXI_AWREADY          (S_AXI_AWREADY),\n\
\n\
   // Register ports\n');

  for entry in regsDict:
     if entry['type']=="RO"  :
       moduleFile.write('   .'+entry['name']+'_reg          ('+entry['name']+'_reg),\n')
     if entry['type']=="ROC" :
       moduleFile.write('   .'+entry['name']+'_reg          ('+entry['name']+'_reg),\n')
       moduleFile.write('   .'+entry['name']+'_reg_clear    ('+entry['name']+'_reg_clear),\n')
     if entry['type']=="RWS" :
       moduleFile.write('   .'+entry['name']+'_reg          ('+entry['name']+'_reg),\n')
     if entry['type']=="WO" :
       moduleFile.write('   .'+entry['name']+'_reg          ('+entry['name']+'_reg),\n')
     if entry['type']=="WOE" :
       moduleFile.write('   .'+entry['name']+'_reg          ('+entry['name']+'_reg),\n')
     if entry['type']=="RWA" :
       moduleFile.write('   .ip2cpu_'+entry['name']+'_reg          (ip2cpu_'+entry['name']+'_reg),\n')
       moduleFile.write('   .cpu2ip_'+entry['name']+'_reg          (cpu2ip_'+entry['name']+'_reg),\n')
     if entry['type']=="RWCR" :
       moduleFile.write('   .ip2cpu_'+entry['name']+'_reg          (ip2cpu_'+entry['name']+'_reg),\n')
       moduleFile.write('   .cpu2ip_'+entry['name']+'_reg          (cpu2ip_'+entry['name']+'_reg),\n')
       moduleFile.write('   .cpu2ip_'+entry['name']+'_reg_clear    (cpu2ip_'+entry['name']+'_reg_clear),\n')
     if entry['type']=="RWCW" :
       moduleFile.write('   .ip2cpu_'+entry['name']+'_reg          (ip2cpu_'+entry['name']+'_reg),\n')
       moduleFile.write('   .cpu2ip_'+entry['name']+'_reg          (cpu2ip_'+entry['name']+'_reg),\n')
       moduleFile.write('   .cpu2ip_'+entry['name']+'_reg_clear    (cpu2ip_'+entry['name']+'_reg_clear),\n')

  for entry in memsDict:
       moduleFile.write('    .'+entry['name']+'_addr          ('+entry['name']+'_addr),\n')
       moduleFile.write('    .'+entry['name']+'_data          ('+entry['name']+'_data),\n')
       moduleFile.write('    .'+entry['name']+'_rd_wrn        ('+entry['name']+'_rd_wrn),\n')
       moduleFile.write('    .'+entry['name']+'_cmd_valid     ('+entry['name']+'_cmd_valid ),\n')
       moduleFile.write('    .'+entry['name']+'_reply         ('+entry['name']+'_reply),\n')
       moduleFile.write('    .'+entry['name']+'_reply_valid   ('+entry['name']+'_reply_valid),\n')       


  moduleFile.write('   // Global Registers - user can select if to use\n\
   .cpu_resetn_soft(),//software reset, after cpu module\n\
   .resetn_soft    (),//software reset to cpu module (from central reset management)\n\
   .resetn_sync    (resetn_sync)//synchronized reset, use for better timing\n\
);\n\
//registers logic, current logic is just a placeholder for initial compil, required to be changed by the user\n');

#registers logic

  moduleFile.write('always @(posedge axis_aclk)\n\
	if (~resetn_sync) begin\n');

  for entry in regsDict:
     if entry['type']=="RO"  :
       if entry['endian']=="little":
         moduleFile.write('\
        '+entry['name']+'_reg <= #1    `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
            '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

     if entry['type']=="ROC" :
       if entry['endian']=="little":
         moduleFile.write('\
        '+entry['name']+'_reg <= #1    `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
            '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

     if entry['type']=="RWA" :
       if entry['endian']=="little":
         moduleFile.write('\
        ip2cpu_'+entry['name']+'_reg <= #1    `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
            ip2cpu_'+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

     if entry['type']=="RWCR" :
       if entry['endian']=="little":
         moduleFile.write('\
        ip2cpu_'+entry['name']+'_reg <= #1    `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
            ip2cpu_'+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

     if entry['type']=="RWCW" :
       if entry['endian']=="little":
         moduleFile.write('\
        ip2cpu_'+entry['name']+'_reg <= #1    `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
            ip2cpu_'+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

       moduleFile.write('		cpu_'+entry['name']+'_reg_clear_d <= #1    \'h0\n;')
      
  moduleFile.write('	end\n\
	else begin\n')
  for entry in regsDict:
     if entry['type']=="RO"  :
       if entry['endian']=="little":
         moduleFile.write('\
        '+entry['name']+'_reg <= #1    `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
            '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');

     if entry['type']=="ROC" :
       if entry['endian']=="little":
         moduleFile.write('\
        '+entry['name']+'_reg <= #1 '+entry['name']+'_reg_clear ? \'h0  : `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        if ('+entry['name']+'_reg_clear == 1\'b1) \n\
            '+entry['name']+'_reg <= #1 \'h0;\n\
        else\n\
            for (byte_index = 0; byte_index <= (`REG_'+entry['name'].upper()+'_WIDTH/8-1); byte_index = byte_index +1)\n\
                '+entry['name']+'_reg[byte_index*8 +: 8] <= reg_'+entry['name']+'_default_little[(C_S_AXI_DATA_WIDTH/8-byte_index-1)*8 +: 8];\n');


     if entry['type']=="RWA" :
       moduleFile.write('		ip2cpu_'+entry['name']+'_reg <= #1 cpu2ip_'+entry['name']+'_reg;\n')

     if entry['type']=="RWCR" :
       if entry['endian']=="little":
         moduleFile.write('\
        ip2cpu_'+entry['name']+'_reg <= #1 '+entry['name']+'_reg_clear ? \'h0  : `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        if ('+entry['name']+'_reg_clear == 1\'b1) \n\
            '+entry['name']+'_reg <= #1 \'h0;\n\
        else\n\
            ip2cpu_'+entry['name']+'_reg <= #1 cpu2ip_'+entry['name']+'_reg;');

     if entry['type']=="RWCW" :
       if entry['endian']=="little":
         moduleFile.write('\
        ip2cpu_'+entry['name']+'_reg <= #1 '+entry['name']+'_reg_clear ? \'h0  : `REG_'+entry['name'].upper()+'_DEFAULT;\n');
       if entry['endian']=="big":
         moduleFile.write('\
        if ('+entry['name']+'_reg_clear_d == 1\'b1) \n\
            ip2cpu_'+entry['name']+'_reg <= #1 \'h0;\n\
        else\n\
            ip2cpu_'+entry['name']+'_reg <= #1 cpu2ip_'+entry['name']+'_reg;');
       moduleFile.write('		cpu_'+entry['name']+'_reg_clear_d <= #1    cpu_'+entry['name']+'_reg_clear;\n')

  moduleFile.write('\
        end\n\n')



#end of write_module_template


########################################################################################
#
# Main function body
#
########################################################################################


# List of files to be generated.
filename_regs=''+module_name+'_cpu_regs.v'
filename_defs=''+module_name+'_cpu_regs_defines.v'
filename_template=''+module_name+'_cpu_template.v'
filename_h=''+module_name+'_regs_defines.h' 
filename_tcl=''+module_name+'_regs_defines.tcl'
filename_tb=''+module_name+'_regs_defines.txt'


# Open the files for writing
regsFile = open(filename_regs, 'w')
defsFile = open(filename_defs, 'w')
moduleFile = open(filename_template, 'w')
hFile = open(filename_h, 'w')
tclFile = open(filename_tcl, 'w')
tbFile = open(filename_tb, 'w')

# Write the header of each file
write_regs_header(regsFile)
write_defs_header(defsFile)
write_tcl_header(tclFile)
write_hFile_header(hFile)
write_tbFile_header(tbFile)

#Write the regs module
#first the ports...
regsDict=create_regs_list()
memsDict=create_mems_list()
write_regs_ports(regsFile,regsDict, memsDict)


#then the wires...
write_regs_wires(regsFile,regsDict, memsDict)

#resets etc.....
sync_reset(regsFile)


#registers logic...
write_logic(regsFile,regsDict)

#indirect access...
if memsDict:
  write_indirect(regsFile,memsDict)

#tables...

#close module.....
regsFile.write('endmodule\n')

#write the defs module
write_defines(defsFile,regsDict, memsDict)

#write the tcl module
write_tcl(tclFile,regsDict, memsDict)

#write the default text to be copied to the h module
write_h(hFile,regsDict, memsDict)

#write the default text to table file
write_tb(tbFile,regsDict, memsDict)

#writes the default text to be copied to the top module
write_module_template(moduleFile,regsDict, memsDict)


# Close the output files
regsFile.close()
defsFile.close()
tclFile.close()
moduleFile.close()
hFile.close()
tbFile.close()
