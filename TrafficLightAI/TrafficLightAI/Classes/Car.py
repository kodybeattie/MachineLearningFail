from pyglet import *
from Classes.Road import *
import random, math
class Car(sprite.Sprite):
    """
    This is a class used to represent a car.

    Light States
    ============
    0 = Red
    1 = Yellow
    2 = Green

    """
    resource.path = ['Images']
    resource.reindex()
    def __init__(self):
        pass

    def __init__(self, dir, spr):
        self.direction = dir
        self.sprite = spr
        self.sprite.scale = 0.5
        self.idle = 0
        self.road = Road
        self.speed = 30
        # right
        if self.direction == 0:
            self.sprite.x = -10
            self.sprite.y = 518
        # left
        elif self.direction == 1:
            self.sprite.x = 1538
            self.sprite.y = 547
        # up
        elif self.direction == 2:
            upX = [125, 706, 1436]
            self.sprite.x = random.choice(upX)
            self.sprite.y = 0
            self.sprite.rotation = 90
        # down 
        elif self.direction == 3:
            downX = [99, 675, 1406]
            self.sprite.x = random.choice(downX)
            self.sprite.y = 864
            self.sprite.rotation = 90

    # sprite animation
    def update(self, dt, stopLights, cars):
        # right
        if self.direction == 0:
            redLights = []
            for light in stopLights[0]:
                if light.currState == 0:
                    redLights.append(stopLights[0].index(light))
            if int(self.sprite.x) in self.road.rightHoriStopPoints:
                if int(self.road.rightHoriStopPoints.index(int(self.sprite.x)) in redLights):
                    self.sprite.x += 0
                    self.idle += dt
                else:
                    self.sprite.x += dt * self.speed
                    self.idle -= dt
            else:
                self.checkFront(dt, cars)
        # left
        if self.direction == 1:
            redLights = []
            for light in stopLights[1]:
                if light.currState == 0:
                    redLights.append(stopLights[1].index(light))
            if int(self.sprite.x) in self.road.leftHoriStopPoints:
                if int(self.road.leftHoriStopPoints.index(int(self.sprite.x)) in redLights):
                    self.sprite.x -= 0
                    self.idle += dt
                else:
                    self.sprite.x -= dt * self.speed
                    self.idle -= dt
            else:
                self.checkFront(dt, cars)
        # up
        if self.direction == 2:
            redLights = []
            for light in stopLights[2]:
                if light.currState == 0:
                    redLights.append(stopLights[2].index(light))
            if int(self.sprite.y) in self.road.upVertStopPoints:
                if (self.road.rightHoriStopPoints[0] < int(self.sprite.x) 
                    and int(self.sprite.x) < self.road.leftHoriStopPoints[0]
                    and 0 in redLights):
                    self.sprite.y += 0
                    self.idle += dt
                else:
                    if (self.road.rightHoriStopPoints[1] < int(self.sprite.x)  
                        and int(self.sprite.x)  < self.road.leftHoriStopPoints[1]
                        and 1 in redLights):
                        self.sprite.y += 0
                        self.idle += dt
                    else:
                        if (self.road.rightHoriStopPoints[2] < int(self.sprite.x) 
                            and int(self.sprite.x)  < self.road.leftHoriStopPoints[2]
                            and 2 in redLights):
                            self.sprite.y += 0
                            self.idle += dt
                        else:
                            self.sprite.y += dt * self.speed
                            self.idle -= dt
            else:
                self.checkFront(dt, cars)

        # down
        if self.direction == 3:
            redLights = []
            for light in stopLights[3]:
                if light.currState == 0:
                    redLights.append(stopLights[3].index(light))
            if int(self.sprite.y) in self.road.downVertStopPoints:
                if (self.road.rightHoriStopPoints[0] < int(self.sprite.x) 
                    and int(self.sprite.x) < self.road.leftHoriStopPoints[0]
                    and 0 in redLights):
                    self.sprite.y -= 0
                    self.idle += dt
                else:
                    if (self.road.rightHoriStopPoints[1] < int(self.sprite.x)  
                        and int(self.sprite.x)  < self.road.leftHoriStopPoints[1]
                        and 1 in redLights):
                        self.sprite.y -= 0
                        self.idle += dt
                    else:
                        if (self.road.rightHoriStopPoints[2] < int(self.sprite.x) 
                            and int(self.sprite.x)  < self.road.leftHoriStopPoints[2]
                            and 2 in redLights):
                            self.sprite.y -= 0
                            self.idle += dt
                        else:
                            self.sprite.y -= dt * self.speed
                            self.idle -= dt
            else:
                self.checkFront(dt, cars)

    def checkFront(self, dt, cars):
        inFront = False
        if self.direction == 0:
            for car in cars:
                if (cars.index(car) != cars.index(self)
                    and cars.index(car) < cars.index(self)
                    and self.sprite.y == car.sprite.y
                        and self.distance((car.sprite.position[0],car.sprite.position[1]), car.sprite.height, car.sprite.width) <= 30):
                            inFront = True
            if inFront == True:
                self.sprite.x += 0
                self.idle += dt
            else:
                self.sprite.x += dt * self.speed
                self.idle -= dt
        if self.direction == 1:
            for car in cars:
                if (cars.index(car) != cars.index(self)
                    and cars.index(car) < cars.index(self)
                    and self.sprite.y == car.sprite.y
                        and self.distance((car.sprite.position[0],car.sprite.position[1]), car.sprite.height, car.sprite.width) <= 30):
                            inFront = True
            if inFront == True:
                self.sprite.x -= 0
                self.idle += dt
            else:
                self.sprite.x -= dt * self.speed
                self.idle -= dt
        if self.direction == 2:
            for car in cars:
                if (cars.index(car) != cars.index(self)
                    and cars.index(car) < cars.index(self)
                    and self.sprite.x == car.sprite.x
                       and self.distance((car.sprite.position[0],car.sprite.position[1]), car.sprite.height, car.sprite.width) <= 30):
                            inFront = True
            if inFront == True:
                self.sprite.y += 0
                self.idle += dt
            else:
                self.sprite.y += dt * self.speed
                self.idle -= dt
        if self.direction == 3:
            for car in cars:
                if (cars.index(car) != cars.index(self)
                    and cars.index(car) < cars.index(self)
                    and self.sprite.x == car.sprite.x
                        and self.distance((car.sprite.position[0],car.sprite.position[1]), car.sprite.height, car.sprite.width) <= 30):
                            inFront = True
            if inFront == True:
                self.sprite.y -= 0
                self.idle += dt
            else:
                self.sprite.y -= dt * self.speed 
                self.idle -= dt
    
    def distance(self, point2=(0, 0), car2Height=0, car2Width=0):
        #print("Car1Pos1: " + str(self.sprite.position[0]) + " Car1Pos2: " + str(self.sprite.position[1]))
        #print("Car2Pos1: " + str(point2[0]) + " Car2Pos2: " + str(point2[1]))
        #print(str(math.sqrt((self.sprite.position[0] - point2[0]) ** 2 + (self.sprite.position[1] - point2[1]) ** 2)))
        return max(abs(self.sprite.position[0] - point2[0]) - (self.sprite.width + car2Width)/2, abs(self.sprite.position[1] - point2[1]) - (self.sprite.height + car2Height)/2)

    def collide(self, car):
        if self.distance((car.sprite.position[0],car.sprite.position[1]), car.sprite.height, car.sprite.width) <= 0:
            return True
        else:
            return False