my_list = [10, 20, 30, 40, 50]

print("List:", my_list)
print("Length:", len(my_list))
print("First Element:", my_list[0])

my_list.append(60)
my_list.insert(1, 15)
my_list.remove(30)
my_list.pop()
my_list.extend([70, 80])
my_list.sort()
my_list.reverse()

print("Updated List:", my_list)

my_tuple = (1, 2, 3, 4, 5)

print("\nTuple:", my_tuple)
print("Length:", len(my_tuple))
print("First Element:", my_tuple[0])
print("Count of 2:", my_tuple.count(2))
print("Index of 4:", my_tuple.index(4))

my_set = {10, 20, 30, 40}

print("\nSet:", my_set)

my_set.add(50)
my_set.update([60, 70])
my_set.remove(20)
my_set.discard(100)

another_set = {40, 50, 80, 90}

print("Union:", my_set.union(another_set))
print("Intersection:", my_set.intersection(another_set))
print("Difference:", my_set.difference(another_set))
print("Symmetric Difference:", my_set.symmetric_difference(another_set))
print("Updated Set:", my_set)