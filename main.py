from gateCollection import *
from gateFunctions import *
from InputOutputOPs import *
from Optimization import *
import numpy

'''
User imports a file with their circuits and gates

Calculate initial score --> output that 

Then run algorithm to improve the score --> output that and show what we did to improve
'''

if __name__ == "__main__":
  filename = input("Please enter library filename: ")
  collections = getCollections(filename)
  filename = input("Please enter input filename: ")
  inputFile = getCollections(filename)
  
  numberGates = int(input("Please enter the number of gates: "))
  netlist = [""]*numberGates
  for i in range(numberGates):
  	netlist[i] = input("Please enter next line of netlist: ")
  
  inputNames = [""]*3
  abc = ["a", "b", "c"]
  for i in range(3):
    inputNames[i] = input("Please enter the name of the input model for input ", abc[i], ": ")
  
  inputs = [0]*6
  inputs[0] = inputFile["models"][inputNames[0]]["parameters"][1]["value"]
  inputs[1] = inputFile["models"][inputNames[0]]["parameters"][0]["value"]
  
  inputs[2] = inputFile["models"][inputNames[1]]["parameters"][1]["value"]
  inputs[3] = inputFile["models"][inputNames[1]]["parameters"][0]["value"]
  
  inputs[4] = inputFile["models"][inputNames[2]]["parameters"][1]["value"]
  inputs[5] = inputFile["models"][inputNames[2]]["parameters"][0]["value"]
    
  models = [""]*numberGates
  for i in range(numberGates):
    modelName = input("Please enter the name of Gate ", i ,"'s model in netlist: ")
    models[i] = collections["models"][modelName]
  
  initY, initVals = getTT(netlist,inputs,models)
  initScore = calculate_score(3,initY,initVals)
  print_truth_table(3,initY,initVals)

  print('The initial score is: ', initScore)
  print('\n')
  
  newGates, improvement = ImproveScore(netlist,inputs,models)
  
  for count,gate in enumerate(newGates):
    print('Improve gate ', gate["name"], ' by: ')
	  # If the impovement is 0 it doesn't print because nothing is changing
    if improvement[count][0] > 0:
      print('Stronger promoter by a factor of ', improvement[count][0])
    elif improvement[count][0] < 0: 
      print('Weaker promoter by a factor of ', improvement[count][0])
    
    if improvement[count][1] != 0:
      print('Stretch by a factor of ', improvment[count][1])
  
    if improvement[count][2] > 0: 
      print('Stronger RBS by a factor of ', improvement[count][2])
    elif improvement[count][2] < 0:
      print('Weaker RBS by a factor of ', improvement[count][2])
  
    if improvement[count][3] > 0: 
      print('Increase slope by a factor of ', improvement[count][3])
    elif improvement[count][3] < 0:
      print('Decrease slope by a factor of ', improvement[count][3])
    print("\n")
        
  newY, newVals = getTT(netlist,inputs,newGates)
  newScore = calculate_score(3,newY,newVals)
  print_truth_table(3,newY,newVals)
  print('The new score is: ', newScore)
  
  # POTENTIALLY WRITE THE COMMAND LINE TO A NEW FILE 
    
