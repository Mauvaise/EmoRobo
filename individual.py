from pyrosim import PYROSIM 
from robot import ROBOT 
import random
import math 
import numpy
import constants as con
from smile_detect import SMILE
 
class INDIVIDUAL: 
    def __init__(self, i): 
 
        self.genome = numpy.random.random((4, 8)) * 2 - 1 
 
        self.fitness = 0 

        self.ID = i
         

    def Start_Evaluation(self, paused, blind):

        self.sim = PYROSIM(playPaused=paused,  playBlind=blind, evalTime=con.evaluationTime) 

        robot = ROBOT(self.sim, self.genome) 
 
        self.sim.Start()

        # self.smile_detect = SMILE()

        # self.smile_detect.Start_Smile_Evaluation(con.evaluationTime)


    def Compute_Fitness(self):

        self.sim.Wait_To_Finish()

        y = self.sim.Get_Sensor_Data(sensorID=4 , s=1 ) 

        self.fitness = y[-1]

        # self.smile_detect.End_Smile_Evaluation()

        del self.sim
        

    def Mutate(self): 
 
        geneToMutateX = random.randint(0,3) 
 
        geneToMutateY = random.randint(0,7)         
 
        self.genome[geneToMutateX,geneToMutateY] = random.gauss(self.genome[geneToMutateX,geneToMutateY],  math.fabs(self.genome[geneToMutateX,geneToMutateY])) 
         
        if self.genome[geneToMutateX,geneToMutateY] > 1: 
            self.genome[geneToMutateX,geneToMutateY] = 1 
 
        if self.genome[geneToMutateX,geneToMutateY] < -1: 
            self.genome[geneToMutateX,geneToMutateY] = -1 

 
    def Print(self): 
        print '[', self.ID, self.fitness, ']', 

        
        
