"""
Your friend invites you out to a cool floating pontoon around 1km off the
beach. Among other things, the pontoon has a huge slide that drops you out
right into the ocean, a small way from a set of stairs used to climb out.

As you plunge out of the slide into the water, you see a shark hovering in the
darkness under the pontoon... Crap!

You need to work out if the shark will get to you before you can get to the
pontoon. To make it easier... as you do the mental calculations in the water
you either freeze when you realise you are dead, or swim when you realise
you can make it!
"""


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    dolphin_factor = 0.5 if dolphin else 1
    you_time = pontoon_distance / you_speed
    shark_time = shark_distance / (shark_speed * dolphin_factor)
    return 'Alive!' if you_time < shark_time else 'Shark Bait!'
