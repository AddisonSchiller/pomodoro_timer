import sys
from ptimer.console_version import Ptimer


time_settings = [25, 5, 20]
if len(sys.argv) == 4:
    time_settings = map(float, sys.argv[1:])
else:
    if len(sys.argv) != 1:
        print(":::::::::::::::::::::::::::::")
        print("Usage: python console_main.py [round length in minutes] [break length in minutes] [long break length in minutes]")
        print("example: python console_main 20.1 5.2 12")
        print("Inputting no args will use default values")
        print(":::::::::::::::::::::::::::::")
        sys.exit(1)

timer = Ptimer(*time_settings)

timer.start()
