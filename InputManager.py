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
      inputList[inputName] = readCommands(inputCommands)
  return inputList


#read commands string and transfer to dictionary
#@inputCommands - string of commands
#return dictionary of type of commands with array list of keys
def readCommands(inputCommands):
  commandList = {}
  #split each type of commands on a line
  for line in inputCommands.split():
    #split each command type from keys into a dictionary
    commandType, keys = line.split(":")

    #split each key into a list of keys
    keyList = keys.split("-")
    for i, char in enumerate(keyList):
      keyList[i] = char
    commandList[commandType] = keyList
  return commandList
  
#write command dictionary into file
#@fileName - name of file
#@inputDic - dictionary of commands
def writeFile(fileName, inputDic):
  file = open(fileName, "a")
  #get through each part of nested dictionary/ array into a string and write to file
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

#empty out file
#@fileName - name of file wanted to be emptied
def emptiedFile(fileName):
  #seen pointless to make function for it
  open('writeInput.txt', 'w').close()

#add command to dictionary
#@inputDic - Distionary of commands
#@inputName - the name of the command/ string that chat have to input to call the command
#@inputType -  Type of input function to call, like...
#             (HR(HoldAndReleaseKey), 
#              H (HoldKey), 
#              R (Release)) 
#@inputKey - keyboards keys that wanted to use, like...
#             W,A,S,D
def addCommand(inputDic, inputName, inputType, inputKey):
  #check if inputType exist in dictionary
  if searchCommand(inputDic, inputName, inputType):
    inputDic[inputName][inputType].append(inputKey) 
  else:
    #if not, lets check where to start adding in the dictionary
    #if inputName doesn't exist in dictionary, lets add it with everything else
    if inputName not in inputDic:
      inputDic[inputName] = {inputType: [inputKey]}
    else:
      #if inputType doesn't exist in dictionary, add it and add keys
      if inputType not in inputDic[inputName]:
        inputDic[inputName][inputType] = [inputKey]
      else:
        #add new empty array and the 
        #probably don't need this
        inputDic[inputName][inputType] = []
        inputDic[inputName][inputType].append(globals()[inputKey]) 
  

#search if command exist in the dictionary
##@inputDic - Distionary of commands
#@inputName - the name of the command/ string that chat have to input to call the command
#@inputType -  Type of input function to call, like...
#             (HR(HoldAndReleaseKey), 
#              H (HoldKey), 
#              R (Release)) 
#return - True if command exist, False if not
def searchCommand(inputDic, inputName, inputType):
  isExist = False
  if inputName in inputDic:
    print(inputName)
    if inputType in inputDic[inputName]:
      isExist = True
  return isExist

#remove command from dictionary (SHOULD CHANGE IF THING GOES MESSY!)
#Note: if inputKey doesn't exist in array list, it remove the inputType dictionary
#      if inputType doesn't exist in dictionary, it remove the inputName dictionary
#@inputDic - Distionary of commands
#@inputName - the name of the command/ string that chat have to input to call the command
#@inputType -  Type of input function to call, like...
#             (HR(HoldAndReleaseKey), 
#              H (HoldKey), 
#              R (Release)) 
#@inputKey - keyboards keys that wanted to use, like...
#             W,A,S,D
def removeCommand(inputDic, inputName, inputType, inputKey):
  if inputType in inputDic[inputName]:
    if inputKey in inputDic[inputName][inputType]:  
      #remove first key element similar from array
      print(inputKey);
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