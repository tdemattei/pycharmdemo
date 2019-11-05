"""Simple example showing how to get gamepad events."""

# from __future__ import print_function


from inputs import get_gamepad


# def main():
#     """Just print out some event infomation when the gamepad is used."""
in_min = int(3000)
in_max = int(32768)
out_min = int(0)
out_max = (600)




def gp_input():


    velocity = None
    # while 1:
    events = get_gamepad()
    if events:
        print("if events")
        for event in events:
            if event.code == "BTN_START" and event.state == 1:
                print("Start Button Pressed")
                return

            elif event.code != "ABS_RX":
                print("this is break")
                break
            elif event.code == "ABS_RX" and abs(event.state) > in_min and abs(event.state) <= in_max:
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
            return (velocity)
        print("All Return Here")
    else:
        print("this is no event")

    print("While 1")
    print("While 2")
    print("While 3")
    print(gp_input())

while 1:

    gp_input()

print(gp_input())
# print(velocity)
print("bye")
