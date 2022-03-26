


d = {1: [False, False,"0","0.01"], 2: ["0", "1","1","15"], 3: ["1", "0","1","16"], 4: ["1", "1","0","0.02"]}
print ("{:<3} {:<3} {:<3} {:<3}".format('a','b','y','value'))
for k, v in d.items():
    a,b,y,value = v
    print ("{:<3} {:<3} {:<3} {:<3}".format(a, b, y, value))


