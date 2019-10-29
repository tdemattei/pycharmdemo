# Learn code in read_write.py


import os  # import built in os module

os_info = os.name  # Set os_info = to os.name
print(os_info)  # Print os_info

if os.name == 'nt':  # Test if os is equal to nt
    print("True")  # If os is equal to nt print True
    import msvcrt
    print("Imported msvcrt ")

from inputs import get_gamepad  # import get_gamepad from inputs module to read gamepad
print("Imported Game Pad")

import dynamixel_sdk as dxl  # import and name dynamixel_sdk to dxl
print("Imported dynamixel SDK")


def main(): # define function to read gamepad imput and convert to servo motion comands

    in_min = int(3000)  # minimum value of gamepad joystick input (set a dead zone)
    in_max = int(32768)  # Maximum value of gamepad joystick input
    out_min = int(0)  # Minimum value to map gamepad input to
    out_max = 600      # Maximum value to map gamepad input to
    velocity = 0   # variable for velocity of dymamixel servo
    write_velocity = 0  # variable for velocity to write to dynamixel servo

    while 1:
        # dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID,
        #                                                                                ADDR_PRO_PRESENT_POSITION)
        # if dxl_comm_result != dxl.COMM_SUCCESS:
        #     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        # elif dxl_error != 0:
        #     print("%s" % packetHandler.getRxPacketError(dxl_error))
        #
        # print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, DXL_MAXIMUM_POSITION_VALUE, dxl_present_position))

        events = get_gamepad()
        for event in events:  # read input from game pad
            if event.code == "BTN_START" and event.state == 1:  # Exit loop if start button is pressed
                print("Start Button Pressed")
                return

            # read input if right joystick is moved in "X" plane and scale for dynamexil velocity
            if event.code == "ABS_RX" and abs(event.state) > in_min and abs(event.state) <= in_max:
                velocity = round((abs(event.state) - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

                if event.state < 0:
                    velocity = velocity * -1

            elif event.code == "ABS_RX":
                velocity = 0


# Write velocity to dynamixel servo only if velocity changes.
            elif write_velocity == velocity:
                continue

            elif write_velocity != velocity:
                write_velocity = velocity
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_PRO_GOAL_VELOCITY, write_velocity)
                if dxl_comm_result != dxl.COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Check position of servo
           # while write_velocity == velocity:
                # Read present position



# Control table address
ADDR_PRO_TORQUE_ENABLE      = 512               # Control table address is different in Dynamixel model
ADDR_PRO_GOAL_POSITION      = 564
ADDR_PRO_PRESENT_POSITION   = 580
ADDR_PRO_GOAL_VELOCITY      = 552

# Protocol version
PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = 1                 # Dynamixel ID : 1
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = 'COM3'    # Check which port is being used on your controller
                                        # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = 10           # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 4000            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold


index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = dxl.PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = dxl.PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != dxl.COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")


while 1:
    print("Type any key to continue or ESC to exit:")
    char = msvcrt.getch().decode()
    if char == chr(27):
        break
    main()


# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != dxl.COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()

print("Port Closed")

quit()