from TwitchPlays_KeyCodes import *
import inspect, re

''' file format
up  HR:W
down  HR:S
left  HR:A
right  HR:D
shoot up  R:J-H-K  H:U
shoot down  R:U-H-K  H:J
shoot left  R:U-J-K  H:H
shoot right  R:U-J-H  H:K
be a man  R:U-J-H-K
'''

#read/load input from file and transfer to dictionary
#@inputFile - name of file
#return - dictionary
def readFile(inputFile):
  inputList = {}
  #starting reading file
  with open(inputFile, "r") as file:
    #get each file line by line
    for line in file:
      #split line of string from, command name : command dectionary
      line = line.strip().split("  ", 1)      
      inputName, inputCommands = line[0], line[1]
      inputList[inputName] = readCommands(inputCommands, ":")
  return inputList


#read commands string and transfer to dictionary
#Note: each command keys are stored as a variable name (output will show binary convertion of the hex value of key that was assign to it)
#@inputCommands - string of commands
#@splitBy - probably don't need, but split string by certain character
#return dictionary of type of commands with array list of keys
def readCommands(inputCommands, splitBy):
  commandList = {}
  for line in inputCommands.split():
    commandType, keys = line.split(splitBy)
    keyList = keys.split("-")
    for i, char in enumerate(keyList):
      keyList[i] = char
      #print(varname(globals()[]))
    commandList[commandType] = keyList
  return commandList
  
#
def writeCommand(fileName, inputDic):
  file = open(fileName, "a")
  for commandKey in inputDic:
    curStr = commandKey;
    for commandType in inputDic[commandKey]:
      curStr =  curStr + "  " + commandType + ":";
      for idx, keys in enumerate(inputDic[commandKey][commandType]):
        if idx != 0:
          curStr = curStr + "-"
        curStr = curStr + keys 
    file.write(curStr + "\n")
  file.close      


#add command to dictionary
def addCommand(inputDic, inputName, inputType, inputKey):
  if searchCommand(inputDic, inputName, inputType):
    inputDic[inputName][inputType].append(inputKey) 
  else:
    if inputName not in inputDic:
      inputDic[inputName] = {inputType: [inputKey]}
    else:
      if inputType not in inputDic[inputName]:
        inputDic[inputName][inputType] = [inputKey]
      else:
        inputDic[inputName][inputType] = []
        inputDic[inputName][inputType].append(globals()[inputKey]) 
  

#search if command exist in the dictionary
def searchCommand(inputDic, inputName, inputType):
  isExist = False
  if inputName in inputDic:
    print(inputName)
    if inputType in inputDic[inputName]:
      isExist = True
  return isExist

#remove command from dictionary (in progress ...)
#Note: if inputKey doesn't exist in array list, it remove the inputType dictionary
#      if inputType doesn't exist in dictionary, it remove the inputName dictionary
def removeCommand(inputDic, inputName, inputType, inputKey):
  if inputType in inputDic[inputName]:
    if globals()[inputKey] in inputDic[inputName][inputType]:  
      
      #remove first element similar to inputType
      inputDic[inputName][inputType].remove(inputKey)
    else:
      del inputDic[inputName][inputType]
  else:
    del inputDic[inputName]
  

#print formated version of dictionary
def print_command(dct):
  print("Command List:")
  for inputName, inputCommand in dct.items():  
    print("{} {}".format(inputName, inputCommand))


#Print variable name
#https://stackoverflow.com/questions/592746/how-can-you-print-a-variable-name-in-python
def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)