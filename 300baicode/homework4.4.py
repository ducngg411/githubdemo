import turtle as t

def draw_square(length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

for i in range(1, 5):
    draw_square(50 * i)
    t.penup()
    t.forward(60 * i)
    t.pendown()

t.exitonclick()

print()
input("Press return to continue ...")
