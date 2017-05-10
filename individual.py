from pyrosim import PYROSIM 
from robot import ROBOT 
import random
import math 
import numpy
import constants as con
import matplotlib.pyplot as plt
from smile_detect import SMILE
 
class INDIVIDUAL: 
    def __init__(self, i): 
 
        self.genome = numpy.random.random((6, 10)) * 2 - 1 
 
        self.fitness = 0

        self.fitnessX = 0

        self.fitnessY = 0

        self.ID = i

        self.wagCount = 0

        self.fitnessLight = 0

        # self.goodPaws = list()

        # self.pawSensors = list()

    def Start_Evaluation(self, paused, blind):

        self.sim = PYROSIM(playPaused=paused,  playBlind=blind, evalTime=con.evaluationTime) 

        robot = ROBOT(self.sim, self.genome) 
 
        self.sim.Start()

        # print 'Current eval ID', self.ID

        # smile_detect = SMILE()

        # smile_detect.Start_Smile_Evaluation(con.evaluationTime)

    def Compute_Fitness(self):

        self.sim.Wait_To_Finish()

        self.Get_Fitness_Data()

        del self.sim

        return self.fitness



    def Mutate(self): 
 
        geneToMutateX = random.randint(0,5) 
 
        geneToMutateY = random.randint(0,9)         
 
        self.genome[geneToMutateX,geneToMutateY] = random.gauss(self.genome[geneToMutateX,geneToMutateY],  math.fabs(self.genome[geneToMutateX,geneToMutateY])) 
         
        if self.genome[geneToMutateX,geneToMutateY] > 1: 
            self.genome[geneToMutateX,geneToMutateY] = 1 
 
        if self.genome[geneToMutateX,geneToMutateY] < -1: 
            self.genome[geneToMutateX,geneToMutateY] = -1 

 
    def Print(self): 
        print '[', 'ID:', self.ID, 'Fitness:', self.fitness, ']', 


    def Get_Fitness_Data(self):

        light = self.sim.Get_Sensor_Data(sensorID=7)
        
        self.fitnessLight = light[-1]

        y = self.sim.Get_Sensor_Data(sensorID=5)

        x = self.sim.Get_Sensor_Data(sensorID=6)

        tailSensors = self.sim.Get_Sensor_Data(sensorID=4)

        tailWag = tailSensors[0:1000:10]

        # pawSensors = list()

        # for sn in range(0,4):
        #     pawSensors.append(self.sim.Get_Sensor_Data(sensorID=sn)[-1])

        # print pawSensors

        # if sum(pawSensors) >= 3:
        #     self.goodPaws.append(1)

        # else:
        #     self.goodPaws.append(0)


        # print "Good paws", self.goodPaws

        self.fitnessY = y[-1]

        self.fitnessX = x[-1]

        for i in range(0,99):
            wagDiff = abs(tailWag[i] - tailWag[i + 1])
            # print "Wag Oscillation: ", wagDiff
            if wagDiff > 0.6:
                self.wagCount += 1
            i += 2

        print "Wags: ", self.wagCount  

        print "Light: ", self.fitnessLight

        self.fitness = (self.fitnessLight + (self.wagCount * 0.001))


        
        
