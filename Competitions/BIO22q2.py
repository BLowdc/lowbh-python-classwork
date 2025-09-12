hive = [['X' for i in range(6)] for j in range(25)]
r, b = [int(s) for s in input("Enter num of jumps: ").split()]
s, f = [int(s) for s in input("Enter num of skirmishes and feuds: ").split()]

r_hex, r_edge = 0, 0
b_hex, b_edge = 24, 5

r_control, b_control = 0, 0

hive[r_hex][r_edge] = "RED"
hive[b_hex][b_edge] = "BLUE"

for i in range(s-1):
    r_hex = (r_hex + r) % 25
    r_edge = (r_edge + 1) % 6
    b_hex = (b_hex + b) % 25
    b_edge = (b_edge - 1) % 6

    hive[r_hex][r_edge] = "RED"
    hive[b_hex][b_edge] = "BLUE"
#next i

for hex in hive:
    r_count, b_count = 0, 0
    for edge in hex:
        if edge == "RED":
            r_count += 1
        elif edge == "BLUE":
            b_count += 1
        #end if
    #next edge
    if r_count > b_count:
        r_control += 1
    elif b_count > r_count:
        b_control += 1
    #end if
#next hex