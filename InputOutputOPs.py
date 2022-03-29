import json
from gateCollection import response_function

def readJSON(filepath):
    with open(filepath) as f:
        data = json.load(f)


    collections = {}
    for mydict in data:
        if "name" in mydict.keys():
            collections[mydict["collection"]] = {}
        else:
            collections[mydict["collection"]] = []

    for mydict in data:
        # if the collection has a name associated with each piece, you can index using the name
        if "name" in mydict.keys():
            collections[mydict["collection"]][mydict["name"]] = mydict
        else:
            collections[mydict["collection"]] += [mydict]

    return collections

def getTT(netlist, inputs, models):
    '''
    Assumptions: three inputs (a,b,c), one output (y)
    Also, assuming that wires' inputs are specified before
    they themselves are used as inputs

    Will return an 8-long list of True or False values,
    these values will go in order of (a,b,c) = (0,0,0) to
    (a,b,c) = (1,1,1), where a is the most significant bit.
    '''
    out = [False]*8
    count = 0
    # Each wire will be represented as a string of the formula to get its value
    # e.g. if "NOT(0Wire15990,a)", then in the dictionary you will find:
    #    wires[0Wire15990] = "(not(a))"
    wires = {"a":["a", inputs[0]],"b":["b", inputs[1]],"c":["c", inputs[2]]}
    for connection in netlist:
        (gate, argstr) = connection.split('(')
        argstr = argstr.replace(')','')
        args = argstr.split(',')
        
        # second item in output is ---- response_function(models[count], wires[args[1]][1]) -----
        if gate == "NOT":
            wires[args[0]] = ["(not(" + wires[args[1]][0] + "))", response_function(models[count], wires[args[1]][1])]
        elif gate == "NOR":
            wires[args[0]] = ["(not(" + wires[args[1]][0] + " or " + wires[args[2]][0] + "))", response_function(models[count], wires[args[1]][1] + wires[args[2]][1])]
        elif gate == "OUTPUT_OR":
            wires[args[0]] = ["(" + wires[args[1]][0] + " or " + wires[args[2]][0] + ")", response_function(models[count], wires[args[1]][1]+wires[args[2]][1])]
        elif gate == "NAND":
            wires[args[0]] = ["(not(" + wires[args[1]][0] + " and " + wires[args[2]][0] + "))", response_function(models[count], wires[args[1]][1]+wires[args[2]][1])]
        elif gate == "BUF":
            wires[args[0]] = args[1]

        count += 1


    count = 0
    for a in [False,True]:
        for b in [False,True]:
            for c in [False,True]:
                out[count] = eval(wires['y'])
                count += 1

    return out