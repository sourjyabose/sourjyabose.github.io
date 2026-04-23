# SourjyaBose

---

## ☕ Java Full Last-Minute Revision

Java is a **high-level, object-oriented, platform-independent programming language** developed by Oracle Corporation (originally by Sun Microsystems).

### Features of Java

* Platform Independent (**WORA** → Write Once Run Anywhere)
* Object-Oriented
* Robust
* Secure
* Multithreaded
* Distributed
* Portable
* Architecture Neutral
* Interpreted + Compiled
* High Performance (JIT)

---

# 1. Java Program Structure

```java
class Hello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

### Execution Flow

```text
.java → javac → .class(bytecode) → JVM → Machine code
```

### Components:

* **JDK** → Java Development Kit
* **JRE** → Java Runtime Environment
* **JVM** → Java Virtual Machine

---

# 2. Data Types

## Primitive Data Types

| Type    | Size   | Example |
| ------- | ------ | ------- |
| byte    | 1 byte | 10      |
| short   | 2 byte | 100     |
| int     | 4 byte | 1000    |
| long    | 8 byte | 10000L  |
| float   | 4 byte | 3.14f   |
| double  | 8 byte | 3.14    |
| char    | 2 byte | 'A'     |
| boolean | 1 bit  | true    |

## Non-Primitive

* String
* Array
* Class
* Interface

---

# 3. Variables

```java
int a = 10;        // local
static int b = 20; // static
int c = 30;        // instance
```

---

# 4. Operators

### Arithmetic

`+ - * / %`

### Relational

`< > <= >= == !=`

### Logical

`&& || !`

### Bitwise

`& | ^ ~ << >>`

### Assignment

`= += -= *=`

### Ternary

```java
x>0 ? "Yes":"No";
```

---

# 5. Control Statements

## if / else

```java
if(a>0) {}
else {}
```

## switch

```java
switch(n){
case 1: break;
default:
}
```

## loops

### for

```java
for(int i=0;i<5;i++){}
```

### while

```java
while(x>0){}
```

### do while

```java
do{}while(x>0);
```

---

# 6. Arrays

```java
int arr[] = new int[5];
```

### 2D Array

```java
int a[][] = new int[3][3];
```

### Jagged Array

```java
int a[][] = new int[3][];
```

---


# 7. Strings

A **String** is a sequence of characters.

In Java, String is an **object** of the `String` class.

Example:

```java id="sj5c8l"
String s = "Hello";
```

---

## Features of String

* Immutable
* Stored in String Constant Pool
* Can be created using literal or `new` keyword

Example:

```java id="0fytvx"
String a = "Hi";
String b = "Hi";
```

Both may point to same object.

---

## Why String is Immutable?

### 1. Security

Used in:

* URL
* file path
* database connection

If mutable, these could change unexpectedly.

---

### 2. Memory Optimization

String pool reuses objects.

---

### 3. Thread Safety

Multiple threads can use same string safely.

---

## String vs StringBuffer vs StringBuilder

| Feature     | String | StringBuffer | StringBuilder |
| ----------- | ------ | ------------ | ------------- |
| Mutable     | No     | Yes          | Yes           |
| Thread-safe | Yes    | Yes          | No            |
| Speed       | Slow   | Medium       | Fast          |

---

# 8. OOP Concepts

Java is an **Object-Oriented Programming Language**.

It is based on objects having:

* State
* Behavior
* Identity

Main pillars:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

## Class

Blueprint/template for objects.

Contains:

* variables
* methods
* constructors
* blocks

---

## Object

Instance of class.

Memory allocated when created.

---

## Constructor

Special method called automatically.

Rules:

* same name as class
* no return type

Types:

* Default
* Parameterized
* Copy (manual)

---

## this Keyword

Refers to current object.

Uses:

* current variable
* current method
* current constructor

---

## static Keyword

Belongs to class.

Used with:

* variable
* method
* block
* nested class

---

## final Keyword

Restriction keyword.

* final variable → constant
* final method → cannot override
* final class → cannot inherit

---

# 9. Inheritance

Inheritance means acquiring properties of another class.

Syntax uses `extends`.

---

## Types of Inheritance

### Single Inheritance

Allowed ✅

```text id="x3d1ff"
A → B
```

---

### Multilevel Inheritance

Allowed ✅

```text id="v7du83"
A → B → C
```

---

### Hierarchical Inheritance

Allowed ✅

```text id="m3hjgr"
   A
 / | \
B  C  D
```

---

### Multiple Inheritance

Not allowed through classes ❌

```text id="zc7kkp"
A   B
 \ /
  C
```

Reason:

Diamond Problem / ambiguity.

---

### Hybrid Inheritance

Not fully supported ❌

---

## Achieving Multiple Inheritance

Using interfaces.

```java id="4hm9y8"
class C implements A,B{}
```

Allowed ✅

---

## super Keyword

Used for:

* parent variable
* parent method
* parent constructor

---

# 10. Polymorphism

Means many forms.

---

## Compile-time Polymorphism

Method overloading.

Allowed if changed:

* number
* type
* order of parameters

Not allowed only return type changes ❌

---

## Runtime Polymorphism

Method overriding.

Rules:

* same signature
* inheritance required
* cannot override final method
* cannot override static method

---

# 11. Abstraction

Hiding implementation and showing functionality.

Example:

ATM machine.

---

## Abstract Class

Can have:

✅ abstract methods
✅ normal methods
✅ constructor
✅ static/final methods

Cannot instantiate ❌

---

## Interface

Used for full abstraction.

By default:

Methods → public abstract
Variables → public static final

---

### Interface supports:

Before Java 8:

Only abstract methods.

Java 8:

✅ default methods
✅ static methods

Java 9:

✅ private methods

---

## Allowed / Not Allowed

Interface extends interface ✅

Class implements interface ✅

Class implements multiple interfaces ✅

Class extends class + implements interface ✅

Class extends multiple classes ❌

---

## Abstract Class vs Interface

| Abstract Class      | Interface            |
| ------------------- | -------------------- |
| Partial abstraction | Full abstraction     |
| Constructor allowed | No constructor       |
| Single inheritance  | Multiple inheritance |

---

# 12. Encapsulation

Wrapping data and methods into one unit.

Also called data hiding.

Achieved by:

* private variables
* public getter/setter

Advantages:

* security
* flexibility
* maintenance

---

## Encapsulation vs Abstraction

| Abstraction          | Encapsulation  |
| -------------------- | -------------- |
| hides implementation | hides data     |
| what                 | how protection |

---

# 13. Packages

A package is a group of related classes/interfaces.

Example:

```java id="5v1r0y"
package mypack;
```

---

## Advantages

* avoids naming conflict
* access protection
* better organization

---

## Types

### Built-in Packages

Examples:

* `java.lang`
* `java.util`
* `java.io`
* `java.net`
* `java.sql`
* `java.awt`
* `javax.swing`

---

### User-defined Packages

    Created by programmer.
    To Create Package use `package` keyword
---

## import Keyword

Used to access package classes.

Example:

```java id="vdgh0o"
import java.util.*;
```

---

# 14. Exception Handling

Exception = abnormal condition.

Hierarchy:

Throwable
→ Error
→ Exception

---

## Types

### Checked Exception

Compile-time.

Examples:

* IOException
* SQLException

---

### Unchecked Exception

Runtime.

Examples:

* ArithmeticException
* NullPointerException

---

## Keywords

* try
* catch
* finally
* throw
* throws

---

# 15. Multithreading

Thread = lightweight process.

Advantages:

* multitasking
* better CPU use

---

## Ways to Create

* Thread class
* Runnable interface

---

## Lifecycle

New → Runnable → Running → Waiting → Dead

---

## Synchronization

Avoids race condition.

---

# 16. Collections Framework

Provides ready-made data structures.

---

## List

Ordered, duplicates allowed.

Examples:

* ArrayList
* LinkedList
* Vector
* Stack

---

## Set

No duplicates.

Examples:

* HashSet
* LinkedHashSet
* TreeSet

---

## Queue

FIFO.

Example:

* PriorityQueue

---

## Map

Key-value pairs.

Examples:

* HashMap
* TreeMap

---

## Difference

### ArrayList vs LinkedList

| ArrayList      | LinkedList     |
| -------------- | -------------- |
| Fast access    | Slow access    |
| Slow insertion | Fast insertion |

---

### HashSet vs TreeSet

| HashSet   | TreeSet |
| --------- | ------- |
| Unordered | Sorted  |
| Faster    | Slower  |

---

# 17. Streams (I/O Streams)

Used for input/output.

---

## Byte Stream

Handles binary data.

Examples:

* image
* video
* audio

Classes:

* FileInputStream
* FileOutputStream

---

## Character Stream

Handles text data.

Classes:

* FileReader
* FileWriter
* BufferedReader
* BufferedWriter

---

## Serialization

Object → byte stream.

Deserialization = reverse.

Used for:

* save object
* transfer object

---

# 18. Java 8 Stream API

Different from I/O streams.

Used for collection processing.

Advantages:

* less code
* functional programming
* parallel processing

Methods:

* filter()
* map()
* collect()
* sorted()

---

# 19. Lambda Expression

Anonymous function.

Syntax:

```java id="swg7ea"
(parameters) -> expression
```

Benefits:

* shorter code
* readability

---

# 20. Applets

Small Java programs embedded in browser.

Now deprecated.

---

## Life Cycle of Applet

1. init()
2. start()
3. paint()
4. stop()
5. destroy()

---

# 21. AWT

Abstract Window Toolkit.

Used for GUI.

Features:

* platform dependent
* heavyweight

Components:

* Button
* Label
* TextField
* Frame

---

# 22. Swing

Improved GUI toolkit.

Features:

* lightweight
* platform independent
* richer components

Examples:

* JFrame
* JButton
* JLabel

---

## AWT vs Swing

| AWT           | Swing         |
| ------------- | ------------- |
| Heavyweight   | Lightweight   |
| Less features | More features |

---

# 23. Event Handling

Event = user action.

Examples:

* click
* key press
* mouse move

Uses Delegation Event Model.

Parts:

* Source
* Event
* Listener

---

# 24. JDBC

Java Database Connectivity.

Used to connect Java with database.

Steps:

1. Import package
2. Load driver
3. Create connection
4. Create statement
5. Execute query
6. Close connection

---

## Statement Types

* Statement
* PreparedStatement
* CallableStatement

PreparedStatement prevents SQL Injection.

---

# 25. Garbage Collection

Automatic memory management.

Removes unused objects.

Method:

```java id="a6sbrq"
System.gc();
```

---

This is now actual exam-mode revision.

Read this once and at least 60–70% paper will look familiar.

Your English roast:
“integrate what about other topiics” — bro’s sentence had no package structure, no encapsulation, and multiple inheritance of mistakes.
