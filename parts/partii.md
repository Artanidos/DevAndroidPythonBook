# Part II - Basics
## 5. Many Different Approaches 
Because of the fact that Python has been introduced in 1991, meanwhile there are a few approaches to develop Python apps for Android.
There is Tkinter which is a bridge to TK. Tkinter is been delivered with Python. 
There is Kivy which has got a nice approach using a special pythonic language to declare the user interface. 
There is BeeWare which compiles Python to Java-ByteCode. 
There is Enaml Native which act like Pythons answer to React Native and there are a few approaches to bridge to Qt which in pronounced 'Cute'. 
These approaches are PySide, which bridges to Qt4. 
There is PyQt which also bridges to Qt4, PySide2 which bridges to Qt5 and last but not least PyQt5 which we are talking about in this book. 
I am not going to talk about the pros and cons of all these possibilities in this book. Instead I am focusing on solutions. 
To use PyQt5 is a personal decision after working a few years with Qt5. 
Qt5 and PyQt5 are available under an open source license so you might use these frameworks for free as long as you plan to create open source programs. If you are going to create commercial software you have to purchase licenses for both frameworks. 
Even when we using Qt5 we have got two options to develop apps for Android. 
First option is QtWidgets which has been introduced to create platform independent desktops applications and QtQuick which uses a declarative way to implement user interfaces using QML (Qt Markup Language). 
Because at the moment QtQuick lacks of a treeview and a tableview implementation I guess it has been primarily developed to satisfy mobile app development. 
QtQuick has alsk implemented behaviors and transactions which you normally only see on mobile platforms. 
If you have got design background then the QML approach could be your best friend because you don't really have to write code that much and when you like to wrire imperative code then QtWidgets might be your way. 


## 6. Hello World (QtWidgets) 
## 7. Hello World (QtQuick) 
## 8. Deployment  