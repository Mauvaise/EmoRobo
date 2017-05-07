from pyrosim import PYROSIM 
from robot import ROBOT 
import random 
from individual import INDIVIDUAL 
from population import POPULATION 
import copy 
import constants as con
from smile_detect import SMILE
import pickle

fileName ='robotdata.p'
f = open(fileName,'r')
robotData = pickle.load(f)
f.close()


# parents = POPULATION() 

parents = robotData
 
# parents.Evaluate() 
  
for g in range (0,1): 

    children = copy.deepcopy(parents) 
 
    children.Mutate() 
 
    children.Evaluate()
 
    parents.Replace_With(children) 
 
    print g, 

parents.Print()

pickle.dump(parents, open('robotdata.p','wb'))





# print "Best: ", parents    

# parents.Show_Best()

 

 
 
#     print "Generation", "[", i, "]", "PW:", parent.genome, " Parent:", parent.fitness, " Child:", child.fitness 
 
# # print sensorData 
 
# # f = plt.figure() 
 
# # pn = f.add_subplot(111) 
 
# # plt.plot(sensorData) 
 
# # pn.set_ylim(-2,+2) 
 
# # plt.show
