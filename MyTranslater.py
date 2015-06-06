import DYPL
import Parser
import math
from JythonTranslater import Jtrans
class Translate(Jtrans):
    def __init__(self):
        self.instance = None
        self.draw = True
        self.angle = -90
        self.current_x = 0
        self.current_y = 0
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
    def move_forward(self):
        self.move(1, self.angle)
    def move_backward(self):
        self.move(1, -self.angle)
    def move(self, step, angle):
        y_steps = math.sin(math.radians(self.angle)) * step
        new_y = self.current_y + y_steps
        x_steps = math.cos(math.radians(self.angle)) * step
        new_x = self.current_x + x_steps
        self.setAngle(angle)
        if self.draw:
            self.draw_line(self.current_x, new_x, self.current_y, new_y)       
    
    def turn_cw(self,angle):
        self.setAngle(angle)
    def turn_ccw(self, angle):
        self.setAngle(-angle)
    def put(self, x, y, angle):
        self.current_x = x
        self.current_y = y
        self.angle = angle-90  
    #Bresenham's line algorithm. Based on code from the literate program and roguebasin
    #http://en.literateprograms.org/Bresenham's_line_algorithm_(Python)
    #http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm       
    def draw_line(self, x0, x1, y0, y1):
        
        steep = abs(y1-y0) > abs(x1-x0)
        new_x = x1
        new_y = y1
        
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        
        deltax = x1-x0
        deltay = abs(y1-y0)
        error = int(deltax / 2.0)
        y_step = 1 if y0 < y1 else -1
        y = y0
        
        for x in range(int(x0), int(x1)+1):
            if steep:
                DYPL.setPixel(self.instance, int(y), int(x))
            else:
                DYPL.setPixel(self.instance, int(x), int (y))
            error -= deltay
            if error < 0:
                y += y_step
                error += deltax
        
        self.current_x = new_x
        self.current_y = new_y
        
    def setAngle(self, angle):
        self.angle += int(angle)
        if self.angle < 0:
            self.angle += 360
        if self.angle > 360:
            self.angle -= 360            