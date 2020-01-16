from NumPyCreator import NumPyCreator

npc = NumPyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))

print(npc.from_tuple(("a", "b", "c")))
print(npc.from_iterable(range(5)))
shape = (3, 5)
print("\n", npc.from_shape(shape), "\n")
print(npc.random(shape))

print("\n", npc.identity(4))
