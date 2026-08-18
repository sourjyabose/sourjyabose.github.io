# C# Chapter 3 — Last-Minute Exam Revision

## Question & Answer Format — **High Marks Focus**

I have kept these notes **short, direct, and exam-oriented**, based on your uploaded Chapter 3 material.  

---

## 1. What is Object-Oriented Programming (OOP)?

**Answer:**
OOP is a programming approach that organizes software using **objects rather than functions or procedures**. It helps make programs:

* Modular
* Reusable
* Secure
* Easy to maintain

**Main OOP concepts:**

1. Class
2. Object
3. Abstraction
4. Inheritance
5. Polymorphism
6. Encapsulation

**Exam line:**

> OOP is a programming paradigm that organizes programs using objects containing data and behavior.

---

# CLASS AND OBJECT

## 2. What is a Class?

**Answer:**
A **class** is a **blueprint or template** used to create objects. It defines the **data** and **behavior** of objects.

* Data → Fields/Properties
* Behavior → Methods
* Memory is not occupied by a class until an object is created.

**Example:** `Student` is a class.

---

## 3. What is an Object?

**Answer:**
An **object** is an **instance of a class** representing a real-world entity. It contains:

* Data (properties/fields)
* Behavior (methods)

Memory is allocated when an object is created.

**Example:**
Class → `Car`
Objects → Honda City, Toyota Fortuner

**Syntax:**

```csharp
Student s1 = new Student();
```

---

## 4. Differentiate between Class and Object.

| Class                                         | Object                           |
| --------------------------------------------- | -------------------------------- |
| Blueprint/template                            | Instance of a class              |
| Defines properties and methods                | Uses the properties and methods  |
| Memory is not allocated until object creation | Memory is allocated when created |
| Example: Student                              | Example: s1                      |

---

# ABSTRACTION

## 5. What is Abstraction?

**Answer:**
Abstraction is the process of **hiding internal implementation details** and exposing only the **essential features** of an object.

In C#, abstraction is achieved using:

1. Abstract classes
2. Interfaces

**Real-life example:**
An ATM allows withdrawal of money without showing the internal transaction process.

---

## 6. What are the advantages of Abstraction?

**Answer:**

1. Hides implementation details.
2. Reduces complexity.
3. Improves security.
4. Makes code easier to maintain.
5. Promotes code reusability.
6. Makes applications flexible and scalable.

---

## 7. Which keywords are used for abstraction through an abstract class?

**Answer:**

* `abstract` → Used to declare an abstract class/method.
* `override` → Used to provide implementation in the derived class.

**Example:**

```csharp
abstract class Vehicle
{
    public abstract void Start();
}

class Car : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Car Started");
    }
}
```

---

# INHERITANCE

## 8. What is Inheritance?

**Answer:**
Inheritance is the process by which **one class inherits the properties and methods of another class**.

It promotes:

* Code reusability
* Reduced code duplication

**Syntax:**

```csharp
class Dog : Animal
```

The colon `:` is used for inheritance in C#.

---

## 9. What is a Parent/Base Class and Child/Derived Class?

**Answer:**

### Parent/Base Class

Provides common properties and methods.

### Child/Derived Class

Inherits features from the parent class and can add its own features.

---

## 10. What are the advantages of Inheritance?

**Answer:**

1. Code reusability
2. Reduces code duplication
3. Easy maintenance
4. Improves readability
5. Supports extensibility

---

## 11. What are the types of Inheritance?

**Answer:**

1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance

---

## 12. What is Single Inheritance?

**Answer:**
In single inheritance, **one child class inherits from one parent class**.

```text
Animal
   ↓
 Dog
```

**Example:**

```csharp
class Animal
{
    public void Eat() { }
}

class Dog : Animal
{
    public void Bark() { }
}
```

---

## 13. What is Multilevel Inheritance?

**Answer:**
Multilevel inheritance occurs when one class inherits from another class and a third class inherits from the second class.

```text
Animal
   ↓
 Dog
   ↓
Puppy
```

A `Puppy` can inherit features from both `Dog` and indirectly `Animal`.

---

## 14. What is Hierarchical Inheritance?

**Answer:**
Hierarchical inheritance occurs when **multiple child classes inherit from the same parent class**.

```text
       Animal
       /    \
     Dog    Cat
```

Both `Dog` and `Cat` inherit common features of `Animal`.

---

## 15. What is Multiple Inheritance?

**Answer:**
Multiple inheritance means **one child class inherits from more than one parent class**.

### Is it supported through classes in C#?

**No.**

C# does not support multiple inheritance using classes because it can create ambiguity called the **Diamond Problem**.

---

## 16. How does C# achieve Multiple Inheritance?

**Answer:**
C# achieves multiple inheritance through **interfaces**.

```csharp
class Mobile : ICamera, IMusic
{
    public void Click() { }
    public void PlayMusic() { }
}
```

**Important exam point:**

> C# does not support multiple inheritance through classes but supports it through interfaces.

---

## 17. What is Hybrid Inheritance?

**Answer:**
Hybrid inheritance is a **combination of two or more types of inheritance**, such as multilevel and hierarchical inheritance.

### Is it directly supported using classes in C#?

**No.**

C# supports hybrid inheritance through **interfaces**.

---

# POLYMORPHISM

## 18. What is Polymorphism?

**Answer:**
Polymorphism is an OOP concept that allows **one method or interface to perform different tasks** based on the object or parameters used.

**Poly = Many**
**Morph = Forms**

Therefore:

> **Polymorphism means "one interface, many forms."**

---

## 19. What are the types of Polymorphism?

**Answer:**

1. **Compile-Time Polymorphism** → Method Overloading
2. **Run-Time Polymorphism** → Method Overriding

**⭐ Very important exam question.**

---

## 20. What is Method Overloading?

**Answer:**
Method overloading means creating **multiple methods with the same name but different parameters** in the same class.

Parameters can differ in:

* Number
* Type
* Order

The compiler decides which method to call **during compilation**.

**Example:**

```csharp
public int Add(int a, int b)
{
    return a + b;
}

public int Add(int a, int b, int c)
{
    return a + b + c;
}
```

**Key point:**

> Method Overloading = Compile-Time Polymorphism.

---

## 21. What is Method Overriding?

**Answer:**
Method overriding occurs when a **child class provides its own implementation of a method already defined in the parent class**.

Keywords used:

* `virtual` → Parent class
* `override` → Child class

The method to execute is decided **at runtime**.

**Example:**

```csharp
class Animal
{
    public virtual void Sound()
    {
        Console.WriteLine("Animal makes a sound");
    }
}

class Dog : Animal
{
    public override void Sound()
    {
        Console.WriteLine("Dog barks");
    }
}
```

**Key point:**

> Method Overriding = Run-Time Polymorphism.

---

## 22. Differentiate between Method Overloading and Method Overriding.

| Method Overloading                  | Method Overriding             |
| ----------------------------------- | ----------------------------- |
| Compile-time polymorphism           | Run-time polymorphism         |
| Same method name                    | Same method name              |
| Different parameters                | Same method is reimplemented  |
| Usually in same class               | Parent and child classes      |
| Compiler decides method             | Runtime decides method        |
| No `virtual`/`override` requirement | Uses `virtual` and `override` |

---

# ENCAPSULATION

## 23. What is Encapsulation?

**Answer:**
Encapsulation is the process of **binding data (variables) and methods (functions) into a single unit called a class** and protecting data from unauthorized access.

It is achieved by:

1. Declaring variables as `private`
2. Providing controlled access using `public` methods or properties (`get` and `set`)

**Exam definition:**

> Encapsulation is the process of hiding data and allowing controlled access to it through public methods or properties.

---

## 24. How is Encapsulation achieved in C#?

**Answer:**

```text
Private variable
      ↓
Public method/property
      ↓
Controlled access
```

Example:

```csharp
private string name;

public void SetName(string n)
{
    name = n;
}

public void GetName()
{
    Console.WriteLine(name);
}
```

---

# CONSTRUCTOR

## 25. What is a Constructor?

**Answer:**
A constructor is a **special method of a class automatically called when an object is created**. It is mainly used to initialize object data members.

---

## 26. What are the characteristics of a Constructor?

**Answer:**

1. Has the same name as the class.
2. Has no return type.
3. Is called automatically when an object is created.
4. Is used to initialize object values.

---

## 27. What are the types of Constructors?

**Answer:**

1. Default Constructor
2. Parameterized Constructor
3. Copy Constructor

---

## 28. What is a Default Constructor?

**Answer:**
A default constructor is a constructor **without parameters**.

```csharp
class Student
{
    public Student()
    {
        Console.WriteLine("Constructor is called.");
    }
}
```

---

## 29. What is a Parameterized Constructor?

**Answer:**
A parameterized constructor is a constructor that **takes one or more parameters** and initializes an object with values when it is created.

**Example:**

```csharp
class Student
{
    int id;
    string name;

    public Student(int i, string n)
    {
        id = i;
        name = n;
    }
}
```

Creating the object:

```csharp
Student s1 = new Student(101, "Kanishk");
```

---

## 30. What is a Copy Constructor?

**Answer:**
A copy constructor creates a **new object by copying the values of an existing object**.

**Syntax:**

```csharp
public ClassName(ClassName obj)
{
    // Copy values
}
```

Example:

```csharp
public Student(Student s)
{
    id = s.id;
    name = s.name;
}
```

**Creating a copy:**

```csharp
Student s2 = new Student(s1);
```

---

## 31. Differentiate between Default, Parameterized, and Copy Constructor.

| Type                      | Parameters                   | Purpose                                        |
| ------------------------- | ---------------------------- | ---------------------------------------------- |
| Default Constructor       | No parameters                | Initializes object with default initialization |
| Parameterized Constructor | One or more parameters       | Initializes object with given values           |
| Copy Constructor          | Existing object as parameter | Copies values from an existing object          |

---

# DESTRUCTOR

## 32. What is a Destructor?

**Answer:**
A destructor is a special method automatically called by the **.NET Garbage Collector** when an object is no longer needed. It is used to release resources before the object is removed from memory.

---

## 33. Write the syntax of a Destructor.

```csharp
~ClassName()
{
    // Cleanup code
}
```

---

## 34. What are the characteristics of a Destructor?

**Answer:**

1. Starts with tilde `~`.
2. Has no parameters.
3. Has no return type.
4. Is called automatically by the .NET Garbage Collector.
5. The exact time at which it runs is **not guaranteed**.

**⭐ Important:** Do not write that a destructor runs immediately when the program ends.

---

# INDEXERS

## 35. What is an Indexer?

**Answer:**
An indexer is a special feature in C# that allows an **object to be accessed like an array using the `[]` operator**.

**Syntax:**

```csharp
public string this[int index]
{
    get { return names[index]; }
    set { names[index] = value; }
}
```

Example:

```csharp
s[0] = "Rahul";
Console.WriteLine(s[0]);
```

---

## 36. Which keyword/syntax is specially used for an Indexer?

**Answer:**

```csharp
this[int index]
```

The indexer uses:

* `this`
* `[]`
* `get`
* `set`

---

# DELEGATE

## 37. What is a Delegate?

**Answer:**
A delegate is a **type-safe reference to a method**.

It:

* Stores the address/reference of a method.
* Allows one method to call another method.
* Refers to methods having the same signature.

**Syntax:**

```csharp
delegate void MyDelegate();
```

---

## 38. Give an example of a Delegate.

```csharp
delegate void MyDelegate();

class Program
{
    static void Display()
    {
        Console.WriteLine("Hello from Delegate");
    }

    static void Main()
    {
        MyDelegate d = Display;
        d();
    }
}
```

---

## 39. What are the advantages/uses of Delegates?

**Answer:**

1. Flexible method calling.
2. Supports callback methods.
3. Used in events.

---

# EVENTS

## 40. What is an Event?

**Answer:**
An event is used to **notify when a specific action occurs**.

It is associated with delegates.

**Syntax:**

```csharp
public delegate void MyDelegate();
public event MyDelegate MyEvent;
```

---

## 41. Explain Event with a simple example.

```csharp
delegate void Notify();

class Alarm
{
    public event Notify Ring;

    public void StartAlarm()
    {
        Console.WriteLine("Alarm Started");
        Ring();
    }
}
```

A method can subscribe to the event:

```csharp
a.Ring += Message;
```

When `StartAlarm()` calls `Ring()`, the subscribed `Message()` method executes.

---

# 🔥 ULTRA-SHORT FINAL REVISION

Memorize these **one-line answers** before entering the exam:

### Q. Class?

**A:** Blueprint/template used to create objects.

### Q. Object?

**A:** Instance of a class containing data and behavior.

### Q. Abstraction?

**A:** Hiding implementation details and showing essential features.

### Q. Inheritance?

**A:** A mechanism by which one class inherits properties and methods of another class.

### Q. Polymorphism?

**A:** One interface, many forms.

### Q. Encapsulation?

**A:** Binding data and methods into a class and protecting data through controlled access.

### Q. Compile-time polymorphism?

**A:** Method Overloading.

### Q. Runtime polymorphism?

**A:** Method Overriding.

### Q. Overloading?

**A:** Same method name with different parameters.

### Q. Overriding?

**A:** Child class provides its own implementation of a parent class method.

### Q. Keywords for overriding?

**A:** `virtual` in parent and `override` in child.

### Q. Inheritance symbol in C#?

**A:** Colon `:`.

### Q. Multiple inheritance through classes in C#?

**A:** Not supported.

### Q. How does C# support multiple inheritance?

**A:** Through interfaces.

### Q. Constructor?

**A:** Special method automatically called when an object is created to initialize data members.

### Q. Constructor types?

**A:** Default, Parameterized, Copy.

### Q. Destructor?

**A:** Special method called automatically by the Garbage Collector when an object is no longer needed.

### Q. Destructor symbol?

**A:** `~`

### Q. Indexer?

**A:** Allows an object to be accessed like an array using `[]`.

### Q. Delegate?

**A:** Type-safe reference to a method.

### Q. Event?

**A:** Mechanism used to notify when a specific action occurs.

**Highest-priority topics to prepare:** **OOP pillars, all inheritance types, overloading vs overriding, constructors, destructor, indexer, delegate, and event.**  
