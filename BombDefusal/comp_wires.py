def complicated_module(wire_num):
    i = 0
    last_digit = input("Is the last digit of the serial number even? ")
    if last_digit.lower() == "yes":
        serial = True
    else:
        serial = False
    parallel = input("Is there a serial port on the bomb? (Very wide port with dots) ")
    if parallel.lower() == "yes":
        port = True
    else:
        port = False
    battery_num = input("Are there more than 2 batteries? ")
    if battery_num.lower() == "yes":
        battery = True
    else:
        battery = False

    while i <= wire_num:
        red = input("\n\nIs some part of the wire red? ")
        if red.lower() == "yes":
            r = True
        else:
            r = False
        blue = input("Is some part of the wire blue? ")
        if blue.lower() == "yes":
            b = True
        else:
            b = False
        led = input("Is the LED above the wire on? ")
        if led.lower() == "yes":
            l = True
        else:
            l = False
        star = input("Is there a star drawn under the wire? ")
        if star.lower() == "yes":
            s = True
        else:
            l = False
        if r:
            if serial:
                print("Cut the wire")
            elif s:
                print("Cut the wire")
            elif l and battery:
                print("Cut the wire")
            elif s and l and battery:
                print("Cut the wire")
            elif b:
                if s and port:
                    print("Cut the wire")
                elif l and serial:
                    print("Cut the wire")
                elif s and l:
                    print("Don't cut the wire")
        elif b:
            if serial:
                print("Cut the wire")
            elif s:
                print("Don't cut")
            elif l and port:
                print("Cut the wire")
            elif s and l and port:
                print("Cut the wire")
            elif r:
                if s and port:
                    print("Cut the wire")
                if l and serial:
                    print("Cut the wire")
                elif s and l:
                    print("Don't cut the wire")
        else:
            if s:
                print("Cut the wire")
            elif l:
                print("Don't cut the wire")
            elif s and l and battery:
                print("Cut the wire")
            else:
                print("Cut the wire")
        i += 1
