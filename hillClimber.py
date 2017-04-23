from pyrosim import PYROSIM
import matplotlib.pyplot as plt
from robot import ROBOT
import random
from individual import INDIVIDUAL
import copy
import pickle


for i in range(0,2): 

    parent = INDIVIDUAL()

    for i in range(0,100): 
 
        parent Evaluate(False,True)

        child = copy.deepcopy(parent)
 
        child.Mutate()

 
sensorData = sim.Get_Sensor_Data(sensorID=2) 
 
print sensorData 

print "Generation", "[", i, "]", "PW:", parent.genome, " Parent:", parent.fitness, " Child:", child.fitness 
 
# f = plt.figure()

if child.fitness > parent.fitness:
    parent = child

    child.Start_Evaluation(False,False)


# f = plt.figure() 
 
# pn = f.add_subplot(111) 

 
# plt.plot(sensorData) 
 
# pn.set_ylim(-2,+2) 
 
# plt.show