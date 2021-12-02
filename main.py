def on_button_pressed_a():
    global on
    if on == 0:
        pins.digital_write_pin(DigitalPin.P0, 1)
        on = 1
    if on == 1:
        pins.digital_write_pin(DigitalPin.P0, 0)
        on = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

on = 0
pins.digital_write_pin(DigitalPin.P0, 0)
on = 0