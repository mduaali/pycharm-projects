from tkinter import *
import random

    #   'unchangeable constants'
GAME_WIDTH = 700                    #   width of game area (pixels)
GAME_HEIGHT = 700                   #   width of game height (pixels)
SPEED = 80                          #   speed of snake, delay in ms (lower = faster)
SPACE_SIZE = 50                     #   size of one grid cell
BODY_PARTS = 3                      #   starting length of snake
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS     #   current num of segments
        self.coordinates = []           #   list [x,y] positions for each segment
        self.squares =[]                #   list of canvas rectangles for each segment

        for i in range(0,BODY_PARTS):   #   start with all body parts at position [0,0]
            self.coordinates.append([0,0])

        #   draw rectangle for each coordinate store id in square
        for x, y in self.coordinates:
            square =  canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill = SNAKE_COLOR, tags = "snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        #   choose random grid cell in game area for food to show up
        x = random.randint(0 , (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0 , (GAME_HEIGHT // SPACE_SIZE)-1) * SPACE_SIZE

        #   store food position
        self.coordinates = [x,y]

        #   draw create food oval
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tags = "food")

def next_turn(snake, food):

    #get current head position at index 0
    x,y = snake.coordinates[0]

    #   update head position based on direction
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    #   insert new head at beginning of coordinates list
    snake.coordinates.insert(0, (x,y))

    #   draw new head square on canvas
    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill = SNAKE_COLOR)

    #   insert new head square id at beginning of the square list
    snake.squares.insert(0, square)

    #   check if snake has eaten food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        #   increment score
        score += 1

        #   update label to display score
        label.config(text = "Score: {}".format(score))

        #   delete food (using tag food)
        canvas.delete("food")

        #   create new random food object
        food = Food()

    else:

        #   remove last segment position (tail) from coordinates
        del snake.coordinates[-1]

        #   delete last segment square from canvas
        canvas.delete(snake.squares[-1])

        #   removes last square id form list
        del snake.squares[-1]

    #   if collision end game
    if check_collision(snake):
        game_over()

    else:   #   if not, next move
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    #   use if statements for no 180 turns
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collision(snake):
    #   head position
    x,y = snake.coordinates[0]

    #   check collisions with walls
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    #   check collision with own body except head
    for body_part in snake.coordinates[1::]:
        if x == body_part[0] and y == body_part[1]:
            return True

    #   no collision
    return False

def game_over():
    canvas.delete(ALL)  #   clear everything

    #   display game over and SPACE to play again option
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("Arial", 70), text = "GAME OVER", fill = 'red')
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 80, font=("Arial", 20),
                       text = "Press SPACE to play again", fill = 'white')
    window.bind('<space>', lambda event: restart_game())

#   function to restart game
def restart_game():
    global snake, food, score, direction

    window.unbind('<space>')    #   unbind space for bug fix
    canvas.delete(ALL)          #   clear everything

    score = 0                   #   reset back to default
    direction = 'down'
    label.config(text = "Score: {}".format(score))

    snake = Snake()             #   recreate objects
    food = Food()

    next_turn(snake, food)      #   call next turn

window = Tk()                   #   create window
window.title("Snake Game")
#window.resizable(False, False)

score = 0                       #   score initially 0
direction = 'down'              #   default direction down

#   label to display score and pack
label = Label(window, text = "Score: {}".format(score), font=("Arial", 40))
label.pack()

#   canvas for snake game and pack
canvas = Canvas(window, bg= BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

#   update window
window.update()

#   center window in middle of screen
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#   calculate top-left corner so window is centered
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

#   set window size and position: "widthxheight+x+y"
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#   bind keys with lambda function calling change_direction function with appropriate directions
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

#   create snake and food objects instances of Snake() and Food() class
snake = Snake()
food = Food()

#   start game loop
next_turn(snake, food)

#   start tkinter event loop
window.mainloop()
