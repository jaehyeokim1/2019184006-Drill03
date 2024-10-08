from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x, y)  
    delay(0.1)

def run_circle():
    print('Circle')

    r, cx, cy = 300, 800 // 2, 600 // 2 
    for degree in range(0, 360, 3):

        theta = math.radians(degree) 
        x = r * math.cos(theta) + cx  
        y = r * math.sin(theta) + cy 
        draw_boy(x,y)
        

def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass

def run_right():
    print('RIGHT')
    for y in range(550,0,-10):
        draw_boy(790,y)
    pass

def run_bottom():
    print('BOTTOM')
    for x in range(800,0,-10):
        draw_boy(x,0)
    pass

def run_left():
    print('LEFT')
    for y in range(0,550,10):
        draw_boy(0,y)
    pass

def run_diagonal1():
    print('Diagonal1')

    x, y = 800, 600  
    
    while x > 400 and y > 300:  
        x = x - 10  # x 좌표 감소 (왼쪽으로 이동)
        y = y - 10  # y 좌표 감소 (아래로 이동)def run_triangle():
        draw_boy(x,y)

def run_diagonal2():
    print('Diagonal2')

    x, y = 400,300

    while x > 0 and y < 600:
        x = x - 10
        y = y + 10
        draw_boy(x,y)
        
def run_rectangle():
    print('Rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_triangle():
    run_diagonal1()
    run_diagonal2()
    run_top()
while True:
    run_circle()
    run_rectangle()
    run_triangle()
    

close_canvas()
