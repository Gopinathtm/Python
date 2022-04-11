
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        mark1 = self.m1 + other.m1
        mark2 = self.m2 + other.m2
        total = Student(mark1, mark2)
        return total

    def __gt__(self, other):
        total1 = self.m1 + self.m2
        total2 = other.m1 + other.m2
        if total1 > total2:
            return True
        else:
            return False

    def __str__(self):
        return f"({self.m1}, {self.m2})"


gopi = Student(90, 95)
subin = Student(100, 176)
mani = gopi + subin
print(mani.m1, mani.m2)

if gopi > subin:
    print("Gopi wins")
else:
    print("subin wins")

print(gopi)
print(subin)
print(mani)

"""
Output

190 271
subin wins
(90, 95)
(100, 176)
(190, 271)
"""
