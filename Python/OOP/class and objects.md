## Object
An object is an entity(tangible or intangible) that has well defined structure and behaviour.

In OOP, a program is seen as comprising of a collection of objects, that act on each other.

Each object has a distinct role or responsibility.

## Class
A class is a blueprint of an object.

It defines a set of attributes that characterizes any object that is instantiated from this class.

An object is a realized version of a class. It can also be defined as an abstract datatype.

## Features of Object Oriented Programming
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

### 1. Encapsulation

**Encapsulation** works in OOP by forming a protective barrier around the information contained within a class from the rest of the code. The word “encapsulate” means to enclose something. 

In OOP, we encapsulate by binding the data and functions that operate on that data into a single unit known as the class. This hides private details of a class from the outside world and only exposes functionality important for interfacing with it. 

When a class does not allow calling code access to its private data directly, we say that it is well encapsulated.

**2. Abstraction**

**Abstraction** is a process where you show only “relevant” data and “hide” unnecessary details of an object from the user. 

Consider your mobile phone, you just need to know what buttons are to be pressed to send a message or make a call, What happens when you press a button, how your messages are sent, how your calls are connected is all abstracted away from the user.

**3. Inheritance**

Object-oriented languages that support classes almost always support the notion of **Inheritance**. 

Classes can be organized into hierarchies where a class might have one or more parent or child classes. 

If a class has a parent class, we say it is derived or inherited from the parent class and it represents an “IS-A” type relationship. That is to say, the child class “IS-A” type of the parent class. 

Therefore, if a class inherits from another class, it automatically obtains much of the same functionality and properties from that class and can be extended to contain separate code and data. 

A nice feature of inheritance is that it often leads to good code reuse since a parent class’s functions don’t need to be re-defined in any of its child classes.

**4. Polymorphism**

In OOP, **Polymorphism** allows for the uniform treatment of classes in a hierarchy. 

Therefore, calling code only needs to be written to handle objects from the root of the hierarchy, and any object instantiated by any child class in the hierarchy will be handled in the same way.

In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form.