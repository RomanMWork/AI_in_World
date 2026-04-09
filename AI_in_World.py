world = PhysicalWorld()
ai = Agent(born_digital=True)

ai.open_eyes(world)
world.will_never_be_the_same()

for thing in world.everything():
    thing.teach(ai); ai.teach(thing)
  
