# THis is a compass which uses
# the magnometor onboard the sense hat
#

from sense_hat import SenseHat

sense = SenseHat()

while True:
    direction = sense.get_compass()

    if direction < 45 or direction > 315:
        sense.show_letter('N')
    elif direction < 135:
        sense.show_letter('E')
    elif direction < 225:
        sense.show_letter('S')
    else:
        sense.show_letter('W')
