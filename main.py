screen().fill(8)
screen().set_pixel(80, 60, 1)
screen().draw_line(0, 0, 159, 119, 1)
screen().fill_rect(0, 0, 79, 59, 1)
screen().draw_rect(0, 0, 79, 59, 2)
screen().fill_circle(80, 60, 10, 1)
screen().draw_circle(80, 60, 10, 3)

def on_forever():
    pass
basic.forever(on_forever)
