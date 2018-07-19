#!/bin/bash -f
xv_path="/opt/Xilinx/Vivado/2016.4"
ExecStep()
{
"$@"
RETVAL=$?
if [ $RETVAL -ne 0 ]
then
exit $RETVAL
fi
}
ExecStep $xv_path/bin/xelab -wto 4c14ac6607c541f79bcad01913f2fdd2 -m64 --debug typical --relax --mt 8 -d "SIMULATION=1" -L xil_defaultlib -L blk_mem_gen_v8_3_5 -L lib_pkg_v1_0_2 -L lib_srl_fifo_v1_0_2 -L generic_baseblocks_v2_1_0 -L axi_infrastructure_v1_1_0 -L axi_register_slice_v2_1_11 -L fifo_generator_v13_1_3 -L axi_data_fifo_v2_1_10 -L axi_crossbar_v2_1_12 -L axi_clock_converter_v2_1_10 -L axi_protocol_converter_v2_1_11 -L axi_mmu_v2_1_9 -L unisims_ver -L unimacro_ver -L secureip -L xpm --snapshot top_tb_behav xil_defaultlib.top_tb xil_defaultlib.glbl -log elaborate.log
