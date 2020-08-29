import sys

#print ('# of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
#print(type(sys.argv[1]))
#print(sys.argv[1])

q = sys.argv[1].split()
if q[0] != "select":
    print("Missing select statement")
    exit    

#print("q", q)
conditions =[]
fields = ["name","pb","pe","yield"]

i = 0
while i < len(q):
    if q[i] in fields:
        condition = {
            "field":q[i],
            "op":q[i+1],
            "limit":q[i+2]
        }
        conditions.append(condition)
    i += 1    

with open('stocks.csv') as f:
    lines = f.readlines()

column_index = { "code":0 ,"name":1, "pe":2, "pb":3, "yield":4, "time":5 }

result = []

#print("conditions", conditions)
#print("# conditions", len(conditions))

lines = iter(lines)
next(lines) #skip headerline
for line in lines:
    #print("line", line)
    exclude = False
    for condition in conditions:
        field = condition["field"]
        op = condition["op"]
        field_index = column_index[field]
        temp_line = str(line).split(",")
        value = temp_line[field_index]
           
        try:
            v = float(value.strip())
            limit = float(condition["limit"].strip())
        except:
            print("Cant convert " + str(v) + " to float")  
            continue

        if op is ">":
            #print("eval rule >") 
            if v <= limit:
                exclude = True
                #print("exclude True")
                #break
            
        if op is "<":
            #print("eval rule <") 
            if v > limit:
                exclude = True
                #print("exclude True")
                #break         

    if exclude == False:
        #print("adding line" ,line)
        result.append(line)
        #print(result)    

print("Code, Name, pe, pb, yield, time")

for item in result:
    print(item)         

print("Results: " + str(len(result)))
