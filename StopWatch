"""
Algorithm:     Create a stop watch program that times how long, in milliseconds, it takes the program to add up
               from 1 to 1,000,000.
"""

import time

class StopWatch():

    def __init__(self):
        self.startTime = 0
        self.endTime = 0

    def start(self):
        self.startTime = time.time()
        return self.startTime

    def end(self):
        self.endTime = time.time()
        return self.endTime

    def getElapsedTime(self):
        return (self.endTime - self.startTime)*1000
        

def main():
    print("This program outputs how long, in milliseconds it takes to add up",\
          "numbers starting at 1 to 1,000,000.")
    print()

    go = StopWatch()
    
    go.start()

    for i in range(1, 1000001):
        i += i

    go.end()
    print("The loop time is", int(go.getElapsedTime()), "milliseconds.")
    

main()
