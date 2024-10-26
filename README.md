
# python_basics
## Module 1
## Table of Contents
- [Installation](#installation)
- [Classes](##Classes)
- [Dataclasses](#contributing)
- [License](#license)
- [Contact](#contact)

## installation
```shell
pip install -r requirements.txt
```
## Classes
```
Subclasses:
The class that is the son must contain the parents in the definition class son(mom, dad):
The super().method, calls methods from the parent.
The common use is to use super().__init__ where it calls the  method that loads the attributes created on the parent. 
In summary, while dataclasses do not require super() inherently, you use super() when you need to ensure that methods from parent classes are properly invoked,
particularly in the context of inheritance and custom initialization.

@properties 
• Encapsulation and Control: When you want to encapsulate the internal representation of an attribute and control how it is accessed or modified.
• Read-Only Attributes: When you want to create a read-only attribute that cannot be modified after it is set.
• Computed Properties: When the value of an attribute depends on other attributes and you want to compute it dynamically.
• Validation: When you need to validate the value before setting an attribute.
• Lazy Evaluation: When you want to delay the computation of a property until it is accessed for the first time.

see classes/classes.py
```
## Classes
```
Subclasses:
The class that is the son must contain the parents in the definition class son(mom, dad):
The super().method, calls methods from the parent.
The common use is to use super().__init__ where it calls the  method that loads the attributes created on the parent. 
In summary, while dataclasses do not require super() inherently, you use super() when you need to ensure that methods from parent classes are properly invoked,
particularly in the context of inheritance and custom initialization.

@properties 
• Encapsulation and Control: When you want to encapsulate the internal representation of an attribute and control how it is accessed or modified.
• Read-Only Attributes: When you want to create a read-only attribute that cannot be modified after it is set.
• Computed Properties: When the value of an attribute depends on other attributes and you want to compute it dynamically.
• Validation: When you need to validate the value before setting an attribute.
• Lazy Evaluation: When you want to delay the computation of a property until it is accessed for the first time.

see classes/classes.py
```
