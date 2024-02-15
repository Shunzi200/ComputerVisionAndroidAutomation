
import sys
import os

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input(print("Press key to exit."))
    sys.exit(-1)

clear = lambda: os.system('cls')
