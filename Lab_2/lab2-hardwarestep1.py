from sense_hat import SenseHat

sense = SenseHat()
state = 1

while True:
    events = sense.stick.get_events()
    if events:
        for event in events:
            if event.action != 'pressed':
                # this is a hold or key up; move on
                continue
            if event.direction == 'left':
                if state == 1:
                    sense.show_letter("N")
                    state = 2
                elif state == 2:
                    sense.show_letter("F")
                    state = 1
            elif event.direction == 'right':
                if state == 1:
                    sense.show_letter("N")
                    state = 2
                elif state == 2:
                    sense.show_letter("F")
                    state = 1
            elif event.direction == 'up':
                if state == 1:
                    sense.show_letter("N")
                    state = 2
                elif state == 2:
                    sense.show_letter("F")
                    state = 1
            elif event.direction == 'down':
                if state == 1:
                    sense.show_letter("N")
                    state = 2
                elif state == 2:
                    sense.show_letter("F")
                    state = 1
