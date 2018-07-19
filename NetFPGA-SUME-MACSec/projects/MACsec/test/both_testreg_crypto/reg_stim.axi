# BARRIER
B 4
# Interface 0
N 0
S 0
# Interface 1
N 0
S 0
# Interface 2
N 0
S 0
# Interface 3
N 0
S 0
# DMA
N 0
S 0
# WRITE
W 00000002
4409001c, ffffffff, f, -.
# READ
R 00000001
-, -, -, 4409001c.
# BARRIER
B 4
# Interface 0
N 0
S 10
# Interface 1
N 10
S 0
# Interface 2
N 10
S 0
# Interface 3
N 10
S 0
# DMA
N 0
S 0
# WRITE
W 00000002
4409001c, f0f0f0f0, f, -.
# READ
R 00000001
-, -, -, 4409001c.
# BARRIER
B 4
# Interface 0
N 0
S 0
# Interface 1
N 0
S 0
# Interface 2
N 0
S 0
# Interface 3
N 0
S 0
# DMA
N 0
S 0
# BARRIER
B 4
# Interface 0
N 10
S 0
# Interface 1
N 0
S 10
# Interface 2
N 0
S 0
# Interface 3
N 0
S 0
# DMA
N 0
S 0
# READ
R 00000001
-, -, -, 4409001c.
# READ
R 00000001
-, -, -, 44020020.
# READ
R 00000001
-, -, -, 4402001c.
# BARRIER
B 4
# Interface 0
N 0
S 0
# Interface 1
N 0
S 0
# Interface 2
N 0
S 0
# Interface 3
N 0
S 0
# DMA
N 0
S 0
