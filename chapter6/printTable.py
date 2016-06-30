def printTable(tableData):
    maxlen = 0
    for item in tableData:
        for subitem in item:
            if len(subitem) > maxlen:
                maxlen = len(subitem)
    
    for item in tableData:
        for subitem in item:    
            print(subitem.rjust(maxlen), end=" ")
        print()
            

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#print(len(tableData))
printTable(tableData)
    