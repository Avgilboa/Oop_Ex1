from abc import ABC
from time import time

class Human(ABC): ##ABC mean that the class is abstract
    _human_id =111

    def __init__(self, name, age):
        self.id =Human._human_id
        self.name = name
        self.age = age
        Human._human_id+=1


class student(Human):
    def __init__(self, st_name ,age, classes:list):
        super().__init__(st_name,age)
        self.lessons = classes
    def __str__(self):
        return f"The name of the student is : {self.name}, his id is : {self.id} ig age is: {self.age} the lessons: {self.lessons}"
    def add_Class(self, str):
        self.lessons.append(str)
    def __eq__(self, other):
        if not isinstance(other, student):
            return False
        return (self.id==other.id)
    def __hash__(self):   ## we need hash that diffrent and then we can find the methis in O(1)
        return self.id
    def __repr__(self):
        return self.__str__()


def main():
    s1 = student( "Rick",55, ["Math", "oop"])
    s2 = student("Morty",15, ["Math", "oop"])
    s2.add_Class("mavo")
    s1.add_Class("aoutomatic")
    print({s2})
    print([s1, s2])
    print(s2.__repr__())
    print(s1 == s2)
    lst = [s1, s2]
    print(lst)
    lst.sort(key=lambda x: x.name)
    print(lst)



if __name__ == '__main__':
    main()

