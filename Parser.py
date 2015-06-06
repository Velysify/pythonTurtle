import re
import MyTranslater

def parse_command(command):
    try:
        if command.find("(") == -1:
            command = command + "()"
        if command.find(" ", 0, 6) > 0:
            command = command.replace(" ","_", 1)
        command = "translater." + command
        return command
    except AttributeError:
        print("Not a command!")

def parse_loop(loop):
    loop = loop.replace("to", "in xrange(")
    loop = loop.replace(" do", "):")
    commands = loop[loop.index(":"):len(loop)]
    loop = loop[0: loop.index(":")+1]
    commandsList = commands.split("\n")
    loop_commands = []
    for x in commandsList:
        if x != ":" and x:
            loop_commands.append(parse_command(x))
    commands = "\n    ".join(loop_commands)
    loop = loop + "\n    " + commands
    range1 = loop[loop.index("=")+1:loop.index("in xrange")]
    command = loop.replace("=", "")
    #Only works for x=0 esc syntax. Breaks at for var = 0 since the index of the value moves...
    commandPart1 = command[0: command.index("(")+1]
    commandPart2 = command[command.index("(")+1: len(command)]
    commandPart1 = commandPart1.replace(range1," ")
    command = commandPart1 + range1 + "," + commandPart2
    return command

def sort_command_list(commandList, loopList):
    in_for_loop = False
    list_to_return = []
    index = 0
    for command in commandList:
        if command.find("for ") != -1:
            list_to_return.append(loopList[index])
            in_for_loop = True
            index += 1
        elif not in_for_loop:
            list_to_return.append(command)
        elif command.find("end") != -1:
            in_for_loop = False
    return list_to_return

def parse(translater, string):
    loopList = []
    commandList = string.split("\n")
    for x in xrange(0,string.count('for ')):
        loop = string[string.index('for '):string.index('end')]
        string = string[0: string.index('for ')] + string[string.index('end') + 3: len(string)]
        loop = parse_loop(loop)
        loopList.append(loop)

    commandList = sort_command_list(commandList, loopList)
    for command in commandList:
        if(command == ""):
            pass
        elif(command.find("for ") != -1):
            exec(command)
        else:
            command = parse_command(command)
            print command
            eval(command)
