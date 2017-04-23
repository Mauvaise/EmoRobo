from individual import INDIVIDUAL 
import constants as con
 
class POPULATION: 
  def __init__(self, popSize): 

    self.population = {} 
 
    for i in range(0, popSize): 
      self.population[i] = INDIVIDUAL(i) 
 
  def Print(self): 
    for i in self.population: 
      self.population[i].Print() 
 
    print "\n" 
 
  def Evaluate(self): 
    for i in self.population: 
      self.population[i].Start_Evaluation(con.Paused, con.Blind)
 
    for i in self.population: 
      self.population[i].Compute_Fitness()
 
  def Mutate(self): 
    for i in self.population: 
      self.population[i].Mutate()   
 
  def Replace_With(self,other): 
    for i in self.population: 
       
      if (self.population[i].fitness < other.population[i].fitness): 
        self.population[i] = other.population[i]

  def Show_Best(self):
    for i in self.population:
      print "Best robot being displayed:", self.population[i].fitness
      self.population[i].Start_Evaluation(False, False)

