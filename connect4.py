# connect 4 
def drawField(field1):
    for row in range(12):
        if row%2 == 0:
            lineRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    lineColumn = int(column/2)
                    if column != 12:
                        print(field1[lineColumn][lineRow], end = "")
                    else:
                        print(field1[lineColumn][lineRow])
                else:
                    print("|", end = "")
        else:
            print("-------------")

player = 1
currentField = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
drawField(currentField)
rowcounter = 5
while(True):
    print("player turn: ", player)
    ColumnChoose = int(input("Select the column from 0 to 6 whwre you want to drop your turn: \n"))
    #rowchoose = int(input("Select the row you want to: \n"))
    if player == 1:
        while(True):
            if currentField[ColumnChoose][rowcounter] == " ":
                currentField[ColumnChoose][rowcounter] = "X"
                player = 2 
                rowcounter = 5 
                break
            else:
                rowcounter -= 1
    else:
        while (True):
            if currentField[ColumnChoose][rowcounter] == " ":
                currentField[ColumnChoose][rowcounter] = "O"
                player = 1
                rowcounter = 5
                break
            else:
                rowcounter -= 1
    drawField(currentField)
    print(currentField)

# this is kind of nice game