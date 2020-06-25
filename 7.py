import turtle as t
import itertools as i
t.shape('turtle')
t.bgcolor('black')
t.speed(0)
colours = i.cycle(['red', 'orange', 'yellow' 'green', 'blue', 'purple', 'grey', 'yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white'])
def draw(size, angle, shift, shape):
     t.pencolor(next(colours))
     next_shape = ''
     if shape == 'circle':
          t.circle(size)
          next_shape = 'square'
     elif shape == 'square':
          for i in range (4):
               t.forward(size * 2)
               t.left(90)
          next_shape = 'circle'
     t.right(angle)
     t.forward(shift)
     draw(size + 2, angle + 1, shift + 1, next_shape)

draw(1, 0, 1, 'circle')
