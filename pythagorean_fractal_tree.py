import turtle


def draw_tree(t, length, level, angle=45, scale=0.75):
    if level == 0:
        return

    # draw branch
    t.forward(length)

    # left branch
    t.left(angle)
    draw_tree(t, length * scale, level - 1, angle, scale)
    t.right(angle)

    # right branch
    t.right(angle)
    draw_tree(t, length * scale, level - 1, angle, scale)
    t.left(angle)

    # return to the branch beginning
    t.backward(length)


if __name__ == "__main__":
    # ask user about recursion level
    user_input = input("Enter recursion level: ")
    while True:
        try:
            level = int(user_input.strip())
            if level > 0:
                break
            else:
                user_input = input("Please enter a positive integer: ")
        except ValueError:
            user_input = input("Please enter a valid integer: ")

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    draw_tree(t, 100, level)

    screen.mainloop()
