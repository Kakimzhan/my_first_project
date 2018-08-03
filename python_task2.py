import turtle
import time
start_time = time.time()
turtle.color('violet','red')
for i in range(5):
    turtle.color('violet','red')
    turtle.begin_fill()
    turtle.forward(150)
    turtle.right(144) 
    turtle.end_fill()
    #print (turtle.speed)
print("The time spent on drawing a star is %s seconds " % (time.time() - start_time))
turtle.done()







     


