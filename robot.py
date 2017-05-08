from pyrosim import PYROSIM 
import constants as con
 
class ROBOT: 
    def __init__(self, sim, wts): 
        self.Send_Objects(sim) 
        self.Send_Joints(sim) 
        self.Send_Sensors(sim) 
        self.Send_Neurons(sim) 
        self.Send_Synapses(sim,wts) 

    #Objects      
    def Send_Objects(self, sim):
        #Main body
        # sim.Send_Box(objectID=0, x=0, y=0, z=con.Leg + con.Radius, length=2 *con.Leg, 
        #              width=con.Leg, height=2 * con.Radius, r=0.5, g=0.5, b=0.5)
        sim.Send_Cylinder(objectID=0, x=0, y=0, z=con.Leg + con.Radius,
                     r1=1, r2=0, r3=0, length=1.8 *con.Leg, radius=con.Leg/1.8, r=0.5, g=0.5, b=0.5)
        #Dark Red top 
        sim.Send_Cylinder(objectID=1, x=con.Leg_Offset, y=con.Leg, z=con.Leg + con.Radius, 
                          r1=0, r2=1, r3=0, length=con.Leg, radius=con.Radius, r=0.5, g=0, b=0)
        #Dark Green top
        sim.Send_Cylinder(objectID=2, x=-con.Leg_Offset, y=con.Leg, z=con.Leg + con.Radius, 
                          r1=0, r2=1, r3=0, length=con.Leg, radius=con.Radius, r=0, g=0.5, b=0) 
        #Dark Blue top
        sim.Send_Cylinder(objectID=3, x=con.Leg_Offset, y=-con.Leg, z=con.Leg + con.Radius, 
                          r1=0, r2=1, r3=0, length=con.Leg, radius=con.Radius, r=0, g=0, b=0.5) 
        #Dark Purple top
        sim.Send_Cylinder(objectID=4, x=-con.Leg_Offset, y=-con.Leg, z=con.Leg + con.Radius, 
                          r1=0, r2=1, r3=0, length=con.Leg, radius=con.Radius, r=0.5, g=0, b=0.5) 
        #Light Red bottom
        sim.Send_Cylinder(objectID=5, x=con.Leg_Offset, y=1.5 * (con.Leg), z=0.5 * con.Leg + con.Radius, 
                          r1=0, r2=0, r3=1, length=con.Leg, radius=con.Radius, r=1, g=0, b=0) 
        #Light Green bottom
        sim.Send_Cylinder(objectID=6, x=-con.Leg_Offset, y=1.5 * (con.Leg), z=0.5 * con.Leg + con.Radius, 
                          r1=0, r2=0, r3=1, length=con.Leg, radius=con.Radius, r=0, g=1, b=0) 
        #Light Blue bottom
        sim.Send_Cylinder(objectID=7, x=con.Leg_Offset, y=-1.5 * (con.Leg), z=0.5 * con.Leg + con.Radius, 
                          r1=0, r2=0, r3=1, length=con.Leg, radius=con.Radius, r=0, g=0, b=1) 
        #Light Purple bottom
        sim.Send_Cylinder(objectID=8, x=-con.Leg_Offset, y=-1.5 * (con.Leg), z=0.5 * con.Leg + con.Radius, 
                          r1=0, r2=0, r3=1, length=con.Leg, radius=con.Radius, r=1, g=0, b=1) 
        #Robot tail
        sim.Send_Cylinder(objectID=9, x=-con.Leg*1.9, y=0, z=con.Leg + con.Radius*2, 
                  r1=1, r2=0, r3=0, length=con.Leg, radius=0.02, r=0.5, g=0.5, b=0.5) 
        #Robot neck
        sim.Send_Cylinder(objectID=10, x=con.Leg, y=0, z= 1.4*con.Leg + con.Radius, 
                  r1=0.5, r2=0, r3=0.5, length=con.Radius, radius=con.Radius, r=0.7, g=0.7, b=0.7) 
        #Robot head
        sim.Send_Cylinder(objectID=11, x=con.Leg*1.5, y=0, z=1.6 * con.Leg + con.Radius, 
                  r1=1, r2=0, r3=0, length=con.Radius*2, radius=con.Radius*1.5, r=0.5, g=0.5, b=0.5) 



    #Joints
    def Send_Joints(self, sim):
        #Body to dark red 
        sim.Send_Joint(jointID=0, firstObjectID=0, secondObjectID=1, x=con.Leg_Offset, y=con.Leg / 2, z=con.Leg + con.Radius, n1=-1, n2=0, n3=0)
       
        #Dark red to light red 
        sim.Send_Joint(jointID=1, firstObjectID=1, secondObjectID=5, x=con.Leg_Offset, y=1.5 *con.Leg, z=con.Leg + con.Radius, n1=-1, n2=0, n3=0)
       
        #Body to dark green  
        sim.Send_Joint(jointID=2, firstObjectID=0, secondObjectID=2, x=-con.Leg_Offset, y=con.Leg / 2, z=con.Leg + con.Radius, n1=-1, n2=0, n3=0) 
        
        #Dark green to light green
        sim.Send_Joint(jointID=3, firstObjectID=2, secondObjectID=6, x=-con.Leg_Offset, y=1.5 *con.Leg, z=con.Leg + con.Radius, n1=-1, n2=0, n3=0) 
        
        #Body to dark blue  
        sim.Send_Joint(jointID=4, firstObjectID=0, secondObjectID=3, x=con.Leg_Offset, y=-con.Leg/2, z=con.Leg + con.Radius, n1=1, n2=0, n3=0) 
       
        #Dark blue to light blue
        sim.Send_Joint(jointID=5, firstObjectID=3, secondObjectID=7, x=con.Leg_Offset, y=-1.5*con.Leg, z=con.Leg + con.Radius, n1=1, n2=0, n3=0) 
       
        #Body to dark purple
        sim.Send_Joint(jointID=6, firstObjectID=0, secondObjectID=4, x=-con.Leg_Offset, y=-con.Leg / 2, z=con.Leg + con.Radius, n1=1, n2=0, n3=0) 
        
        #Dark purple to light purple
        sim.Send_Joint(jointID=7, firstObjectID=4, secondObjectID=8, x=-con.Leg_Offset, y=-1.5 *con.Leg, z=con.Leg + con.Radius, n1=1, n2=0, n3=0) 

        #Body to tail
        sim.Send_Joint(jointID=8, firstObjectID=0, secondObjectID=9, x=-con.Leg*1.8/2, y=0, z=con.Leg + con.Radius*2, n1=0, n2=0, n3=1, speed = 3.0) 

        #Body to neck
        sim.Send_Joint(jointID=9, firstObjectID=0, secondObjectID=10, x=con.Leg/2, y=0, z=1.4*con.Leg + con.Radius, n1=0, n2=0, n3=1) 

        #Neck to head
        sim.Send_Joint(jointID=10, firstObjectID=10, secondObjectID=11, x=con.Leg/2, y=0, z=1.6 * con.Leg + con.Radius, n1=1, n2=0, n3=0) 

        
 
        
    #Sensors
    def Send_Sensors(self, sim): 
        sim.Send_Touch_Sensor(sensorID=0, objectID=5) 
        sim.Send_Touch_Sensor(sensorID=1, objectID=6) 
        sim.Send_Touch_Sensor(sensorID=2, objectID=7) 
        sim.Send_Touch_Sensor(sensorID=3, objectID=8)
        sim.Send_Proprioceptive_Sensor(sensorID=4, jointID=8)
        sim.Send_Position_Sensor(sensorID=5, objectID=0)
        sim.Send_Position_Sensor(sensorID=6, objectID=10)

 
    #Neurons
    def Send_Neurons(self, sim):
        #Sensor neurons
        for sn in range(0, 5): 
            sim.Send_Sensor_Neuron(neuronID=sn, sensorID=sn)


        #Motor neurons
        for mn in range(0,9): 
            sim.Send_Motor_Neuron(neuronID=mn+5, jointID=mn, tau=0.3) 


    #Synapses
    def Send_Synapses(self, sim, wts): 
        for s in range(0, 5): 
          for v in range(0,9): 
            sim.Send_Synapse(sourceNeuronID=s, targetNeuronID= v + 5, weight=wts[s][v]) 

