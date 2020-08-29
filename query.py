import sys

print ('# of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print(type(sys.argv[1]))
print(sys.argv[1])

q = sys.argv[1].split()
if q[0] != "select":
    print("Missing select statement")
    exit    

print("q", q)
conditions =[]
fields = ["name","pb","pe","yield"]

i = 0
while i < len(q):
    if q[i] in fields:
        condition = {
            "field":q[i],
            "op":q[i+1],
            "limit":float(q[i+2])
        }
        conditions.append(condition)
    i += 1    

with open('stocks.csv') as f:
    lines = f.readlines()

column_index = { "code":0 ,"name":1, "pe":2, "pb":3, "yield":4, "time":5 }

result = []

print("conditions", conditions)

lines = iter(lines)
next(lines) #skip headerline
for line in lines:
    exclude = False
    for condition in conditions:
        field = condition["field"]
        op = condition["op"]
        limit = condition["limit"]
        field_index = column_index[field]
        line = str(line).split(",")
        value = line[field_index]
        try:
           v = float(value)
        except:
            print("Cant convert " + value + " to float")  
            continue

        if op is ">":
           if v <= limit:
               exclude = True
               break
        if op is "<":
            if v >= limit:
                exclude = True
                break         

    if exclude == False:
        result.append(line)

print("result count", len(result))

print(result)
for item in result:
    print(item[0] + " " + item[1] + " " + item[2] + " " + item[3] + " " + item[4])         

