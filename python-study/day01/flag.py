
import turtle

def draw_rectangle(x,y,width,height):
    turtle.goto(x,y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def main():
    turtle.speed(12)
    turtle.penup()
    draw_rectangle(100,0,540,360)
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口
    turtle.mainloop()

if __name__ == '__main__':
    main()