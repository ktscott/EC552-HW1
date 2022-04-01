#######################################################
# Defining the 7 function that can manipulate the gates
#######################################################

import json

'''
ymax is the max value of the gate
ymin is the min value of the gate
n is the slope of the curve / transfer function
K = Kd of the curve of the distance between 0 to the mid-point of the max slope in the x axis

Parameters array info
[0] is ymax, [1] is ymin, [2] is K , [3] is n

model is the specific model associated with the gate
x is the value of how you want the parameter to change
updates the model with the new adjusted parameter
'''

def stretch(model, x):
    # Stretch increases ymax and decreases ymin
    if x <= 1.5:
        model['parameters'][0]['value'] = model['parameters'][0]['value'] * x
        model['parameters'][1]['value'] = model['parameters'][1]['value'] / x
    else: 
        print('Not a valid input')

    return model
     
def increase_slope(model,x):
    # Increases slope of the transfer curve
    if x <= 1.05:
        model['parameters'][3]['value'] = model['parameters'][3]['value'] * x 
    else:
        print('Not a valid input')
    
    return model 

def decrease_slope(model,x):
    # Decreases slope of the transfer curve
    if x <= 1.05:
        model['parameters'][3]['value'] = model['parameters'][3]['value'] / x
    else:
        print('Not a valid input')
    
    return model

def stronger_promoter(model,x):
    # Stronger promoter increases both ymax and ymin
    model['parameters'][0]['value'] = model['parameters'][0]['value'] * x
    model['parameters'][1]['value'] = model['parameters'][1]['value'] * x
    
    return model


def weaker_promoter(model,x):
    # Weaker promoter decreases both ymax and ymin
    model['parameters'][0]['value'] = model['parameters'][0]['value'] / x
    model['parameters'][1]['value'] = model['parameters'][1]['value'] / x
    
    return model

def stronger_rbs(model,x):
    # Stronger RBS decreases the value of K
    model['parameters'][2]['value'] = model['parameters'][2]['value'] / x
    
    return model

def weaker_rbs(model,x):
    # Weaker RBS increases the value of K
    model['parameters'][2]['value'] = model['parameters'][2]['value'] * x
    
    return model