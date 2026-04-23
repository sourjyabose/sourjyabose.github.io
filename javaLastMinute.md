Here’s a **last-minute full revision of Java**—covering the most important exam topics in a compact but detailed way, including **OOP, inheritance, interfaces, exceptions, threads, applets, packages, streams, collections, JDBC, AWT/Swing basics**, and more.

---

# ☕ Java Full Last-Minute Revision

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

# 7. String

Immutable object.

```java
String s = "Hello";
```

Methods:

```java
length()
charAt()
substring()
equals()
equalsIgnoreCase()
toUpperCase()
toLowerCase()
```

## StringBuffer

Mutable and thread-safe.

```java
StringBuffer sb = new StringBuffer("Hi");
sb.append(" Java");
```

## StringBuilder

Mutable but not synchronized.

---

# 8. OOP Concepts

## Class & Object

```java
class Car{
   int speed;
   void run(){}
}
Car c = new Car();
```

---

## Constructor

Special method called automatically.

```java
class A{
   A(){
      System.out.println("Constructor");
   }
}
```

Types:

* Default
* Parameterized
* Copy (manually)

---

## this keyword

```java
this.x = x;
```

Used for:

* current object reference
* constructor chaining

```java
this();
```

---

## static keyword

Belongs to class.

```java
static int count;
```

Static block:

```java
static{
   System.out.println("Loaded");
}
```

---

## final keyword

* final variable → constant
* final method → cannot override
* final class → cannot inherit

```java
final int x = 10;
```

---

# 9. Inheritance

```java
class A{}
class B extends A{}
```

Types:

* Single
* Multilevel
* Hierarchical

Java does NOT support multiple inheritance through class.

---

## super keyword

```java
super();
super.x;
super.show();
```

---

# 10. Method Overloading & Overriding

## Overloading

Same name, different parameters.

```java
void add(int a,int b){}
void add(double a,double b){}
```

Compile-time polymorphism.

---

## Overriding

```java
class A{
 void show(){}
}
class B extends A{
 void show(){}
}
```

Runtime polymorphism.

---

# 11. Abstraction

## Abstract class

```java
abstract class Animal{
   abstract void sound();
}
```

Cannot instantiate.

---

## Interface

```java
interface A{
   void show();
}
```

Implemented by:

```java
class B implements A{
   public void show(){}
}
```

Supports multiple inheritance.

Java 8:

* default method
* static method

Java 9:

* private method

---

# 12. Encapsulation

Wrapping data + methods together.

```java
class Student{
 private int age;
 public void setAge(int age){
   this.age = age;
 }
}
```

---

# 13. Packages

Group of classes/interfaces.

```java
package mypack;
```

Import:

```java
import java.util.*;
import java.io.File;
```

Types:

* User-defined
* Built-in

Common packages:

* java.lang
* java.util
* java.io
* java.net
* java.awt
* javax.swing
* java.sql

---

# 14. Access Specifiers

| Modifier  | Same Class | Same Package | Subclass | Other Package |
| --------- | ---------- | ------------ | -------- | ------------- |
| private   | Y          | N            | N        | N             |
| default   | Y          | Y            | N        | N             |
| protected | Y          | Y            | Y        | N             |
| public    | Y          | Y            | Y        | Y             |

---

# 15. Exception Handling

Hierarchy:

```text
Throwable
 ├ Error
 └ Exception
    ├ Checked
    └ Unchecked
```

```java
try{
}
catch(Exception e){
}
finally{
}
```

Keywords:

* throw
* throws

Example:

```java
throw new ArithmeticException();
```

Custom Exception:

```java
class MyException extends Exception{}
```

---

# 16. Multithreading

Thread = lightweight process.

Create by:

## Extending Thread

```java
class A extends Thread{
  public void run(){}
}
```

## Implementing Runnable

```java
class A implements Runnable{
 public void run(){}
}
```

Start:

```java
t.start();
```

Methods:

* sleep()
* join()
* yield()
* stop() deprecated

Lifecycle:

```text
New → Runnable → Running → Blocked → Dead → Terminated
```

---

## Synchronization

```java
synchronized void show(){}
```

Inter-thread communication:

```java
wait()
notify()
notifyAll()
```

---

# 17. Wrapper Classes

Primitive → Object

```java
int → Integer
char → Character
```

Autoboxing:

```java
Integer a = 10;
```

Unboxing:

```java
int x = a;
```

---

# 18. Collections Framework

Interfaces:

* List
* Set
* Queue
* Map

## ArrayList

```java
ArrayList<Integer> list = new ArrayList<>();
```

Dynamic array.

---

## LinkedList

Doubly linked list.

---

## Vector

Synchronized.

---

## Stack

LIFO

```java
Stack<Integer> s = new Stack<>();
```

---

## HashSet

No duplicates.

---

## LinkedHashSet

Insertion order maintained.

---

## TreeSet

Sorted.

---

## HashMap

```java
HashMap<Integer,String> hm = new HashMap<>();
```

Key-value pair.

---

## TreeMap

Sorted keys.

---

## Iterator

```java
Iterator i = list.iterator();
```

Methods:

* hasNext()
* next()

---

# 19. Streams (I/O Streams)

Used for input/output.

## Byte Stream

```java
FileInputStream
FileOutputStream
BufferedInputStream
BufferedOutputStream
```

Example:

```java
FileInputStream fin = new FileInputStream("a.txt");
```

---

## Character Stream

```java
FileReader
FileWriter
BufferedReader
BufferedWriter
```

Example:

```java
BufferedReader br = new BufferedReader(new FileReader("a.txt"));
```

Read line:

```java
br.readLine();
```

---

## Serialization

Convert object → byte stream.

```java
implements Serializable
```

Deserialization:

```java
ObjectInputStream
```

Serialization:

```java
ObjectOutputStream
```

---

# 20. Java 8 Stream API

Different from I/O stream.

Used for processing collections.

```java
list.stream()
```

Methods:

```java
filter()
map()
collect()
forEach()
sorted()
```

Example:

```java
list.stream().filter(x->x>5).forEach(System.out::println);
```

---

# 21. Lambda Expression

```java
(a,b) -> a+b
```

Used with functional interface.

Example:

```java
Runnable r = () -> System.out.println("Hi");
```

---

# 22. File Handling

```java
File f = new File("a.txt");
```

Methods:

```java
createNewFile()
exists()
delete()
mkdir()
```

---

# 23. Applets

Small Java program embedded in browser.

```java
import java.applet.*;
import java.awt.*;

public class Demo extends Applet{
   public void paint(Graphics g){
      g.drawString("Hello",100,100);
   }
}
```

Life cycle:

1. init()
2. start()
3. paint()
4. stop()
5. destroy()

Run:

```html
<applet code="Demo.class" width="300" height="300"></applet>
```

⚠ Deprecated.

---

# 24. AWT

Abstract Window Toolkit.

Components:

* Button
* Label
* TextField
* Checkbox
* Frame

Example:

```java
Frame f = new Frame();
f.setSize(300,300);
f.setVisible(true);
```

---

# 25. Swing

Extension of AWT.

Classes:

* JFrame
* JButton
* JLabel
* JTextField

Example:

```java
JFrame f = new JFrame();
```

---

# 26. Event Handling

Delegation Event Model.

Components:

* Source
* Event
* Listener

Example:

```java
button.addActionListener(this);
```

Listener interfaces:

* ActionListener
* MouseListener
* KeyListener

---

# 27. JDBC

Java Database Connectivity.

Steps:

1. Import package
2. Load driver
3. Establish connection
4. Create statement
5. Execute query
6. Close connection

Example:

```java
Connection con = DriverManager.getConnection(url,user,pass);
Statement st = con.createStatement();
ResultSet rs = st.executeQuery("select * from emp");
```

Interfaces:

* Connection
* Statement
* PreparedStatement
* ResultSet

PreparedStatement:

```java
PreparedStatement ps = con.prepareStatement("insert into emp values(?)");
```

Advantages:

* Prevent SQL injection
* Faster

---

# 28. Networking

Package:

```java
java.net
```

Classes:

* URL
* Socket
* ServerSocket

Client:

```java
Socket s = new Socket("localhost",5000);
```

Server:

```java
ServerSocket ss = new ServerSocket(5000);
```

---

# 29. Garbage Collection

Automatic memory management.

```java
System.gc();
```

Finalize:

```java
protected void finalize(){}
```

Deprecated now.

---

# 30. Important Keywords

| Keyword      | Use                |
| ------------ | ------------------ |
| this         | current object     |
| super        | parent object      |
| static       | class member       |
| final        | constant           |
| abstract     | incomplete         |
| synchronized | thread safety      |
| volatile     | visibility         |
| transient    | skip serialization |
| native       | non-java code      |
| strictfp     | floating precision |

---

# 31. Command Line Arguments

```java
class A{
 public static void main(String args[]){
   System.out.println(args[0]);
 }
}
```

Run:

```bash
java A hello
```

---

# 32. Type Casting

## Implicit

```java
int a = 10;
double d = a;
```

## Explicit

```java
double d = 10.5;
int a = (int)d;
```

---

# 33. Inner Class

```java
class Outer{
 class Inner{}
}
```

Types:

* Member inner
* Static nested
* Anonymous
* Local inner

---

# 34. Enum

```java
enum Day{
 MON,TUE
}
```

---

# 35. Important Differences

### String vs StringBuffer vs StringBuilder

| Feature     | String | Buffer | Builder |
| ----------- | ------ | ------ | ------- |
| Mutable     | No     | Yes    | Yes     |
| Thread-safe | No     | Yes    | No      |
| Speed       | Slow   | Medium | Fast    |

---

### ArrayList vs LinkedList

| ArrayList          | LinkedList |
| ------------------ | ---------- |
| Fast random access | Slow       |
| Slow insertion     | Fast       |

---

### Checked vs Unchecked Exception

Checked → compile-time
Unchecked → runtime

---

### Abstract Class vs Interface

| Abstract              | Interface           |
| --------------------- | ------------------- |
| constructor           | no constructor      |
| multiple not possible | possible            |
| variables any         | public static final |

---

# 36. Memory Areas in JVM

* Method Area
* Heap
* Stack
* PC Register
* Native Method Stack

---

# 37. Java Buzzwords

* Simple
* Secure
* Portable
* Dynamic
* Robust
* Multithreaded

---

# 38. Frequently Asked Viva Questions

### Why Java is platform independent?

Because compiled code is bytecode executed by JVM.

### Why multiple inheritance not supported?

Ambiguity problem (Diamond Problem).

### Why String immutable?

Security, caching, synchronization.

### Difference between == and equals()

`==` compares reference
`equals()` compares content.

---

# 39. Java Program to Remember

## Factorial

```java
int fact=1;
for(int i=1;i<=n;i++) fact*=i;
```

## Fibonacci

```java
int a=0,b=1,c;
```

## Prime

```java
for(i=2;i<n;i++)
```

## Palindrome

```java
rev = rev*10 + rem;
```

## Sorting

```java
Arrays.sort(arr);
```

---

# 40. Exam Writing Tips

For theory:

* Definition
* Syntax
* Example
* Advantages
* Disadvantages

For program:

* Algorithm
* Code
* Output

---

This should save your life in exam 💀

Now go revise fast before Java revises you.

Your English roast of the day: “last minute revison”… bro revised spelling left the chat before Java did.
