'''

Here are a few examples of how we might use a class:

    - Say we wanted to model a student in a course. We could have a Student
      class that has instance variables for name, emailAddress, currentGrade,
      and so on. Each Student object we create from this class would have its
      own set of these instance variables, and the values given to the instance
      variables would be different for each student.

    - Consider a game where we have multiple players. A player could be
      modeled by a Player class with instance variables for name, points,
      health, location, and so on. Each player would have the same
      capabilities, but the methods could work differently based on the
      different values in the instance variables.

    -  Imagine an address book. We could create a Person class with instance
       variables for name, address, phoneNumber, and birthday. We could create
       as many objects from the Person class as we want, one for each person
       we know. The instance variables in each Person object would contain
       different values. We could then write code to search through all the
       Person objects and retrieve information about the one or ones we are
       looking for.

OOP as a Solution:

    1.  A well-written class can be easily reused in many different programs.
        Classes do not need to access global data. Instead, objects provide
        code and data at the same level.

    2.  Object-oriented programming can greatly reduce the number of global
        variables required, because a class provides a framework in which data
        and code that acts on the data exist in one grouping. This also tends
        to make code easier to debug.

    3.  Objects created from a class only have access to their own data—their
        set of the instance variables in the class. Even when you have multiple
        objects created from the same class, they do not have access to each
        other's data.

Summary:

    The class defines the shape and capabilities of an object. An object is a
    single instance of a class that has its own set of all the data defined
    in the instance variables of the class. Each piece of data you want an
    object to contain is stored in an instance variable, which has object
    scope, meaning that it is available within all methods defined in the
    class. All objects created from the same class get their own set of all
    the instance variables, and because these may contain different values,
    calling the methods on different objects can result in different behavior.
    Create an object from a class, typically through an assignment statement.
    After instantiating an object, you can use it to make calls to any method
    defined in the class of that object. Also is possible instantiate multiple
    object from a class.

'''
