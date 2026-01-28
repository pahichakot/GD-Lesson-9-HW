#Ocean CLeaner- Pick up fish and avoid fish
#Recycle Paper Bag Game
import pgzrun
import random

#Setup
WIDTH = 800
HEIGHT = 600

FINAL_LEVEL = 6
current_level = 1

#List of non recyclable items
ITEMS = ["fish", "fish", "fish", "fish"]

START_SPEED = 10

#When you lose the game
game_over = False
#When you win the game
game_complete = False

items = []
animations = []

#Draw background and ending message
def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    #Background
    screen.blit("oceanimg",(0,0))

    #Display message for game over
    if game_over:
        display_message("GAME OVER","Try again.")
    #Display message for game completion
    elif game_complete:
        display_message("YOU WON!", "Congratulations.")
    #Keep playing game
    else:
        for item in items:
            item.draw()

#Print heading and subheading
def display_message(heading, subheading):
    screen.draw.text(heading, fontsize = 60, center = (400, 300), color = "black")
    screen.draw.text(subheading, fontsize = 30, center = (400, 330), color = "black")

#Monitor items list -- if empty, makes more
def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down        

#Make items
def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

#Get items randomly from list
def get_option_to_create(number_of_extra_items):
    items_to_create = ["trash"]
    for i in range(0, number_of_extra_items):
        choice = random.choice(ITEMS)
        items_to_create.append(choice)
    return items_to_create

#Create actors
def create_items(items_to_create):
    new_items = []
    for i in items_to_create:
        item = Actor(i+"img")
        new_items.append(item)
    return new_items

#Organize items on background neatly
def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gapsize = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    #enumerate function will access list value and its index
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gapsize
        item.x = new_x_pos

#Make items move down
def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        #Increase speed
        duration = START_SPEED - current_level
        animation = animate(item, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

#If you lose game
def handle_game_over():
    global game_over
    game_over = True

#CLick on objects
def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            #Click on paper
            if "trash" in item.image:
                handle_game_complete()
            #Click on any other object
            else:
                handle_game_over()

#Game or level is complete
def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    #End game
    if current_level == FINAL_LEVEL:
        game_complete = True
    #Next level
    else:
        current_level += 1
        items = []
        animations = []

#Stop all animations
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

pgzrun.go()