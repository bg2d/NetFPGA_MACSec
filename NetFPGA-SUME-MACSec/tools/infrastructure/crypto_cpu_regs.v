//
// Copyright (c) 2015 University of Cambridge
// All rights reserved.
//
//
//  File:
//        crypto_cpu_regs.v
//
//  Module:
//        crypto_cpu_regs
//
//  Description:
//        This file is automatically generated with the registers towards the CPU/Software
//
// This software was developed by Stanford University and the University of Cambridge Computer Laboratory
// under National Science Foundation under Grant No. CNS-0855268,
// the University of Cambridge Computer Laboratory under EPSRC INTERNET Project EP/H040536/1 and
// by the University of Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-11-C-0249 ("MRC2"),
// as part of the DARPA MRC research programme.
//
// @NETFPGA_LICENSE_HEADER_START@
//
// Licensed to NetFPGA C.I.C. (NetFPGA) under one or more contributor
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
module crypto_cpu_regs #
(
parameter C_BASE_ADDRESS        = 32'h00000000,
parameter C_S_AXI_DATA_WIDTH    = 32,
parameter C_S_AXI_ADDR_WIDTH    = 32
)
(
    // General ports
    input       clk,
    input       resetn,
    // Global Registers
    input       cpu_resetn_soft,
    output reg  resetn_soft,
    output reg  resetn_sync,

   // Register ports
    input      [`REG_ID_BITS]    id_reg,
    input      [`REG_VERSION_BITS]    version_reg,
    output reg [`REG_RESET_BITS]    reset_reg,
    input      [`REG_FLIP_BITS]    ip2cpu_flip_reg,
    output reg [`REG_FLIP_BITS]    cpu2ip_flip_reg,
    input      [`REG_DEBUG_BITS]    ip2cpu_debug_reg,
    output reg [`REG_DEBUG_BITS]    cpu2ip_debug_reg,
    input      [`REG_PKTIN_BITS]    pktin_reg,
    output reg                          pktin_reg_clear,
    input      [`REG_PKTOUT_BITS]    pktout_reg,
    output reg                          pktout_reg_clear,
    input      [`REG_ETHERTYPE_BITS]    ip2cpu_ethertype_reg,
    output reg [`REG_ETHERTYPE_BITS]    cpu2ip_ethertype_reg,
    input      [`REG_TCI_BITS]    ip2cpu_tci_reg,
    output reg [`REG_TCI_BITS]    cpu2ip_tci_reg,
    input      [`REG_SLEN_BITS]    ip2cpu_slen_reg,
    output reg [`REG_SLEN_BITS]    cpu2ip_slen_reg,
    input      [`REG_PNUM_BITS]    ip2cpu_pnum_reg,
    output reg [`REG_PNUM_BITS]    cpu2ip_pnum_reg,
    input      [`REG_ICV_BITS]    ip2cpu_icv_reg,
    output reg [`REG_ICV_BITS]    cpu2ip_icv_reg,
    input      [`REG_MACSEC_PKTS_BITS]    ip2cpu_macsec_pkts_reg,
    output reg [`REG_MACSEC_PKTS_BITS]    cpu2ip_macsec_pkts_reg,
    input      [`REG_OTHER_PKTS_BITS]    ip2cpu_other_pkts_reg,
    output reg [`REG_OTHER_PKTS_BITS]    cpu2ip_other_pkts_reg,
    output  reg [`MEM_TESTMEM_ADDR_BITS]    testmem_addr,
    output  reg [`MEM_TESTMEM_DATA_BITS]    testmem_data,
    output  reg                         testmem_rd_wrn,
    output  reg                         testmem_cmd_valid,
    input       [`MEM_TESTMEM_DATA_BITS]    testmem_reply,
    input                               testmem_reply_valid,

    // AXI Lite ports
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

    // AXI4LITE signals
    reg [C_S_AXI_ADDR_WIDTH-1 : 0]      axi_awaddr;
    reg                                 axi_awready;
    reg                                 axi_wready;
    reg [1 : 0]                         axi_bresp;
    reg                                 axi_bvalid;
    reg [C_S_AXI_ADDR_WIDTH-1 : 0]      axi_araddr;
    reg                                 axi_arready;
    reg [C_S_AXI_DATA_WIDTH-1 : 0]      axi_rdata;
    reg [1 : 0]                         axi_rresp;
    reg                                 axi_rvalid;

    reg                                 resetn_sync_d;
    wire                                reg_rden;
    wire                                reg_wren;
    reg [C_S_AXI_DATA_WIDTH-1:0]        reg_data_out;
    integer                             byte_index;
    reg                                 pktin_reg_clear_d;
    reg                                 pktout_reg_clear_d;

    // I/O Connections assignments
    assign S_AXI_AWREADY    = axi_awready;
    assign S_AXI_WREADY     = axi_wready;
    assign S_AXI_BRESP      = axi_bresp;
    assign S_AXI_BVALID     = axi_bvalid;
    assign S_AXI_ARREADY    = axi_arready;
    assign S_AXI_RDATA      = axi_rdata;
    assign S_AXI_RRESP      = axi_rresp;
    assign S_AXI_RVALID     = axi_rvalid;


    //Sample reset (not mandatory, but good practice)
    always @ (posedge clk) begin
        if (~resetn) begin
            resetn_sync_d  <=  1'b0;
            resetn_sync    <=  1'b0;
        end
        else begin
            resetn_sync_d  <=  resetn;
            resetn_sync    <=  resetn_sync_d;
        end
    end


    //global registers, sampling
    always @(posedge clk) resetn_soft <= #1 cpu_resetn_soft;

    // Implement axi_awready generation

    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_awready <= 1'b0;
        end
      else
        begin
          if (~axi_awready && S_AXI_AWVALID && S_AXI_WVALID)
            begin
              // slave is ready to accept write address when
              // there is a valid write address and write data
              // on the write address and data bus. This design
              // expects no outstanding transactions.
              axi_awready <= 1'b1;
            end
          else
            begin
              axi_awready <= 1'b0;
            end
        end
    end

    // Implement axi_awaddr latching

    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_awaddr <= 0;
        end
      else
        begin
          if (~axi_awready && S_AXI_AWVALID && S_AXI_WVALID)
            begin
              // Write Address latching
              axi_awaddr <= S_AXI_AWADDR ^ C_BASE_ADDRESS;
            end
        end
    end

    // Implement axi_wready generation

    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_wready <= 1'b0;
        end
      else
        begin
          if (~axi_wready && S_AXI_WVALID && S_AXI_AWVALID)
            begin
              // slave is ready to accept write data when
              // there is a valid write address and write data
              // on the write address and data bus. This design
              // expects no outstanding transactions.
              axi_wready <= 1'b1;
            end
          else
            begin
              axi_wready <= 1'b0;
            end
        end
    end

    // Implement write response logic generation

    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_bvalid  <= 0;
          axi_bresp   <= 2'b0;
        end
      else
        begin
          if (axi_awready && S_AXI_AWVALID && ~axi_bvalid && axi_wready && S_AXI_WVALID)
            begin
              // indicates a valid write response is available
              axi_bvalid <= 1'b1;
              axi_bresp  <= 2'b0; // OKAY response
            end                   // work error responses in future
          else
            begin
              if (S_AXI_BREADY && axi_bvalid)
                //check if bready is asserted while bvalid is high)
                //(there is a possibility that bready is always asserted high)
                begin
                  axi_bvalid <= 1'b0;
                end
            end
        end
    end

    // Implement axi_arready generation

    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_arready <= 1'b0;
          axi_araddr  <= 32'b0;
        end
      else
        begin
          if (~axi_arready && S_AXI_ARVALID)
            begin
              // indicates that the slave has acceped the valid read address
              // Read address latching
              axi_arready <= 1'b1;
              axi_araddr  <= S_AXI_ARADDR ^ C_BASE_ADDRESS;
            end
          else
            begin
              axi_arready <= 1'b0;
            end
        end
    end


    // Implement axi_rvalid generation

    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_rvalid <= 0;
          axi_rresp  <= 0;
        end
      else
        begin
          if (axi_arready && S_AXI_ARVALID && ~axi_rvalid)
            begin
              // Valid read data is available at the read data bus
              axi_rvalid <= 1'b1;
              axi_rresp  <= 2'b0; // OKAY response
            end
          else if (axi_rvalid && S_AXI_RREADY)
            begin
              // Read data is accepted by the master
              axi_rvalid <= 1'b0;
            end
        end
    end


    // Implement memory mapped register select and write logic generation

    assign reg_wren = axi_wready && S_AXI_WVALID && axi_awready && S_AXI_AWVALID;

//////////////////////////////////////////////////////////////
// write registers
//////////////////////////////////////////////////////////////


//Write only register, clear on write (i.e. event)
    always @(posedge clk) begin
        if (!resetn_sync) begin
            reset_reg <= #1 `REG_RESET_DEFAULT;
        end
        else begin
            if (reg_wren) begin
                case (axi_awaddr)
                    //Reset Register
                        `REG_RESET_ADDR : begin
                                for ( byte_index = 0; byte_index <= (`REG_RESET_WIDTH/8-1); byte_index = byte_index +1)
                                    if (S_AXI_WSTRB[byte_index] == 1) begin
                                        reset_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8];
                                    end
                        end
                endcase
            end
            else begin
                reset_reg <= #1 `REG_RESET_DEFAULT;
            end
        end
    end

//R/W register, not cleared
    always @(posedge clk) begin
        if (!resetn_sync) begin

            cpu2ip_flip_reg <= #1 `REG_FLIP_DEFAULT;
            cpu2ip_debug_reg <= #1 `REG_DEBUG_DEFAULT;
            cpu2ip_ethertype_reg <= #1 `REG_ETHERTYPE_DEFAULT;
            cpu2ip_tci_reg <= #1 `REG_TCI_DEFAULT;
            cpu2ip_slen_reg <= #1 `REG_SLEN_DEFAULT;
            cpu2ip_pnum_reg <= #1 `REG_PNUM_DEFAULT;
            cpu2ip_icv_reg <= #1 `REG_ICV_DEFAULT;
            cpu2ip_macsec_pkts_reg <= #1 `REG_MACSEC_PKTS_DEFAULT;
            cpu2ip_other_pkts_reg <= #1 `REG_OTHER_PKTS_DEFAULT;
        end
        else begin
           if (reg_wren) //write event
            case (axi_awaddr)
            //Flip Register
                `REG_FLIP_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_FLIP_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_flip_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Debug Register
                `REG_DEBUG_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_DEBUG_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_debug_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Ethertype Register
                `REG_ETHERTYPE_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_ETHERTYPE_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_ethertype_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Tci Register
                `REG_TCI_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_TCI_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_tci_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Slen Register
                `REG_SLEN_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_SLEN_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_slen_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Pnum Register
                `REG_PNUM_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_PNUM_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_pnum_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Icv Register
                `REG_ICV_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_ICV_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_icv_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Macsec_pkts Register
                `REG_MACSEC_PKTS_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_MACSEC_PKTS_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_macsec_pkts_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
            //Other_pkts Register
                `REG_OTHER_PKTS_ADDR : begin
                    for ( byte_index = 0; byte_index <= (`REG_OTHER_PKTS_WIDTH/8-1); byte_index = byte_index +1)
                        if (S_AXI_WSTRB[byte_index] == 1) begin
                            cpu2ip_other_pkts_reg[byte_index*8 +: 8] <=  S_AXI_WDATA[byte_index*8 +: 8]; //dynamic register;
                        end
                end
                default: begin
                end

            endcase
        end
  end



/////////////////////////
//// end of write
/////////////////////////

    // Implement memory mapped register select and read logic generation
    // Slave register read enable is asserted when valid address is available
    // and the slave is ready to accept the read address.

    // reg_rden control logic
    // temperary no extra logic here
    assign reg_rden = axi_arready & S_AXI_ARVALID & ~axi_rvalid;

    always @(*)
    begin

        case ( axi_araddr /*S_AXI_ARADDR ^ C_BASE_ADDRESS*/)
            //Id Register
            `REG_ID_ADDR : begin
                reg_data_out [`REG_ID_BITS] =  id_reg;
            end
            //Version Register
            `REG_VERSION_ADDR : begin
                reg_data_out [`REG_VERSION_BITS] =  version_reg;
            end
            //Flip Register
            `REG_FLIP_ADDR : begin
                reg_data_out [`REG_FLIP_BITS] =  ip2cpu_flip_reg;
            end
            //Debug Register
            `REG_DEBUG_ADDR : begin
                reg_data_out [`REG_DEBUG_BITS] =  ip2cpu_debug_reg;
            end
            //Pktin Register
            `REG_PKTIN_ADDR : begin
                reg_data_out [`REG_PKTIN_BITS] =  pktin_reg;
            end
            //Pktout Register
            `REG_PKTOUT_ADDR : begin
                reg_data_out [`REG_PKTOUT_BITS] =  pktout_reg;
            end
            //Ethertype Register
            `REG_ETHERTYPE_ADDR : begin
                reg_data_out [`REG_ETHERTYPE_BITS] =  ip2cpu_ethertype_reg;
                reg_data_out [31:`REG_ETHERTYPE_WIDTH] =  'b0;
            end
            //Tci Register
            `REG_TCI_ADDR : begin
                reg_data_out [`REG_TCI_BITS] =  ip2cpu_tci_reg;
                reg_data_out [31:`REG_TCI_WIDTH] =  'b0;
            end
            //Slen Register
            `REG_SLEN_ADDR : begin
                reg_data_out [`REG_SLEN_BITS] =  ip2cpu_slen_reg;
                reg_data_out [31:`REG_SLEN_WIDTH] =  'b0;
            end
            //Pnum Register
            `REG_PNUM_ADDR : begin
                reg_data_out [`REG_PNUM_BITS] =  ip2cpu_pnum_reg;
            end
            //Icv Register
            `REG_ICV_ADDR : begin
                reg_data_out [`REG_ICV_BITS] =  ip2cpu_icv_reg;
            end
            //Macsec_pkts Register
            `REG_MACSEC_PKTS_ADDR : begin
                reg_data_out [`REG_MACSEC_PKTS_BITS] =  ip2cpu_macsec_pkts_reg;
            end
            //Other_pkts Register
            `REG_OTHER_PKTS_ADDR : begin
                reg_data_out [`REG_OTHER_PKTS_BITS] =  ip2cpu_other_pkts_reg;
            end
            //Default return value
            default: begin
                reg_data_out [31:0] =  32'hDEADBEEF;
            end

        endcase

    end//end of assigning data to IP2Bus_Data bus

    //Read only registers, not cleared
    //Nothing to do here....

//Read only registers, cleared on read (e.g. counters)
    always @(posedge clk)
    if (!resetn_sync) begin
        pktin_reg_clear <= #1 1'b0;
        pktin_reg_clear_d <= #1 1'b0;
        pktout_reg_clear <= #1 1'b0;
        pktout_reg_clear_d <= #1 1'b0;
    end
    else begin
        pktin_reg_clear <= #1 pktin_reg_clear_d;
        pktin_reg_clear_d <= #1(reg_rden && (axi_araddr==`REG_PKTIN_ADDR)) ? 1'b1 : 1'b0;
        pktout_reg_clear <= #1 pktout_reg_clear_d;
        pktout_reg_clear_d <= #1(reg_rden && (axi_araddr==`REG_PKTOUT_ADDR)) ? 1'b1 : 1'b0;
    end


// Output register or memory read data
    always @( posedge S_AXI_ACLK )
    begin
      if ( S_AXI_ARESETN == 1'b0 )
        begin
          axi_rdata  <= 0;
        end
      else
        begin
          // When there is a valid read address (S_AXI_ARVALID) with
          // acceptance of read address by the slave (axi_arready),
          // output the read dada
          if (reg_rden)
            begin
              axi_rdata <= reg_data_out/*ip2bus_data*/;     // register read data /* some new changes here */
            end
        end
    end

    //////////////////////////////////
    // Implement Indirect Access
	//////////////////////////////////
	

  //--------------------- Internal Parameters-------------------------
   localparam NUM_INDIRECT_STATES                = 6;
   localparam IDLE_INDIRECT_STATE                = 1;
   localparam WRITE_INDIRECT_STATE               = 2;
   localparam WRITE_WAIT_INDIRECT_STATE          = 4;
   localparam READ_INDIRECT_STATE                = 8;
   localparam READ_WAIT_INDIRECT_STATE           = 16;
   localparam INDIRECT_DONE_STATE                = 32;
   localparam INDIRECT_WRITE                     = 0;
   localparam INDIRECT_READ                      = 1;
   localparam INDIRECT_WRITE_TA                  = 1;
   localparam INDIRECT_WRITE_WS                  = 0;
  //------------------------------------------------------------------
   
   reg  [NUM_INDIRECT_STATES-1:0]           indirect_state, indirect_state_next, indirect_state_last;
   wire                            indirect_trigger;
   wire                            indirect_type;
   reg                             indirect_status, indirect_status_next;
   wire [3:0]                      indirect_address_increment;
   wire                            indirect_write_type;
   wire [10:0]                     indirect_timeout;
   wire [15:0]                     indirect_repeat_count;
   reg  [15:0]                     indirect_remaining,indirect_remaining_next;
   reg  [10:0]                     indirect_timeout_count, indirect_timeout_count_next;
   reg                             indirect_reply_valid;
   reg  [31:0]                     indirect_address,indirect_address_next;
   reg  [3:0]                      indirect_memory_select,indirect_memory_select_next;
   wire                             indirect_command_done;
   
   assign   indirect_trigger = indirectcommand_reg[0];
   assign   indirect_type    = indirectcommand_reg[4];
   assign   indirect_address_increment = indirectconfig_reg[3:0];
   assign   indirect_write_type = indirectconfig_reg[4];
   assign   indirect_timeout    = indirectconfig_reg[15:5];
   assign   indirect_repeat_count = indirectconfig_reg[31:16];
   
 always @(*) begin
      indirect_state_next   = indirect_state;
      indirect_status_next  = indirect_status;
      indirect_remaining_next = indirect_remaining;
      indirect_timeout_count_next = indirect_timeout_count;
      indirect_address_next      = indirect_address;
      indirect_memory_select_next = indirect_memory_select;
      case(indirect_state)
        IDLE_INDIRECT_STATE: begin
     	   if(indirect_trigger) begin
     	      indirect_state_next= (indirect_type == INDIRECT_WRITE) ? WRITE_INDIRECT_STATE : READ_INDIRECT_STATE;
     	      indirect_remaining_next = (indirect_repeat_count == 0) ? 16'h1 : indirect_repeat_count;
     	      indirect_timeout_count_next   = indirect_timeout;
     	      indirect_address_next   =  indirectaddress_reg; //This is the address in the user register
     	      indirect_memory_select_next = indirectaddress_reg[31:28];
     	   end
	    end
	    
	    READ_INDIRECT_STATE: begin
		     indirect_state_next = READ_WAIT_INDIRECT_STATE;
	    end
	    READ_WAIT_INDIRECT_STATE: begin
	         if (indirect_reply_valid) begin
	            indirect_state_next = INDIRECT_DONE_STATE;
	            indirect_status_next =0;
	         end
	         if (indirect_timeout_count==0) begin
	            indirect_state_next = INDIRECT_DONE_STATE;
	            indirect_status_next = 1; 
	         end
	         indirect_timeout_count_next = indirect_timeout_count-1;
	     end
	     WRITE_INDIRECT_STATE: begin
	         indirect_state_next = WRITE_WAIT_INDIRECT_STATE;
	     end
	     WRITE_WAIT_INDIRECT_STATE:  begin
	         if (((indirect_write_type == INDIRECT_WRITE_TA) && (indirect_reply_valid)) || ((indirect_write_type == INDIRECT_WRITE_WS) && (indirect_timeout_count==0))) begin
	           indirect_remaining_next = indirect_remaining - 1;
	           indirect_address_next = indirect_address+indirect_address_increment;
	           if (indirect_remaining==1) begin
	              indirect_state_next = INDIRECT_DONE_STATE;
	           end
	         end
	         else 
	           if (indirect_timeout_count==0) begin
	         	indirect_state_next = INDIRECT_DONE_STATE;
	         	indirect_status_next = 1; 
	         end
             indirect_timeout_count_next = indirect_timeout_count==0 ? 0 : indirect_timeout_count-1;
	     end
	     INDIRECT_DONE_STATE: begin
	        indirect_state_next= IDLE_INDIRECT_STATE;
	     end
	     default: begin
	         indirect_state_next= IDLE_INDIRECT_STATE;
	     end
      endcase // case(state)
   end // always @ (*)
   
    assign indirect_command_done = (indirect_state==INDIRECT_DONE_STATE);
   
   always @(posedge clk) begin
      if(~resetn_sync) begin
         indirect_state <= #1 IDLE_INDIRECT_STATE;
         indirect_state_last <= #1 IDLE_INDIRECT_STATE;
         indirect_status <= #1 1'b0;
         indirect_remaining <= #1 0;
         indirect_timeout_count <= #1 0;
         indirect_address   <= #1 0;
         indirect_memory_select <= #1 0;
         indirectcommand_reg <= #1 `REG_INDIRECTCOMMAND_DEFAULT;
      end
      else begin
         indirect_state <= #1 indirect_state_next;
         indirect_state_last <= #1 indirect_state;
         indirect_status <= #1 indirect_status_next;
         indirect_remaining <= #1 indirect_remaining_next;
         indirect_timeout_count <= #1 indirect_timeout_count_next;
         indirect_address   <= #1  indirect_address_next;
         indirect_memory_select <= #1 indirect_memory_select_next;
         indirectcommand_reg <= #1  indirect_command_done ? {indirect_status,indirectcommand_reg[7:4],4'h0} : 
                                    indirectcommand_reg_update ? indirectcommand_reg_internal: 
                                    indirectcommand_reg;
      end
   end   
   

       
       always @(posedge clk) begin
         if  (~resetn_sync) begin
           testmem_addr <= #1 0;
           testmem_data <= #1 0;
           testmem_rd_wrn<= #1 0;
           testmem_cmd_valid <= #1 0;
         end 
         else begin
           testmem_addr <= #1 indirect_address;
           testmem_data <= #1 indirectwrdata_reg;
           testmem_rd_wrn<= #1 indirect_type;
           testmem_cmd_valid <= #1 (32'h0==(indirect_memory_select<<28)) && ((indirect_state == WRITE_INDIRECT_STATE) || (indirect_state == READ_INDIRECT_STATE));
         end 
       end

       always @(posedge clk) begin
          if  (~resetn_sync) begin
             indirectreply_reg <= #1 0;
             indirect_reply_valid <= #1 0; 
          end 
          else begin 
             indirectreply_reg <= #1 32'h0==(indirect_memory_select<<28) ? testmem_reply : 0;
      indirect_reply_valid <= #1 32'h0==(indirect_memory_select<<28) ? testmem_reply_valid : 0;
          end 
        end
  
endmodule
