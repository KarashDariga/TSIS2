a = set()
a.add(1)
a.add(3)
a.add(2)
a.add(1)
a.add(3)
a.add(10)
a.add("test")
a.add("hello")
a.add("hello")
a.add("test")

a.update([10, 1, 4, 4, 5])

print(a)