//-
// Copyright (c) 2015 University of Cambridge
// Copyright (c) 2015 Noa Zilberman
// All rights reserved.
//
// This software was developed by the University of Cambridge Computer Laboratory 
// under EPSRC INTERNET Project EP/H040536/1, National Science Foundation under Grant No. CNS-0855268,
// and Defense Advanced Research Projects Agency (DARPA) and Air Force Research Laboratory (AFRL), 
// under contract FA8750-11-C-0249.
//
// @NETFPGA_LICENSE_HEADER_START@
//
// Licensed to NetFPGA Open Systems C.I.C. (NetFPGA) under one or more contributor
// license agreements.  See the NOTICE file distributed with this work for
// additional information regarding copyright ownership.  NetFPGA licenses this
// file to you under the NetFPGA Hardware-Software License, Version 1.0 (the
// "License"); you may not use this file except in compliance with the
// License.  You may obtain a copy of the License at:
//
//   http://www.netfpga-cic.org
//
// Unless required by applicable law or agreed to in writing, Work distributed
// under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
// CONDITIONS OF ANY KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations under the License.
//
// @NETFPGA_LICENSE_HEADER_END@
//



`include "crypto_cpu_regs_defines.v"

module crypto
#(
    //Master AXI Stream Data Width
    parameter C_M_AXIS_DATA_WIDTH=256,
    parameter C_S_AXIS_DATA_WIDTH=256,
    parameter C_M_AXIS_TUSER_WIDTH=128,
    parameter C_S_AXIS_TUSER_WIDTH=128,
    parameter SRC_PORT_POS=16,
    parameter DST_PORT_POS=24,

 // AXI Registers Data Width
    parameter C_S_AXI_DATA_WIDTH    = 32,          
    parameter C_S_AXI_ADDR_WIDTH    = 12,          
    parameter C_USE_WSTRB           = 0,	   
    parameter C_DPHASE_TIMEOUT      = 0,               
    parameter C_NUM_ADDRESS_RANGES = 1,
    parameter  C_TOTAL_NUM_CE       = 1,
    parameter  C_S_AXI_MIN_SIZE    = 32'h0000_FFFF,
    //parameter [0:32*2*C_NUM_ADDRESS_RANGES-1]   C_ARD_ADDR_RANGE_ARRAY  = 
    //                                             {2*C_NUM_ADDRESS_RANGES
    //                                              {32'h00000000}
    //                                             },
    parameter [0:8*C_NUM_ADDRESS_RANGES-1] C_ARD_NUM_CE_ARRAY  = 
                                                {
                                                 C_NUM_ADDRESS_RANGES{8'd1}
                                                 },
    parameter     C_FAMILY            = "virtex7", 
    parameter C_BASEADDR            = 32'h00000000,
    parameter C_HIGHADDR            = 32'h0000FFFF


)
(
    // Global Ports
    input axis_aclk,
    input axis_resetn,

    // Master Stream Ports (interface to data path)
    output reg [C_M_AXIS_DATA_WIDTH - 1:0] m_axis_tdata,
    output reg [((C_M_AXIS_DATA_WIDTH / 8)) - 1:0] m_axis_tkeep,
    output reg [C_M_AXIS_TUSER_WIDTH-1:0] m_axis_tuser,
    output reg m_axis_tvalid,
    input   m_axis_tready,
    output reg m_axis_tlast,

    // Slave Stream Ports (interface to RX queues)
    input [C_S_AXIS_DATA_WIDTH - 1:0] s_axis_tdata,
    input [((C_S_AXIS_DATA_WIDTH / 8)) - 1:0] s_axis_tkeep,
    input [C_S_AXIS_TUSER_WIDTH-1:0] s_axis_tuser,
    input  s_axis_tvalid,
    output s_axis_tready,
    input  s_axis_tlast,

// Slave AXI Ports
    input                                     S_AXI_ACLK,
    input                                     S_AXI_ARESETN,
    input      [C_S_AXI_ADDR_WIDTH-1 : 0]     S_AXI_AWADDR,
    input                                     S_AXI_AWVALID,
    input      [C_S_AXI_DATA_WIDTH-1 : 0]     S_AXI_WDATA,
    input      [C_S_AXI_DATA_WIDTH/8-1 : 0]   S_AXI_WSTRB,
    input                                     S_AXI_WVALID,
    input                                     S_AXI_BREADY,
    input      [C_S_AXI_ADDR_WIDTH-1 : 0]     S_AXI_ARADDR,
    input                                     S_AXI_ARVALID,
    input                                     S_AXI_RREADY,
    output                                    S_AXI_ARREADY,
    output     [C_S_AXI_DATA_WIDTH-1 : 0]     S_AXI_RDATA,
    output     [1 : 0]                        S_AXI_RRESP,
    output                                    S_AXI_RVALID,
    output                                    S_AXI_WREADY,
    output     [1 :0]                         S_AXI_BRESP,
    output                                    S_AXI_BVALID,
    output                                    S_AXI_AWREADY
);

    // define registers
reg      [`REG_ID_BITS]    id_reg;
reg      [`REG_VERSION_BITS]    version_reg;
wire     [`REG_RESET_BITS]    reset_reg;
reg      [`REG_FLIP_BITS]    ip2cpu_flip_reg;
wire     [`REG_FLIP_BITS]    cpu2ip_flip_reg;
reg      [`REG_DEBUG_BITS]    ip2cpu_debug_reg;
wire     [`REG_DEBUG_BITS]    cpu2ip_debug_reg;
reg      [`REG_PKTIN_BITS]    pktin_reg;
wire                             pktin_reg_clear;
reg      [`REG_PKTOUT_BITS]    pktout_reg;
wire                             pktout_reg_clear;
reg      [`REG_ETHERTYPE_BITS]    ip2cpu_ethertype_reg, ip2cpu_ethertype_reg_next;
wire     [`REG_ETHERTYPE_BITS]    cpu2ip_ethertype_reg;
reg      [`REG_TCI_BITS]    ip2cpu_tci_reg, ip2cpu_tci_reg_next;
wire     [`REG_TCI_BITS]    cpu2ip_tci_reg;
reg      [`REG_SLEN_BITS]    ip2cpu_slen_reg, ip2cpu_slen_reg_next;
wire     [`REG_SLEN_BITS]    cpu2ip_slen_reg;
reg      [`REG_PNUM_BITS]    ip2cpu_pnum_reg, ip2cpu_pnum_reg_next;
wire     [`REG_PNUM_BITS]    cpu2ip_pnum_reg;
reg      [`REG_ICV_BITS]    ip2cpu_icv_reg, ip2cpu_icv_reg_next;
wire     [`REG_ICV_BITS]    cpu2ip_icv_reg;
reg      [`REG_MACSEC_PKTS_BITS]    ip2cpu_macsec_pkts_reg, ip2cpu_macsec_pkts_reg_next;
wire     [`REG_MACSEC_PKTS_BITS]    cpu2ip_macsec_pkts_reg;
reg      [`REG_OTHER_PKTS_BITS]    ip2cpu_other_pkts_reg, ip2cpu_other_pkts_reg_next;
wire     [`REG_OTHER_PKTS_BITS]    cpu2ip_other_pkts_reg;
wire      [`MEM_TESTMEM_ADDR_BITS]    testmem_addr;
wire      [`MEM_TESTMEM_DATA_BITS]    testmem_data;
wire                              testmem_rd_wrn;
wire                              testmem_cmd_valid;
reg       [`MEM_TESTMEM_DATA_BITS]    testmem_reply;
reg                               testmem_reply_valid;

   function integer log2;
      input integer number;
      begin
         log2=0;
         while(2**log2<number) begin
            log2=log2+1;
         end
      end
   endfunction // log2

   // ------------- Regs/ wires -----------
   // FIFO
   wire                             fifo_nearly_full;
   wire                             fifo_empty;
   reg                              fifo_rd_en;
   wire [C_M_AXIS_TUSER_WIDTH-1:0]  fifo_out_tuser;
   wire [C_M_AXIS_DATA_WIDTH-1:0]   fifo_out_tdata;
   wire [C_M_AXIS_DATA_WIDTH/8-1:0] fifo_out_tkeep;
   wire  	                    fifo_out_tlast;
   wire                             fifo_tvalid;
   wire                             fifo_tlast;

   // MacSec
   localparam MAC_SEC_ETHERTYPE = 16'hE588;             // Little endian encoded
   localparam MAC_SEC_HDR_LENGTH = 64;
   
   // FSM
   localparam MACSEC_DETECT_STATE   = 1;
   localparam PKT_HDR_WORD1         = 2;
   localparam PKT_PAYLOAD           = 4;
   localparam COPY_STATE            = 8; 
   reg  [4:0]                       state, next_state;
   
   integer i;
   reg [7:0] bytes [31:0];
   reg [7:0] sum [32:0];
   
   // ------------ Modules -------------

   fallthrough_small_fifo
   #( .WIDTH(C_M_AXIS_DATA_WIDTH+C_M_AXIS_TUSER_WIDTH+C_M_AXIS_DATA_WIDTH/8+1),
      .MAX_DEPTH_BITS(2)
    )
    input_fifo
    ( // Outputs
      .dout                         ({fifo_out_tlast, fifo_out_tuser, fifo_out_tkeep, fifo_out_tdata}),
      .full                         (),
      .nearly_full                  (fifo_nearly_full),
      .prog_full                    (),
      .empty                        (fifo_empty),
      // Inputs
      .din                          ({s_axis_tlast, s_axis_tuser, s_axis_tkeep, s_axis_tdata}),
      .wr_en                        (s_axis_tvalid & s_axis_tready),
      .rd_en                        (fifo_rd_en),
      .reset                        (~axis_resetn),
      .clk                          (axis_aclk));

   // ------------- Logic ------------

   assign s_axis_tready = !fifo_nearly_full;

  /*********************************************************************
   * Wait until the ethernet header has been decoded and the output
   * port is found, then write the module header and move the packet
   * to the output
   **********************************************************************/
   always @* begin
     m_axis_tuser = fifo_out_tuser;
     m_axis_tdata = fifo_out_tdata;
     m_axis_tkeep = fifo_out_tkeep;
     m_axis_tlast = fifo_out_tlast;
     m_axis_tvalid = 0;
     
     fifo_rd_en = 0;
     ip2cpu_ethertype_reg_next   = ip2cpu_ethertype_reg;
     ip2cpu_tci_reg_next 		 = ip2cpu_tci_reg;
     ip2cpu_slen_reg_next 		 = ip2cpu_slen_reg;
     ip2cpu_pnum_reg_next 		 = ip2cpu_pnum_reg;
     ip2cpu_macsec_pkts_reg_next = ip2cpu_macsec_pkts_reg;
     ip2cpu_other_pkts_reg_next  = ip2cpu_other_pkts_reg;
     ip2cpu_icv_reg_next         = ip2cpu_icv_reg;
     sum[0]                      = ip2cpu_icv_reg[7:0];     
     
     next_state = state;

     case(state)
       MACSEC_DETECT_STATE: begin
         m_axis_tvalid = !fifo_empty;         

         if (m_axis_tvalid && m_axis_tready) begin
            ip2cpu_ethertype_reg_next = m_axis_tdata[111:96];
            fifo_rd_en = 1;
                                    
            // Check if we have a ethernet paket       
            if (m_axis_tdata[111:96] == MAC_SEC_ETHERTYPE) begin
                ip2cpu_tci_reg_next = m_axis_tdata[119:112];
                ip2cpu_slen_reg_next = m_axis_tdata[127:120];
                ip2cpu_pnum_reg_next = m_axis_tdata[159:128];
                ip2cpu_macsec_pkts_reg_next = ip2cpu_macsec_pkts_reg + 1;
            
                ip2cpu_icv_reg_next = {24'h0, sum[32]};
                                    
                // ICV first bytes computation
                // ...
                
                next_state = COPY_STATE;          
            end
            
            // Otherwise; we will ignore everything
            else begin
                ip2cpu_other_pkts_reg_next = ip2cpu_other_pkts_reg + 1;
                ip2cpu_tci_reg_next = 0;
                ip2cpu_slen_reg_next = 0;
                ip2cpu_pnum_reg_next = 0;
                ip2cpu_icv_reg_next = 0;
                next_state = COPY_STATE;
            end

         end
       end
       

        COPY_STATE: begin
            m_axis_tvalid = !fifo_empty;         
        
            if (m_axis_tvalid && m_axis_tready) begin
                fifo_rd_en = 1;
                
                if (fifo_out_tlast) begin
                    next_state = MACSEC_DETECT_STATE;
                end
            end
        end  

     endcase 
   end

   always @(posedge axis_aclk) begin
     if (~axis_resetn) begin
       state       <= MACSEC_DETECT_STATE;
     end

     else begin
       state <= next_state;
     end
   end
   
   
   // Checksum adder block
   always @* begin
   for (i = 0; i <= 31; i=i+1) begin
        bytes[i] = m_axis_tdata[i*8 +: 8];
        sum[i+1] = sum[i] + bytes[i];
     end
   end


   
   
//Registers section
    crypto_cpu_regs
    #(
        .C_BASE_ADDRESS        (C_BASEADDR ),
        .C_S_AXI_DATA_WIDTH    (C_S_AXI_DATA_WIDTH),
        .C_S_AXI_ADDR_WIDTH    (C_S_AXI_ADDR_WIDTH)
    ) crypto_cpu_regs_inst
    (
      // General ports
       .clk                    (axis_aclk),
       .resetn                 (axis_resetn),
      // AXI Lite ports
       .S_AXI_ACLK             (S_AXI_ACLK),
       .S_AXI_ARESETN          (S_AXI_ARESETN),
       .S_AXI_AWADDR           (S_AXI_AWADDR),
       .S_AXI_AWVALID          (S_AXI_AWVALID),
       .S_AXI_WDATA            (S_AXI_WDATA),
       .S_AXI_WSTRB            (S_AXI_WSTRB),
       .S_AXI_WVALID           (S_AXI_WVALID),
       .S_AXI_BREADY           (S_AXI_BREADY),
       .S_AXI_ARADDR           (S_AXI_ARADDR),
       .S_AXI_ARVALID          (S_AXI_ARVALID),
       .S_AXI_RREADY           (S_AXI_RREADY),
       .S_AXI_ARREADY          (S_AXI_ARREADY),
       .S_AXI_RDATA            (S_AXI_RDATA),
       .S_AXI_RRESP            (S_AXI_RRESP),
       .S_AXI_RVALID           (S_AXI_RVALID),
       .S_AXI_WREADY           (S_AXI_WREADY),
       .S_AXI_BRESP            (S_AXI_BRESP),
       .S_AXI_BVALID           (S_AXI_BVALID),
       .S_AXI_AWREADY          (S_AXI_AWREADY),
   
      // Register ports
      .id_reg          (id_reg),
      .version_reg          (version_reg),
      .reset_reg          (reset_reg),
      .ip2cpu_flip_reg          (ip2cpu_flip_reg),
      .cpu2ip_flip_reg          (cpu2ip_flip_reg),
      .ip2cpu_debug_reg          (ip2cpu_debug_reg),
      .cpu2ip_debug_reg          (cpu2ip_debug_reg),
      .pktin_reg          (pktin_reg),
      .pktin_reg_clear    (pktin_reg_clear),
      .pktout_reg          (pktout_reg),
      .pktout_reg_clear    (pktout_reg_clear),
      .ip2cpu_ethertype_reg          (ip2cpu_ethertype_reg),
      .cpu2ip_ethertype_reg          (cpu2ip_ethertype_reg),
      .ip2cpu_tci_reg          (ip2cpu_tci_reg),
      .cpu2ip_tci_reg          (cpu2ip_tci_reg),
      .ip2cpu_slen_reg          (ip2cpu_slen_reg),
      .cpu2ip_slen_reg          (cpu2ip_slen_reg),
      .ip2cpu_pnum_reg          (ip2cpu_pnum_reg),
      .cpu2ip_pnum_reg          (cpu2ip_pnum_reg),
      .ip2cpu_icv_reg          (ip2cpu_icv_reg),
      .cpu2ip_icv_reg          (cpu2ip_icv_reg),
      .ip2cpu_macsec_pkts_reg          (ip2cpu_macsec_pkts_reg),
      .cpu2ip_macsec_pkts_reg          (cpu2ip_macsec_pkts_reg),
      .ip2cpu_other_pkts_reg          (ip2cpu_other_pkts_reg),
      .cpu2ip_other_pkts_reg          (cpu2ip_other_pkts_reg),
       .testmem_addr          (testmem_addr),
       .testmem_data          (testmem_data),
       .testmem_rd_wrn        (testmem_rd_wrn),
       .testmem_cmd_valid     (testmem_cmd_valid ),
       .testmem_reply         (testmem_reply),
       .testmem_reply_valid   (testmem_reply_valid),
      // Global Registers - user can select if to use
      .cpu_resetn_soft(),//software reset, after cpu module
      .resetn_soft    (),//software reset to cpu module (from central reset management)
      .resetn_sync    (resetn_sync)//synchronized reset, use for better timing
   );
   
   //registers logic, current logic is just a placeholder for initial compil, required to be changed by the user
   always @(posedge axis_aclk)
       if (~resetn_sync) begin
           id_reg <= #1    `REG_ID_DEFAULT;
           version_reg <= #1    `REG_VERSION_DEFAULT;
           ip2cpu_flip_reg <= #1    `REG_FLIP_DEFAULT;
           ip2cpu_debug_reg <= #1    `REG_DEBUG_DEFAULT;
           pktin_reg <= #1    `REG_PKTIN_DEFAULT;
           pktout_reg <= #1    `REG_PKTOUT_DEFAULT;
           ip2cpu_ethertype_reg <= #1    `REG_ETHERTYPE_DEFAULT;
           ip2cpu_tci_reg <= #1    `REG_TCI_DEFAULT;
           ip2cpu_slen_reg <= #1    `REG_SLEN_DEFAULT;
           ip2cpu_pnum_reg <= #1    `REG_PNUM_DEFAULT;
           ip2cpu_icv_reg <= #1    `REG_ICV_DEFAULT;
           ip2cpu_macsec_pkts_reg <= #1    `REG_MACSEC_PKTS_DEFAULT;
           ip2cpu_other_pkts_reg <= #1    `REG_OTHER_PKTS_DEFAULT;
       end

       else begin
           id_reg <= #1    `REG_ID_DEFAULT;
           version_reg <= #1    `REG_VERSION_DEFAULT;
           ip2cpu_flip_reg <= #1 cpu2ip_flip_reg;
           ip2cpu_debug_reg <= #1 cpu2ip_debug_reg;
           pktin_reg <= #1 pktin_reg_clear ? 'h0  : `REG_PKTIN_DEFAULT;
           pktout_reg <= #1 pktout_reg_clear ? 'h0  : `REG_PKTOUT_DEFAULT;
           ip2cpu_ethertype_reg <= #1 ip2cpu_ethertype_reg_next;
           ip2cpu_tci_reg <= #1 ip2cpu_tci_reg_next;
           ip2cpu_slen_reg <= #1 ip2cpu_slen_reg_next;
           ip2cpu_pnum_reg <= #1 ip2cpu_pnum_reg_next;
                      
           if (reset_reg[0]) begin
                ip2cpu_macsec_pkts_reg <= `REG_MACSEC_PKTS_DEFAULT;
                ip2cpu_other_pkts_reg  <= `REG_OTHER_PKTS_DEFAULT;
                ip2cpu_icv_reg <= #1    `REG_ICV_DEFAULT;
           end    
           else begin 
                ip2cpu_macsec_pkts_reg <= #1 ip2cpu_macsec_pkts_reg_next;
                ip2cpu_other_pkts_reg  <= #1 ip2cpu_other_pkts_reg_next;
                ip2cpu_icv_reg <= #1 ip2cpu_icv_reg_next;      
           end
                
           
       end




endmodule // crypto
