for i in range(1000, 10000):
    val = i
    hex_val = 0
    while val > 0:
        hex_val += (val % 16)
        val = val // 16

    val = i
    dec_val = 0
    while val > 0:
        dec_val += (val % 10)
        val = val // 10

    val = i
    twel_val = 0
    while val > 0:
        twel_val += (val % 12)
        val = val // 12
    if hex_val == dec_val == twel_val:
        print(i)
