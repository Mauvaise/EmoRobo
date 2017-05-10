from individual import INDIVIDUAL 
import constants as con
from smile_detect import SMILE
import pickle
 
class POPULATION: 
  def __init__(self, popSize): 

    self.population = {} 

    self.fitnessList = list()

 
    for i in range(0, popSize): 
      self.population[i] = INDIVIDUAL(i) 

 
  def Print(self): 
    for i in self.population: 
      self.population[i].Print() 
 
    print "\n" 
 
  def Evaluate(self): 
    for i in self.population: 
      self.population[i].Start_Evaluation(con.Paused, con.Blind)

    # smile_detect = SMILE()

    # smile_detect.Start_Smile_Evaluation(con.evaluationTime) 
 
    for i in self.population: 
      fitness = self.population[i].Compute_Fitness()
    # return fitness
      # self.population[i].fitness = smile_detect.Send_Total_Smiles()
      
 
  def Mutate(self): 
    for i in self.population: 
      self.population[i].Mutate()   
 
  def Replace_With(self,other): 
    for i in self.population: 
      print "Fitness in Replace_With", self.population[i].fitness
      if (self.population[i].fitness < other.population[i].fitness): 
        self.population[i] = other.population[i]
      return self.population[i].fitness
        

  def Show_Best(self):
    best = INDIVIDUAL(-1)

    for i in self.population:
      if best.fitness < self.population[i].fitness:
        best = self.population[i]

    print "Fitness of best robot being displayed:", best.fitness
    best.Start_Evaluation(True, False)




