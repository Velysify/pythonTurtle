import Translater
import DYPL
import Parser
import math
from JythonTranslater import Jtrans
class Translate(Jtrans):
    def __init__(self):
        self.instance = None
        self.draw = False
        self.angle = 0
        self.current_x = 100
        self.current_y = 100
        pass
    def actionPerformed(self, event):
        print("Button clicked. Got event:")
        Parser.parse(self, DYPL.getCode(self.instance))
    def setDYPL(self, obj):
        print("DYPL instance here!")
        self.instance = obj
    def pen_down(self):
        self.draw = True
    def pen_up(self):
        self.draw = False
    def move_forward(self): #Trasig
        self.move(1, self.angle)
    def move_backward(self): #Trasig
        self.move(1,-self.angle)
    def move(self, step, angle):
        y_steps = int(math.sin(math.radians(angle)) * step)
        new_y = self.current_y + y_steps
        x_steps = int(math.cos(math.radians(angle)) * step)
        new_x = self.current_x + x_steps
        if self.draw:
             self.draw_line(self.current_x, new_x, self.current_y, new_y)
        self.current_x += x_steps
        self.current_y += y_steps
        self.angle = angle
    def turn_cw(self,angle):
        self.angle += int(angle)
    def turn_ccw(self, angle):
        self.angle -= int(angle)
    def put(self, x, y, angle):
        self.current_x = int(x)
        self.current_y = int(y)
        self.angle = int(angle)          
    def draw_line(self, x0, x1, y0, y1):
        print x1
        print x0
        deltax = x1 - x0
        deltay = y1 - y0
        error = 0
        print deltax
        if deltax !=0:
            deltaerr = abs((deltay / deltax))
            y = y0
            if x1 > x0:
                for x in range(x0,x1):
                    DYPL.setPixel(self.instance, int(x), int(y))
                    error = error + deltaerr
                    while error >= 0.5:
                        DYPL.setPixel(self.instance, int(x), int(y))
                        y = y + math.copysign(1,(y1 - y0))
                        error = error - 1.0
            else:
                for x in range(x1,x0):
                    DYPL.setPixel(self.instance, int(x), int(y))
                    error = error + deltaerr
                    while error >= 0.5:
                        DYPL.setPixel(self.instance, int(x), int(y))
                        y = y + math.copysign(1,(y1 - y0))
                        error = error - 1.0
        else:
            if y1 > y0:
                for y in range(y0,y1):
                    DYPL.setPixel(self.instance, x1,y)
            else:
                for y in range(y1,y0):
                    DYPL.setPixel(self.instance, x1,y)
                
            