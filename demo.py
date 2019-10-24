

in_val = 25000
in_min = 2500
in_max = 32768
out_min = 0
out_max = 600

if abs(in_val) > in_min and abs(in_val) <= in_max:
    velocity = round((abs(in_val) - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    if in_val < 0:
        velocity = velocity * -1

else:
    velocity = 0


print(velocity)