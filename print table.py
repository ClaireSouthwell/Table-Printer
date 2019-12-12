tableData = [['kiwis', 'melons', 'cherries', 'persimmon'],
             ['Gilbert', 'Bobby', 'Caroline', 'David'],
             ['antelope', 'cats', 'pandas', 'goose', 'red pandas']]

#Account for the possibility that some lists might be longer than others
#The length of the longest inner list is stored in maxLength
maxLength = 0

for innerList in tableData:
    if len(innerList) > maxLength:
        maxLength = len(innerList)

print(maxLength)

#Now in range maxLength, print that element of each inner List

def printTable():
#How many columns do we need?     
    colWidths = [0] * len(tableData) #[0, 0, 0,]
    print(len(colWidths))
#How wide do they need to be? Get the widths
    for i in range(len(colWidths)): #for each inner list...
        print(i)
        for j in range(len(tableData[i])):  #for each item in the list
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
        print(colWidths[i])
    print(colWidths)
#Now find the widest column
    maxWidth = 0
    for width in colWidths:
        if width > maxWidth:
            maxWidth = width
    print(maxWidth)


#print all the things     
    for item in range(maxLength):
        for innerList in tableData:
            try:
                innerList[item] = innerList[item].rjust(maxWidth)
                print(innerList[item], end='') 
            except IndexError:
                print(''.rjust(maxWidth), end='')
                
        print('')

printTable()
