def lcm(a, b, c):
    #find biggest value
    biggest = 0
    if a > b and a > c:
        biggest = a
    elif b > a and b > c:
        biggest = b
    elif c > a and c > a:
        biggest = c

    while(True):
        if (biggest % a == 0) and (biggest % b == 0) and (biggest % c == 0): #if biggest is divisible by all three of them
            lcm = biggest
            break #stop the while loop
        biggest += 1 #add 1 to biggest, and check if divisible again
    return biggest

print(lcm(18, 4, 7))