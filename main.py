def on_button_pressed_a():
    global x
    x = (a * x + b) % c
    basic.show_number(x)
input.on_button_pressed(Button.A, on_button_pressed_a)


a = 59
x = 55
b = 64
c = 100