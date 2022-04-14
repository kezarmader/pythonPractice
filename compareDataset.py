import json

def compareObjectArray(newFileLocation, oldFileLocation, keyName):
    oldJSONFile = open(oldFileLocation, "r")
    newJSONFile = open(newFileLocation, "r")

    oldJSON = json.load(oldJSONFile)
    newJSON = json.load(newJSONFile)

    oldJSON.sort(key=lambda object:object[keyName])
    newJSON.sort(key=lambda object:object[keyName])

    newDataDic = {}
    for i, obj in enumerate(newJSON):
        newDataDic[obj[keyName]] = obj

    oldDataDic = {}
    for i, obj in enumerate(oldJSON):
        oldDataDic[obj[keyName]] = obj

    isSame = True
    for i, obj in enumerate(oldJSON):
        if oldJSON[i][keyName] not in newDataDic:
            isSame = False
            print('\tmissing in new',oldJSON[i][keyName])
        elif json.dumps(oldJSON[i]) != json.dumps(newDataDic[oldJSON[i][keyName]]):
            isSame = False
            print('\told is NOT new?', oldJSON[i][keyName])

    for i, obj in enumerate(newJSON):
        if newJSON[i][keyName] not in oldDataDic:
            isSame = False
            print('\tmissing in old',newJSON[i][keyName])
        elif json.dumps(newJSON[i]) != json.dumps(oldDataDic[newJSON[i][keyName]]):
            isSame = False
            print('\tnew is NOT old?', newJSON[i][keyName])

    if isSame:
        print('\tThe File is identical')

def compareIntArray(newFileLocation, oldFileLocation):
    oldJSONFile = open(oldFileLocation, "r")
    newJSONFile = open(newFileLocation, "r")

    oldJSON = json.load(oldJSONFile)
    newJSON = json.load(newJSONFile)

    oldJSON.sort()
    newJSON.sort()

    newDataDic = {}
    for i, obj in enumerate(newJSON):
        newDataDic[obj] = obj

    oldDataDic = {}
    for i, obj in enumerate(oldJSON):
        oldDataDic[obj] = obj

    isSame = True
    for i, obj in enumerate(oldJSON):
        if oldJSON[i] not in newDataDic:
            isSame = False
            print('\tmissing in new',oldJSON[i])

    for i, obj in enumerate(newJSON):
        if newJSON[i] not in oldDataDic:
            isSame = False
            print('\tmissing in old',newJSON[i])

    if isSame:
        print('\tThe File is identical')

print('comparing Request')
compareIntArray("./newRequest.json", "./oldRequest.json")

print('comparing Response')
compareObjectArray("./newResponse_Trial2.json", "./oldResponse.json", 'uniqueId')
