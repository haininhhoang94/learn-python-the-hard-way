# Gothons from Planet Percal #25
# Hero has to go through rooms (might not be all of them), and each rooms has
# its own description and tell the engine what room to run next out of the map.
# also, there are scenes too, like Death

# Central Corridor: this is a starting point and has a Gothon already standing
# there, the player have to defeat it with a joke before proceed

# Laser Weapon Armory: this is where the hero gets a neutron bomb to blow up
# the ship before getting to the escape pod. It has a keypad the hero has to
# guess the number for

# The Bridge: this is a battle scene with a Gothon where the hero places the
# bomb

# Escape Pod: this is where the hero escapes but after guessing the right
# escape pod

# Object in this game:
# Alien
# Player - > Creature
# Ship
# Maze
# Room
# Scene
# Gothon -> Creature
# Escape Pod -> Object_
# Planet
# Map
# Engine
# Death
# Central Corridor - Laser Weapon Armory - The Bridge -> Room

# Analyzing the Class:
# 1. Object
# Room, Creature, Death, Object_

# Import necessary
from textwrap import dedent


# 1. Define the Rooms is-a Object
class Room(object):
    def __init__(self, name, dialog):
        self.name = name
        self.dialog = dialog

    def __str__(self) -> str:
        return dedent(
            f"""
                Test the Room object:
                Name: {self.name}
                Dialog: {self.dialog}
                       """
        )


CentralCorridor = Room("CentralCorridor", "Hello")
print(CentralCorridor)
