from inputs import get_gamepad

while 1:
    in_min = int(3000)
    in_max = int(32768)
    out_min = int(0)
    out_max = (600)
    velocity = 0
    print("this is loop 1")
    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_START" and event.state == 1:
                print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                print("Button Press")
                print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                # break
            if event.code == "ABS_RX" and abs(event.state) > in_min and abs(event.state) <= in_max:
                velocity = round((abs(event.state) - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
                print("+++++++++++++++++++++++++++++++++++++")
                print("Velocity Positive " + str(velocity))
                print("++++++++++++++++++++++++++++++++++++++")
                # print(velocity)
                if event.state < 0:
                    velocity = velocity * -1
                    print("-----------------------------------")
                    print("Velocity Negative " + str(velocity))
                    print("------------------------------------")
                    # print(event.ev_type, event.code, event.state)
                    # print(velocity)
            elif event.code == "ABS_RX":
                velocity = 0
                print("000000000000000000000000000000000000000")
                print("Velocity Zero " + str(velocity))
                print("000000000000000000000000000000000000000")
                # print(event.ev_type, event.code, event.state)
                # print(velocity)
            print("=====================================")
            print(event.ev_type, event.code, event.state)
            print("this is loop 2")
            print("Velocity = " + str(velocity))
            print("======================================")
