from inputs import get_gamepad

def main():
    """Just print out some event infomation when keys are pressed."""
    while 1:
        events = get_gamepad()
        if events:
            for event in events:
                print(event.ev_type, event.code, event.state)
        print("Hello")
        # sleep(0.1)


if __name__ == "__main__":
    main()
