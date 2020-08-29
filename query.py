import sys

def print_result_to_console(result):
    bar_length = 47
    print "-" * bar_length
    print "QUERY: " + sys.argv[1]
    print "-" * bar_length
    print "%-7s %-15s %7s %7s %7s" % ("CODE", "NAME", "P/E", "P/B", "YIELD")
    print "-" * bar_length

    for item in result:
        item = item.split(",")
        code = item[0]
        name = item[1]
        pe = item[2]
        pb = item[3]
        yld = item[4]
        print "%-7s %-15s %7s %7s %7s" % (code, name, pe, pb, yld)
    print "-" * bar_length
    print "Results: " + str(len(result))
    print "-" * bar_length

def main():
    q = sys.argv[1].split()
    if q[0] != "select":
        print "Missing select statement"
        exit    

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

    lines = iter(lines)
    next(lines) #skip header
    for line in lines:
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
                continue

            if op is ">":
                if v <= limit:
                    exclude = True
                
            if op is "<":
                if v > limit:
                    exclude = True       

        if exclude == False:
            result.append(line)
    
    print_result_to_console(result)

if __name__ == "__main__":
    main()