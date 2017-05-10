from pyrosim import PYROSIM 
from robot import ROBOT 
import random 
from individual import INDIVIDUAL 
from population import POPULATION 
import copy 
import constants as con
from smile_detect import SMILE
import pickle
import matplotlib.pyplot as plt


# fileName ='robotdata.p'
# f = open(fileName,'r')
# robotData = pickle.load(f)
# f.close()

# parents = robotData

parents = POPULATION(con.PopSize)

parents.Evaluate() 

fitnessList = list()
  
for g in range (0, con.Gens+1): 

    children = copy.deepcopy(parents) 
 
    children.Mutate() 

    children.Evaluate()
 
    fitnessList.append(parents.Replace_With(children))
 
    print "<<<< GENERATION >>>>", g, "\n"

    children.Print() 

    # print "fitness list = ", fitnessList

# parents.Print()



pickle.dump(parents, open('robotdata.p','wb'))

# print "Best: ", parents.Print()   

parents.Show_Best()
# parents.Show_Best()

fig = plt.figure()

pn = fig.add_subplot(111)

plt.plot(fitnessList)

plt.ylabel('fitness')

plt.xlabel('generations')

pn.set_ylim(0,+5)

pn.set_xlim(0,con.Gens)

plt.show()


 

 
 
#     print "Generation", "[", i, "]", "PW:", parent.genome, " Parent:", parent.fitness, " Child:", child.fitness 
 
# # print sensorData 
 
