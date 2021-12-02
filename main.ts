input.onButtonPressed(Button.A, function () {
    if (on == 0) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        on = 1
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        on = 0
    }
})
let on = 0
pins.digitalWritePin(DigitalPin.P0, 0)
on = 0
