#!/usr/bin/python

# export PYTHONPATH=<libardrone> so Python can find ardrone library
import libardrone
import sys

drone = libardrone.ARDrone()

# Keep running until q or Ctrl+C
print "Receiving commands... ('Quit' to exit)"

try:
    while True:
        command = sys.stdin.readline().strip().lower()

        if command == 'quit':
            break
        elif command == 'takeoff':
            drone.takeoff()
        elif command == 'land':
            drone.land()

        if command:
            print "Command: ", command

        drone.hover

finally:
    print "Bye"
    drone.land()
    drone.halt()
