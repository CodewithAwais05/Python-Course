# Lecture 8: Object-Oriented Programming (OOP) in Python

## 📋 Overview
This chapter introduces **Object-Oriented Programming** in Python — a paradigm that maps real-world scenarios into code using classes and objects. It covers class/instance attributes, constructors, methods, static methods, inheritance, and the core OOP principles of abstraction and encapsulation.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Explain what OOP is and why it's used
- Create classes and instantiate objects
- Differentiate between class attributes and instance attributes
- Use the `__init__()` constructor to initialize objects
- Define and call instance methods
- Define static methods using the `@staticmethod` decorator
- Explain abstraction and encapsulation
- Understand inheritance and its three types: Single, Multiple, and Multilevel

---

## 📚 Topics Covered

### 1. OOP in Python
To map real-world scenarios into code, we use **objects** — this approach is called **Object-Oriented Programming**.

### 2. Class & Object in Python
A **class** is a blueprint for creating objects.

```python
# creating class
class Student:
    name = "karan kumar"

# creating object (instance)
s1 = Student()
print(s1.name)
```

### 3. Class & Instance Attributes
```python
Class.attr    # class-level attribute
obj.attr      # instance-level attribute
```

### 4. `__init__()` Function (Constructor)
Every class has a function called `__init__()`, which runs automatically whenever an object is created.

```python
class Student:
    def __init__(self, fullname):
        self.name = fullname

# creating object
s1 = Student("karan")
print(s1.name)
```
> 💡 The `self` parameter refers to the current instance of the class and is used to access variables that belong to it.

### 5. Methods
Methods are functions that belong to objects.

```python
class Student:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print("hello", self.name)

s1 = Student("karan")
s1.hello()      # hello karan
```

### 6. Static Methods
Methods that don't use the `self` parameter — they operate at the class level rather than the instance level.

```python
class Student:
    @staticmethod          # decorator
    def college():
        print("ABC College")
```
> 💡 Decorators wrap another function to extend its behavior without permanently modifying it.

### 7. Inheritance
Inheritance allows one class (**child/derived class**) to acquire the properties and methods of another class (**parent/base class**), promoting code reuse.

```python
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):     # Child inherits from Parent
    pass

c = Child()
c.show()      # This is the parent class (inherited method)
```

#### Types of Inheritance

**1. Single Inheritance**
A child class inherits from only **one** parent class.

```python
class Animal:
    def eat(self):
        print("This animal eats food")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

d = Dog()
d.eat()     # inherited from Animal
d.bark()    # defined in Dog
```

**2. Multiple Inheritance**
A child class inherits from **more than one** parent class.

```python
class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def hobbies(self):
        print("Mother: Painting")

class Child(Father, Mother):     # inherits from both classes
    pass

c = Child()
c.skills()      # from Father
c.hobbies()     # from Mother
```

**3. Multilevel Inheritance**
A class inherits from a child class, forming a **chain** of inheritance (grandparent → parent → child).

```python
class Grandparent:
    def house(self):
        print("Has a house")

class Parent(Grandparent):
    def car(self):
        print("Has a car")

class Child(Parent):
    def bike(self):
        print("Has a bike")

c = Child()
c.house()    # inherited from Grandparent
c.car()      # inherited from Parent
c.bike()     # defined in Child
```

| Type | Description |
|---|---|
| **Single Inheritance** | One child class inherits from one parent class |
| **Multiple Inheritance** | One child class inherits from more than one parent class |
| **Multilevel Inheritance** | A class inherits from a child class, forming a chain across generations |

### 8. Core OOP Concepts

**Abstraction**
Hiding the implementation details of a class and only exposing the essential features to the user.

**Encapsulation**
Wrapping data and functions into a single unit (object).

---

## 💻 Practice Exercises
1. Create a `Student` class that takes name & marks of 3 subjects as arguments in the constructor. Create a method to print the average.
2. Create an `Account` class with 2 attributes — `balance` and `account_no`. Create methods for debit, credit, and printing the balance.
3. Create a `Vehicle` class with a method `move()`. Create a `Car` class that inherits from `Vehicle` (single inheritance) and adds its own method `honk()`.
4. Create `Engine` and `Battery` classes, then create an `ElectricCar` class that inherits from both (multiple inheritance).
5. Create a `Person` class, a `Teacher` class that inherits from `Person`, and a `PrincipalTeacher` class that inherits from `Teacher` (multilevel inheritance).

---

## 🔑 Key Takeaways
- A class is a blueprint; an object is an instance created from that blueprint.
- `__init__()` runs automatically on object creation and is used to set up initial state.
- Static methods belong to the class itself, not to any particular instance, and don't use `self`.
- Inheritance lets a child class reuse a parent class's properties and methods — the three common types are **Single**, **Multiple**, and **Multilevel** inheritance.
- Abstraction hides complexity; encapsulation bundles data and behavior together.