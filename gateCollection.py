import math

def print_truth_table(n,y,value):
    # n is the number of inputs
    # y is an array of outputs in an exact order
    # value is an array of values in an exact order
    if n == 2:
        a = [True,True,False,False]
        b = [True,False,True,False]
        d = {1: [a[0], b[0],y[0],value[0]], 2: [a[1], b[1],y[1],value[1]], 3: [a[2], b[2],y[2],value[2]], 4: [a[3], b[3],y[3],value[3]]}
        print ("{:<3} {:<3} {:<3} {:<3}".format('a','b','y','value'))
        for k, v in d.items():
            a,b,y,value = v
            print ("{:<3} {:<3} {:<3} {:<3}".format(a, b, y, value))
    
    if n == 3:
        a = [False, False, False, False, True, True, True, True]
        b = [False, False, True, True, False, False, True, True]
        c = [False, True, False, True, False, True, False, True]

        d = {1: [a[0], b[0],c[0],y[0],value[0]], 2: [a[1], b[1],c[1],y[1],value[1]], 3: [a[2], b[2],c[2],y[2],value[2]], 4: [a[3], b[3],c[3],y[3],value[3]], 5: [a[4], b[4],c[4],y[4],value[4]], 6: [a[5], b[5],c[5],y[5],value[5]], 7: [a[6],b[6],c[6],y[6],value[6]], 8: [a[7], b[7],c[7],y[7],value[7]]}
        print ("{:<3} {:<3} {:<3} {:<3} {:<3}".format('a','b','c','y','value'))
        for k, v in d.items():
            a,b,c,y,value = v
            print ("{:<3} {:<3} {:<3} {:<3} {:<3}".format(a, b, c, y, value))

def calculate_score(n,y,value):
    # n is the number of inputs
    # y is an array of outputs
    # value is an array of the values associated with each y

    lowestON = 0
    highestOFF = 0
    if n == 2:
        for i in range(4):
            if y[i] == True:
                if lowestON == 0:
                    lowestON = value[i]
                elif value[i] < lowestON:
                    lowestON = value[i]
            if y[i] == False:
                if highestOFF == 0:
                    highestOFF = value[i]
                elif value[i] > highestOFF:
                    highestOFF = value[i]
        ratio = lowestON / highestOFF
        score = math.log(ratio,10)

    if n == 3: 
        for i in range(8):
            if y[i] == True:
                if lowestON == 0:
                    lowestON = value[i]
                elif value[i] < lowestON:
                    lowestON = value[i]
            if y[i] == False:
                if highestOFF == 0:
                    highestOFF = value[i]
                elif value[i] > highestOFF:
                    highestOFF = value[i]
        ratio = lowestON / highestOFF
        score = math.log(ratio,10)
    
    return score



y = [True,False,True,False,True,False,True,False]
value = [0.1,0.5,18,3,67,3,1,.05]
print_truth_table(3,y,value)
score1 = calculate_score(3,y,value)
print('Score is: ', score1)

print('\n')

y = [False,True,True,False]
value = [0.01,15,16,0.02]
print_truth_table(2,y,value)
score = calculate_score(2,y,value)
print('Score is: ', score)