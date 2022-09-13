input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    x = (a * x + b) % c
    basic.showNumber(x)
})
let a = 59
let x = 55
let b = 64
let c = 100
