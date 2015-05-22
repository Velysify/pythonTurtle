import re
import MyTranslater

def parse(translater, string):
    translater = translater
    commandList = string.split("\n")

    for command in commandList:
        penDown = re.search(r'\s*pen[ _]down', command)
        penUp = re.search(r'\s*pen[ _]up',command)
        moveForward  = re.search(r'\s*move[ _]forward',command)
        moveBackward = re.search(r"\s*move[ _]backward", command)
        move = re.search("\s*move (\d*),(\d)", command)
        turncw = re.search("\s*turn[ _]cw (\d)", command)
        turnccw = re.search("\s*turn[ _]ccw (\d)", command)
        put = re.search("\s*put (\d*),(\d*),(\d)", command)
        if(command == ""):
            pass
        elif penDown:
            translater.pen_down()
        elif penUp:
            translater.pen_up()
        elif moveForward:
            translater.move_forward()
        elif moveBackward:
            translater.move_backward()
        elif move:
            move_command = []
            command = str(str(command).split(" ")).split(",")
            for cmd in command:
                cmd = cmd.strip("]").strip(" ").strip("'")
                move_command.append(cmd)
            steps = move_command[1]
            angle = move_command[2]
            translater.move(int(steps), int(angle))
            
        elif turncw:
            command = str(command).split(" ")
            angle = command[1]
            translater.turn_cw(angle)
        elif turnccw:
            command = str(command).split(" ")
            angle = command[1]
            translater.turn_ccw(angle)
        elif put:
            put_command = []
            command = str(str(command).split(" ")).split(",")
            for cmd in command:
                cmd = cmd.strip("]").strip(" ").strip("'")
                put_command.append(cmd)
            x = put_command[1]
            y = put_command[2]
            angle = put_command[3]
            translater.put(x,y,angle)
        else:
            print("Not a match")

    

