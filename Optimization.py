import numpy as np
import copy
from gateFunctions import *
from gateCollection import *
from InputOutputOPs import *

def ImproveScore(netlist, inputs, models):
  '''
  For every model, we want to maximize each parameter,
  then move on to the next model. We do this to improve
  overall score. 
  '''
  newModels = [copy.deepcopy(model) for model in models]
  tempModels = [copy.deepcopy(model) for model in models]
  improvement = [[0]*4]*len(models)
  
  y,values = getTT(netlist,inputs,models)
  bestScore = calculate_score(3,y,values)
  
  for count,model in enumerate(models):
    for parameter in range(3):
      # this makes sure we iterate through every param:
      #   ymax, ymin, K, n
      # for every model.
      
      # for each parameter, find value to maximize score
      
      
      if parameter == 0: 
      	# ymax & ymin coupled b/c every function changes both of them

        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,5,0.01):
          tempModels[count] = stronger_promoter(newModels[count],i)
          y,values = getTT(netlist, inputs, newModels)
          score = calculate_score(3,y,values)
          if score >= bestScore:
            newModels[count] = tempModels[count]
            bestScore = score
            improvement[count][0] = i

        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,5,0.01):
          tempModels[count] = weaker_promoter(newModels[count],i)
          y,values = getTT(netlist, inputs, newModels)
          score = calculate_score(3,y,values)
          if score >= bestScore:
            newModels[count] = tempModels[count]
            bestScore = score
            # store improvement as negative val if weaker_prom did it
            improvement[count][0] = -i

        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,1.5,0.01):
          tempModels[count] = stretch(newModels[count],i)
          y,values = getTT(netlist, inputs, newModels)
          score = calculate_score(3,y,values)
          if score >= bestScore:
            newModels[count] = tempModels[count]
            bestScore = score
            # store improvement as negative val if weaker_prom did it
            improvement[count][1] = i
              
      elif parameter == 1:
        # changing K - K ranges between 0 and 1 so do not want to exceed that
        # Would iterate from 1 to 1.5 in step-sizes of 0.005
        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,1.5,0.005):
            tempModels[count] = stronger_rbs(newModels[count],i)
            y,values = getTT(netlist, inputs, newModels)
            score = calculate_score(3,y,values)
            if score >= bestScore:
              newModels[count] = tempModels[count]
              bestScore = score
              improvement[count][2] = i

        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,1.5,0.005):
            tempModels[count] = weaker_rbs(newModels[count],i)
            y,values = getTT(netlist, inputs, newModels)
            score = calculate_score(3,y,values)
            if score >= bestScore:
              newModels[count] = tempModels[count]
              bestScore = score
              # store improvement as negative val if weaker_prom did it
              improvement[count][2] = -i
        
        
      elif parameter == 2:
        # changing n - already have a max which is 1.05
        # Iterate from 1 to 1.05 in a step size of 0.001
        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,1.05,0.001):
          tempModels[count] = increase_slope(newModels[count],i)
          y,values = getTT(netlist, inputs, newModels)
          score = calculate_score(3,y,values)
          if score >= bestScore:
            newModels[count] = tempModels[count]
            bestScore = score
            improvement[count][3] = i
          
        tempModels = [copy.deepcopy(nm) for nm in newModels]
        for i in np.arange(1,1.05,0.001):
          tempModels[count] = decrease_slope(newModels[count],i)
          y,values = getTT(netlist, inputs, newModels)
          score = calculate_score(3,y,values)
          if score >= bestScore:
            newModels[count] = tempModels[count]
            bestSCore = score
            improvement[count][3] = -i

    return newModels, improvement