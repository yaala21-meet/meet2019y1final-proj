# setting up
import turtle
turtle.hideturtle()
turtle.tracer(1,0)
options = []
healths = []
energys = []
environments = []
impact = []
turtle.screensize(6000,2000)

# creating the bars
health = turtle.Turtle()
health.speed(100)
health.hideturtle()
health.penup()
health.goto(-100, 350)
health.write("health: 75")
energy = turtle.Turtle()
energy.speed(100)
energy.hideturtle()
energy.penup()
energy.goto(0, 350)
energy.write("energy: 75")
environment = turtle.Turtle()
environment.speed(100)
environment.hideturtle()
environment.penup()
environment.goto(100, 350)
environment.write("environment: 75")

#adding start points
for i in range(75):
    healths.append(1)
    environments.append(1)

for i in range(50):
    energys.append(1)

# creating the character
character = turtle.Turtle()
character.hideturtle()

# choice turtle
turtle.register_shape("goodmorning.gif")
turtle.register_shape("wake.gif")
turtle.register_shape("snooze.gif")
turtle.register_shape("walk.gif")
turtle.register_shape("brush.gif")
turtle.register_shape("shower.gif")
turtle.register_shape("short.gif")
turtle.register_shape("long.gif")
turtle.register_shape("clothes.gif")
choice = turtle.Turtle()
choice.shape("goodmorning.gif")
choice.hideturtle()
choice.penup()

# first choice
choice.stamp()
choice.goto(turtle.xcor(),100)
choice.shape("wake.gif")
choice.stamp()
options.append(choice.pos())
choice.shape("snooze.gif")
choice.goto(turtle.xcor(),-100)
choice.stamp()
options.append(choice.pos())

# choosing function
def choose():
    if character.ycor() >= 300:
            health.clear()
            energy.clear()
            environment.clear()
            health.goto(health.xcor(), character.ycor()+50)
            energy.goto(energy.xcor(), character.ycor()+50)
            environment.goto(environment.xcor(), character.ycor()+50)
            health.write("health: " + str(len(healths)))
            energy.write("energy: " + str(len(energys)))
            environment.write("environment: " + str(len(environments)))
    if character.pos() in options[-2:] or (len(options) == 35 and character.pos() in options[-3:]):
        if len(options) == 2: #get up
            if options.index(character.pos()) == 0:
                print("you woke up immediately.")
                for i in range(5):
                    energys.pop(0)
            else:
                print("you snoozed.")
                for i in range(5):
                    healths.pop(0)
            choice.shape("walk.gif")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 3: #brush teeth
            print("you got up.")
            choice.shape("brush.gif")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 4: #shower for..
            print("you brushed your teeth.")
            choice.shape("shower.gif")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 5: #long / short
            print("shower for...")
            choice.shape("long.gif")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            choice.shape("short.gif")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 7: #get dressed
            if options.index(character.pos()) == 5:
                print("you showered for a long time.")
                for i in range(10):
                    environments.pop(0)
                for i in range(5):
                    energys.pop(0)
            else:
                print("you showered for a short time.")
                for i in range(5):
                    environments.pop(0)
                    healths.pop(0)
            choice.shape("clothes.gif")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 8: #eat breakfast
            print("you got dressed.")
            #choice.shape("breakfast")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 9: #ac
            print("you ate breakfast.")
            #choice.shape("ac")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 10: #on / off
            print("leave the ac...")
            #choice.shape("ac on")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("ac off")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 12: #get outside
            if options.index(character.pos()) == 10:
                print("you left your ac on.")
                for i in range(10):
                    environments.pop(0)
            else:
                print("you left your ac off.")
                for i in range(8):
                    healths.pop(0)
                    energys.pop(0)
            #choice.shape("outside")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 13: #order coffee in:
            print("you went outside.")
            #choice.shape("coffee")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 14: #single use/ reuseable
            print("get your coffee in a...")
            #choice.shape("single use")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("reuseable (expensive)")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 16: #walk out:
            if options.index(character.pos()) == 14:
                print("you got your coffee in a single use cup.")
                for i in range(5):
                    environments.pop(0)
            else:
                print("you payed for a reusable cup.")
                for i in range(8):
                    energys.pop(0)
            #choice.shape("walk")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 17: #get to work by:
            print("you walked out of the coffee shop.")
            #choice.shape("transportation")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 18: #car / bikes
            print("get to work by..")
            #choice.shape("car")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("bikes")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 20: #enter office:
            if options.index(character.pos()) == 18:
                print("you got to your office by car.")
                for i in range(12):
                    environments.pop(0)
            else:
                print("you rode your bikes to work.")
                for i in range(15):
                    energys.pop(0)
                for i in range(6):
                    healths.append(1)
            #choice.shape("office")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 21: #wow, donuts!:
            print("you got into the office.")
            #choice.shape("donuts")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 22: #eat / not
            print("(packaged) donuts! buy one?")
            #choice.shape("eat")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("no")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 24: #work:
            if options.index(character.pos()) == 22:
                print("you ate a donut.")
                for i in range(8):
                    energys.append(1)
                    healths.pop(0)
                for i in range(4):
                    environments.pop(0)
            else:
                print("you didn't eat a donut.")
            #choice.shape("work")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 25: #eat lunch at:
            print("you worked.")
            for i in range(8):
                energys.pop(0)
            #choice.shape("lunch")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 26: #order in / restaurant
            print("eat lunch at..")
            #choice.shape("restaurant")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("order in")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 28: #back to office:
            if options.index(character.pos()) == 26:
                print("you ate your lunch at a restaurant.")
                for i in range(5):
                    energys.pop(0)
            else:
                print("you ordered in your lunch.")
                for i in range(5):
                    energys.append(1)
                    environments.pop(0)
            #choice.shape("office")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 29: #work:
            print("you entered your office.")
            #choice.shape("work")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 30: #get home:
            print("you kept working.")
            for i in range(8):
                energys.pop(0)
            #choice.shape("home")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 31: #change ac to:
            print("you got home.")
        #choice.shape("ac")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 32: #numbers:
            print("change the ac to...")
            #choice.shape("24")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("19")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("off")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 35: #there are left overs:
            if options.index(character.pos()) == 32:
                print("you set your ac to 24.")
                for i in range(5):
                    environments.pop(0)
            elif options.index(character.pos()) == 33:
                print("you set your ac to 19.")
                for i in range(5):
                    energys.append(1)
                    environments.pop(0)
                    environments.pop(0)
            else:
                print("your ac is off.")
                for i in range(5):
                    healths.pop(0)
        #choice.shape("left overs")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 36: #eat them for dinner?:
            print("eat leftovers for dinner?")
            #choice.shape("leftovers for dinner")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("make something new")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 38: #activity:
            if options.index(character.pos()) == 36:
                print("you ate yesterday's leftovers for dinner.")
                for i in range(6):
                    healths.pop(0)
            else:
                print("you threw away the leftovers and made something new for dinner.")
                for i in range(6):
                    environments.pop(0)
        #choice.shape("activity")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 39: #read / surf online:
            print("spend your evening...")
            #choice.shape("read")
            choice.goto(character.xcor(), character.ycor()+100)
            choice.stamp()
            options.append(choice.pos())
            #choice.shape("surf online")
            choice.goto(character.xcor(), character.ycor()-100)
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 41: #brush teeth:
            if options.index(character.pos()) == 39:
                print("you spent your evening reading.")
                for i in range(6):
                    energys.pop(0)
            else:
                print("you spent your evening surfing online.")
                for i in range(6):
                    environments.pop(0)
        #choice.shape("brush teeth")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 42: #wear pj:
            print("you brushed your teeth.")
        #choice.shape("pj")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 43: #wash face:
            print("you changed to your pjs.")
        #choice.shape("wash face")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 44: #sleep:
            print("you washed your face.")
        #choice.shape("sleep")
            choice.goto(character.xcor()+100, character.ycor())
            choice.stamp()
            options.append(choice.pos())
        elif len(options) == 45: #good night!!
            print("good night!")


    
def up():
    character.goto(character.xcor(),character.ycor()+100)
    choose()

def down(): 
    character.goto(character.xcor(),character.ycor()-100)
    choose()

def right():
    character.goto(character.xcor()+100,character.ycor())
    health.clear()
    energy.clear()
    environment.clear()
    health.forward(100)
    energy.forward(100)
    environment.forward(100)
    health.write("health: " + str(len(healths)))
    energy.write("energy: " + str(len(energys)))
    environment.write("environment: " + str(len(environments)))
    choose()

def left():
    character.goto(character.xcor()-100,character.ycor())
    health.clear()
    energy.clear()
    environment.clear()
    health.backward(100)
    energy.backward(100)
    environment.backward(100)
    health.write("health: " + str(len(healths)))
    energy.write("energy: " + str(len(energys)))
    environment.write("environment: " + str(len(environments)))
    choose()


#listening
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(right,'Right')
turtle.onkeypress(left, 'Left')
turtle.listen()

def finish():
    if len(healths)>=80:
        print('you are super healthy!')
    elif len(healths)>=50:
        print('your health is struggling!')
    elif len(healths)>=10:
        print("")
    else:
        print('you healh suckes!')
        print('you are dying!!!!')
    if len(environments)>=80:
        print('what a green environment that U live in!!!')
    elif len(environments)>=50:
        print('this environment is okay...')
    elif len(environments)>=10:
        print('what a dirty environment!!!')
    if len(energys)>=80:
        print('what a great energy!!')
    elif len(energys)>=50:
        print('your energy is okay...')
    elif len(energys)>=10:
        print('OH your dead!!!')
        print('your energy is tooo low!!')
        

turtle.listen()
turtle.mainloop()
