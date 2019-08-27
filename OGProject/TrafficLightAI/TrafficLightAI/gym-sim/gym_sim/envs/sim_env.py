import gym
from gym import error, spaces, utils
from gym.utils import seeding
from pyglet import *
from pyglet.window import key
import random
from Classes.Car import *
from Classes.StopLight import *

class SimEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        resource.path = ['Images']
        resource.reindex()
        self.netIdle = 0
        self.collisions = 0
        self.newWindow = window.Window(width=1536, height=864, caption='Traffic Light SIM')
        #window.set_fullscreen(True)
        @self.newWindow.event
        def on_draw():
            self.newWindow.clear()
            roadSprite.draw()
            self.batch.draw()
        self.newWindow.on_draw = on_draw
        self.batch = graphics.Batch()
        roadSprite = sprite.Sprite(img=resource.image("road.png"),x=0,y=0)

        self.carSprites = [sprite.Sprite(img=resource.image("car.png"), batch=self.batch) for i in range(6)]
        self.cars = [Car(random.randint(0,3), self.carSprites[j]) for j in range(6)]

        self.stopLightSprites = [sprite.Sprite(img=resource.image("stoplight_red.png"), batch=self.batch) for i in range(12)]
        self.stopLights = [[],[],[],[]]
        sprIndex = 0
        for interNum in range(3):
            for traFlow in range(4):
                self.stopLights[traFlow].append(StopLight(interNum,traFlow,0, self.stopLightSprites[sprIndex]))
                sprIndex+=1

        self.rankings = [1,1,1,1,1,1,1,1,1,1,1,1]
        self.observation_space = [[[self.stopLights, self.cars,self.netIdle]],[],[]]

    def reset(self):
        pass
    #def getPolicy(self, states, actions, rewards):
    def getPolicy(self):
        if (sum(self.rankings) == 12):
            action = random.randint(0,11)
        else:
            if(self.observation_space[2][len(self.observation_space[2])-1] == 1):
                action = self.observation_space[1][len(self.observation_space[1])-1]
            else:
           
                action = self.rankings.index(max(self.rankings))
        return action

    def step(self, dt):
        action = (self.getPolicy())
        if action == 0:
            self.changeLights(0, 0)
        if action == 1:
            self.changeLights(0, 1)
        if action == 2:
            self.changeLights(0, 2)
        if action == 3:
            self.changeLights(0, 3)
        if action == 4:
            self.changeLights(1, 0)
        if action == 5:
            self.changeLights(1, 1)
        if action == 6:
            self.changeLights(1, 2)
        if action == 7:
            self.changeLights(1, 3)
        if action == 8:
            self.changeLights(2, 0)
        if action == 9:
            self.changeLights(2, 1)
        if action == 10:
            self.changeLights(2, 2)
        if action == 11:
            self.changeLights(2, 3)
        if self.observation_space[0][(len(self.observation_space[0])-1)][2] >= self.netIdle:
            if self.collisions > 0:
                reward = 0
                self.rankings[action] = self.rankings[action]-(0.1 + self.collisions)
            else:
                reward = 1
                self.rankings[action] = self.rankings[action]+0.1
        elif self.observation_space[0][(len(self.observation_space[0])-1)][2] <= self.netIdle:
            if self.collisions > 0:
                reward = 0
                self.rankings[action] = self.rankings[action]-(0.1 + self.collisions)
            else:
                reward = 0
                self.rankings[action] = self.rankings[action-1]-0.1
        state = [self.stopLights, self.cars,self.netIdle]
        self.observation_space[0].append(state)
        self.observation_space[1].append(action)
        self.observation_space[2].append(reward)
        self.collisions = 0

    def render(self, mode='human'):
        def update(dt, lights=None, allCars=None):
            if lights == None:
                lights = self.stopLights
            if allCars == None:
                allCars = self.cars
            self.netIdle = 0
            for car in allCars:
                car.update(dt, lights, allCars)
                if (car.sprite.x > 1590 or car.sprite.x < -50
                    or car.sprite.y < -1 or car.sprite.y > 900):
                    car.sprite.delete()
                    allCars.remove(car)
                self.netIdle += car.idle
            for grouping in self.stopLights:
                for light in grouping:
                    light.sprite.draw()

        def spawnCar(dt):
            self.carSprites.append(sprite.Sprite(img=resource.image("car.png"), batch=self.batch))
            self.cars.append(Car(random.randint(0,3), self.carSprites[(len(self.carSprites)-1)]))
    
        def checkForCollisions(dt):
            for i in range(0,(len(self.cars)-1)):
                for j in range(i+1,(len(self.cars)-1)):
                    if (self.cars[i].sprite.x > 0 and self.cars[j].sprite.x > 0
                        and self.cars[i].sprite.x < 1530 and self.cars[j].sprite.x < 1530
                        and self.cars[i].sprite.y > 0 and self.cars[j].sprite.y > 0
                        and self.cars[i].sprite.y < 860 and self.cars[j].sprite.y < 860):
                        if self.cars[i].collide(self.cars[j]) == True:
                            self.collisions+=1

        clock.schedule_interval(update, 1/120)
        clock.schedule_interval(spawnCar, 4)
        clock.schedule_interval(self.step, 4)
        clock.schedule_interval(checkForCollisions, 1)
        clock.schedule_interval(self.changeYellows,5)
        app.run()
       
    def changeLights(self, intersectionNum, direction):
        lightImg=["stoplight_red.png","stoplight_yellow.png","stoplight_green.png"]
        if self.stopLights[direction][intersectionNum].currState == 2:
            self.stopLights[direction][intersectionNum].currState = 1
        elif self.stopLights[direction][intersectionNum].currState == 0:
            self.stopLights[direction][intersectionNum].currState = 2
        self.stopLights[direction][intersectionNum].sprite.image = resource.image(lightImg[self.stopLights[direction][intersectionNum].currState])
        #print(str(intersectionNum) + " - - " + str(direction) + " - - " + str(lightImg[self.stopLights[direction][intersectionNum].currState]))

    def changeYellows(self,dt):
        for grouping in self.stopLights:
            for light in grouping:
                if light.currState == 1:
                    light.currState = 0
                    light.sprite.image = resource.image("stoplight_red.png")

    def close(self):
        #probably dont need this
        self.newWindow.close()
