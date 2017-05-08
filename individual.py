from pyrosim import PYROSIM 
from robot import ROBOT 
import random
import math 
import numpy
import constants as con

from smile_detect import SMILE
 
class INDIVIDUAL: 
    def __init__(self, i): 
 
        self.genome = numpy.random.random((5, 9)) * 2 - 1 
 
        self.fitness = 0

        self.fitnessY = 0

        self.fitnessX = 0

        self.pawSensors = list()

        self.tailSensors = list()

        self.ID = i


    def Start_Evaluation(self, paused, blind):

        self.sim = PYROSIM(playPaused=paused,  playBlind=blind, evalTime=con.evaluationTime) 

        robot = ROBOT(self.sim, self.genome) 
 
        self.sim.Start()

        # print 'Current eval ID', self.ID

        # smile_detect = SMILE()

        # smile_detect.Start_Smile_Evaluation(con.evaluationTime)



    def Compute_Fitness(self):

        self.sim.Wait_To_Finish()

        y = self.sim.Get_Sensor_Data(sensorID=5)

        x = self.sim.Get_Sensor_Data(sensorID=6)

        wagCount = 0

        # counter

        tailWag = list()

        self.tailSensors = self.sim.Get_Sensor_Data(sensorID=4)

        tailWag = self.tailSensors[0:1000:10]

        print tailWag

        # for angle in range(len(self.tailSensor)):

        # abs(first) - 1 + abs(second) - 1 > 5:
        


        for sn in range(0,4):
            self.pawSensors.append(self.sim.Get_Sensor_Data(sensorID=sn)[-1])


 

        self.fitnessY = y[-1]

        self.fitnessX = x[-1]

        # print "Y fitness: ", self.fitnessY

        # print "X fitness: ", self.fitnessX

        if self.fitnessY <= 0.5 and self.fitnessX >= 0.5:
            if all(self.pawSensors) < 0.2:
                self.fitness = (abs(self.fitnessY) + abs(self.fitnessX))*2
                # print "GOOD", self.fitness
        else:
            self.fitness = abs(self.fitnessY) + abs(self.fitnessX) 
            # print "BAD", self.fitness

        del self.sim

        

    def Mutate(self): 
 
        geneToMutateX = random.randint(0,4) 
 
        geneToMutateY = random.randint(0,8)         
 
        self.genome[geneToMutateX,geneToMutateY] = random.gauss(self.genome[geneToMutateX,geneToMutateY],  math.fabs(self.genome[geneToMutateX,geneToMutateY])) 
         
        if self.genome[geneToMutateX,geneToMutateY] > 1: 
            self.genome[geneToMutateX,geneToMutateY] = 1 
 
        if self.genome[geneToMutateX,geneToMutateY] < -1: 
            self.genome[geneToMutateX,geneToMutateY] = -1 

 
    def Print(self): 
        print '[', 'ID:', self.ID, 'Fitness:', self.fitness, ']', 

        
        
