import random
from tkinter import *
import  time

size_wight = 500
game_height = 500
snake_item = 20
snake_color1 = "red"
snake_color2 = "yellow"

virtual_game_x = size_wight//snake_item
virtual_game_y = game_height//snake_item


snake_x = virtual_game_x//2
snake_y = virtual_game_y//2
snake_x_nav = 0
snake_y_nav = 0


Game_Running = True
check_can_we_delete_snake_item = []
present_list = []
bind_all = []

snake_size = 5


tk = Tk()
tk.title("Игра Змейка на Пайтон")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

present_color1 = "blue"
present_color2 = "black"
presents_list = []
present_size = 25
for i in range(present_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item, y * snake_item + snake_item,
                             fill=present_color2)
    id2 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                             y * snake_item + snake_item - 2, fill=present_color1)
    present_list.append([x, y, id1, id2])
print(present_list)

def snake_paint_item(canvas, x, y):
    global snake_size
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                  y * snake_item + snake_item, fill=snake_color2)
    id2 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                  y * snake_item + snake_item - 2, fill=snake_color1)

    snake_size.append([x, y, id1, id2])
    print(snake_size)




def check_we_delete_snake_item():
    if len(snake_size) >= snake_size:
        temp_item = snake_size.pop(0)
        # print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def check_if_we_found_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            # print("found!!!")
            snake_size = snake_size + 1
            canvas.delete(presents_list[i][2])
            canvas.delete(presents_list[i][3])
        # print(snake_x, snake_y)


def snake_move(event):
    global snake_x
    global  snake_y
    global  snake_x_nav
    global  snake_y_nav

    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    check_if_we_found_present()


#canvas.bind_all("<KeyPress-Left>," snake_move)
#canvas.bind_all("<KeyPress-Right>," snake_move)
#canvas.bind_all("<KeyPress-Up>," snake_move)
#canvas.bind_all("<KeyPress-Down>," snake_move)


def game_over():
    global Game_Running
    Game_Running = False

def check_if_borders():
    if snake_x > virtual_game_x or snake_x<0 or snake_y>virtual_game_y or snake_y<0:
        game_over()

def check_we_touch_self(f_x, f_y):
    global Game_Running
    if not (snake_x_nav == 0 and snake_y_nav == 0):
        for i in range(len(snake_size)):
            if snake_size[i][0] == f_x and snake_size[i][1] == f_y:
                print("found!!!")
                Game_Running = False

while Game_Running:
    check_if_we_found_present()
    check_if_borders()
    check_we_touch_self(snake_x + snake_x_nav, snake_y + snake_y_nav)
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    tk.update_idletasks()
    tk.update()
    time.sleep(0.15)

def fun_nothing(event):
    pass
canvas.bind_all("<KeyPress-Left>", fun_nothing)
canvas.bind_all("<KeyPress-Right>", fun_nothing)
canvas.bind_all("<KeyPress-Up>", fun_nothing)
canvas.bind_all("<KeyPress-Down>", fun_nothing)
