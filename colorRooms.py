def main():
    inputPlan = ["##########", "#   #    #", "#   #    #", "## #### ##", "#        #", "#        #", "##########"]
    result = colorTheFloot(inputPlan)
    
    output = ""
    for row in result:
        rowStr = ""
        for unit in row:
            if unit == -1:
                rowStr += '#'
            elif unit == 0:
                rowStr += ' '
            else:
                rowStr += str(unit)
        output += "\n" + rowStr
    
    print(output)

def colorTheFloot(inputPlan):
    floorPlan = [[-1 for _ in range(len(inputPlan[0]))] for _ in range(len(inputPlan))]
    
    lastRoomNo = 0
    for row in range(1, len(inputPlan)):
        for col in range(1, len(inputPlan[row])):
            if inputPlan[row][col] != '#': #is this wall
                if inputPlan[row - 1][col] == '#' and inputPlan[row + 1][col] == '#' or inputPlan[row][col - 1] == '#' and inputPlan[row][col + 1] == '#': #is This Door
                    floorPlan[row][col] = 0
                elif inputPlan[row][col - 1] != '#': #is Left Open
                    floorPlan[row][col] = floorPlan[row][col - 1]
                elif inputPlan[row - 1][col] != '#': #is Top Open
                    floorPlan[row][col] = floorPlan[row - 1][col]
                else:
                    lastRoomNo += 1
                    print(lastRoomNo, 'i m in', row, col)
                    floorPlan[row][col] = lastRoomNo
    return floorPlan

def isDoorOrWall(inputPlan, row, col):
    if inputPlan[row][col] == '#':
        return True
    if inputPlan[row - 1][col] == '#' and inputPlan[row + 1][col] == '#':
        return True
    if inputPlan[row][col - 1] == '#' and inputPlan[row][col + 1] == '#':
        return True
    
    return False
    
if __name__ == '__main__':
    main()