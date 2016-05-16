import os
import time
class game_life():
    def __init__(self,size):
        loadmap = open("map","r")
        reading = loadmap.readline()
        self.map = []
        self.min_alive = 2
        self.max_alive = 3
        self.min_born = 3
        self.max_born = 3
        self.sleepingtime = 0.1
        while reading:
            self.map.append(reading.split())
            reading = loadmap.readline()
        #self.Are_you_alive()
        print(self.map)
    def Are_you_alive(self):
        while 1:
            for y in range(len(self.map)):
                for x in range(len(self.map[y])):
                    if self.map[y][x] == "1":
                        if not self.crowded(self.min_alive,self.max_alive,x,y):
                            self.map[y][x] = "0"
                    else:
                        if self.crowded(self.min_born,self.max_born,x,y):
                            self.map[y][x] = "1"
            for x in self.map:
                print(*x)
            time.sleep(self.sleepingtime)
            os.system('clear')
    def crowded(self,min,max,x,y):
        count = 0
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if self.map[j][i] == 1:
                    count += 1
        return ((count <= max) and (count >= min))
life = game_life(100)