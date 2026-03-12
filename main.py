class Human:
    height1 = 180
    height2 = 190
class Student(Human):
    pass
class Worker(Human):
    pass

nick = Student()
jon = Worker()
print(f"Висота {nick.height1}")
print(f"Висота {jon.height2}")