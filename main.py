##########################################################
## ADVENTURE GAME STARTS HERE
##########################################################
import random
from adventure import *

# start by creating the game system
game = Game("Escape the Room")

# define and describe a couple of locations
room = game.new_location(
  "a room",
"""a dimly lit room""",
"""You are in a daze with a pounding headache, unaware of how you got here""")

sidewalk = game.new_location(
  "Sidewalk",
"""There is a large glass door to the west.
    The sign says 'Come In!'""", """You get an uneasy feeling""")

vestibule = game.new_location(
  "Vestibule",
"""A small area at the bottom of a flight of stairs.
There is a glass door to the east, and door to the
west. To the north there is a dark muddy hole.""",
    """You get an uneasy feeling""")

# office = game.new_location(
#   "Office",
# """A nicely organized office.
# There is a door to the south.""")
# 
# tunnel = game.new_location(
#   "Tunnel",
# """A dark and moist muddy hole that might lead somewhere...""")

game.new_connection("test", room, vestibule, [IN, WEST], [OUT, EAST])
# game.new_connection("Glass Door", sidewalk, vestibule, [IN, WEST], [OUT, EAST])
# game.new_connection("Office Door", vestibule, office, [IN, WEST], [OUT, EAST])
# game.new_connection("Tunnel Opening", vestibule, tunnel, [DOWN, NORTH], [UP, SOUTH])

# Now let's add a thing, a key, by providing a single word name and a longer
# description.  We will create the key at the sidewalk.
# key = sidewalk.new_object("key", "a small tarnished key")

hairpin = room.new_object("hairpin", "a small, tarnished hairpin")

# And we can make the key required to open the office
# office.make_requirement(key)

# Let's add a special phrase. We can attach this phrase to any object, location or actor,
# and the phrase will trigger only if that object or actor is present or at the given location.
hairpin.add_phrase("bend hairpin", game.say("you bend the hairpin, it now makes a"
                                        "good pick"))

player = game.new_player(room)

game.run()
