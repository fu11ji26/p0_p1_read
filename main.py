def on_forever():
    serial.write_value("x", pins.analog_read_pin(AnalogPin.P0))
basic.forever(on_forever)
