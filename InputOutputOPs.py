import json

def readJSON(filepath):
    '''
    If the JSON file has a collection that includes a field called "name",
    the name will be used as a key to access the subsequent set in that collection.
    For example, if there is a field called "models" that has a field called "name",
    then you will be able to call collections["models"][-given name to the model-]

    This relies on the fact that each collection has multiple instances of
    - for example - models, say one called Gate1_model
    '''
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

def getTT(netlist, inputs, models, print_netlist = False):
    '''
    Assumptions: three inputs (a,b,c), one output (y)
    Also, assuming that wires' inputs are specified before
    they themselves are used as inputs

    Will return an 8-long list of True or False values,
    these values will go in order of (a,b,c) = (0,0,0) to
    (a,b,c) = (1,1,1), where a is the most significant bit.
    '''
    # 'inputs' input will be a 6-long list, identifying low and high value for each

    out = [False for _ in range(8)]
    values = [0 for _ in range(8)]
    # Each wire will be represented as a string of the formula to get its value
    # e.g. if "NOT(0Wire15990,a)", then in the dictionary you will find:
    #    wires[0Wire15990] = "(not(a))"
    # wires stores the wire's logical formula in str format
    wires = {"a":["a", "a_in"],"b":["b","b_in"],"c":["c","c_in"]}
    for count,connection in enumerate(netlist):
        (gate, argstr) = connection.split('(')
        argstr = argstr.replace(')','')
        args = argstr.split(',')
        
        ymin = str(models[count]["parameters"][1]["value"])
        ymax = str(models[count]["parameters"][0]["value"])
        K = str(models[count]["parameters"][2]["value"])
        n = str(models[count]["parameters"][3]["value"])

        # first item in wires' value is ---- logical formula as str -----
        # second item in wires' value is --- response function as str ---
        if gate == "NOT":
            x = "(" + wires[args[1]][1] + ")"

            # wires[key][1] = (ymin+(ymax-ymin)/(1+(x/K)**n))
            wires[args[0]] = ["(not(" + wires[args[1]][0] + "))",
                              "(" + ymin + "+(" + ymax + "-" + ymin + ")/(1+(" + x + "/" + K + ")**" + n + "))"]
            
        elif gate == "NOR":
            x = "(" + wires[args[1]][1] + "+" + wires[args[2]][1] + ")"

            wires[args[0]] = ["(not(" + wires[args[1]][0] + " or " + wires[args[2]][0] + "))",
                              "(" + ymin + "+(" + ymax + "-" + ymin + ")/(1+(" + x + "/" + K + ")**" + n + "))"]

        elif gate == "OUTPUT_OR":
            x = "(" + wires[args[1]][1] + "+" + wires[args[2]][1] + ")"
            
            wires[args[0]] = ["(" + wires[args[1]][0] + " or " + wires[args[2]][0] + ")",
                              "(" + ymin + "+(" + ymax + "-" + ymin + ")/(1+(" + x + "/" + K + ")**" + n + "))"]

        elif gate == "NAND":
            x = "(" + wires[args[1]][1] + "+" + wires[args[2]][1] + ")"

            wires[args[0]] = ["(not(" + wires[args[1]][0] + " and " + wires[args[2]][0] + "))",
                              "(" + ymin + "+(" + ymax + "-" + ymin + ")/(1+(" + x + "/" + K + ")**" + n + "))"]
        elif gate == "BUF":
            wires[args[0]] = [args[1], wires[args[1]][1]]

        if print_netlist:
            print(connection + " Gate" + str(count))

    count = 0
    for a in [False,True]:
        for b in [False,True]:
            for c in [False,True]:
                out[count] = eval(wires['y'][0])
                a_in = inputs[a]
                b_in = inputs[2+b]
                c_in = inputs[4+c]
                values[count] = eval(wires['y'][1])
                count += 1

    return (out,values)