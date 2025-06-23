# python-designpatterns

This repository contains simple, easy-to-follow Python implementations of common design patterns.
Each pattern is shown in its own Python file.

---

## Getting Started

1. **To Run the examples directly**

   Each pattern has its own `*.py` file. Execute any of them via:
   ```bash
   python3 design_patterns/singleton.py
   python3 design_patterns/decorator.py
   ```
---

## Design Patterns

Below is a quick summary of each pattern, with a super-easy definition and its category.

| Pattern   | Super-easy Definition / Explanation                                                                   | Category    |
|-----------|--------------------------------------------------------------------------------------------------------|-------------|
| Singleton | Ensures there is only one instance of a class and gives a single, global access point to it.           | Creational  |
| Factory   | Offers a simple way to create objects without knowing the exact class; you just ask the factory to build it. | Creational  |
| AbstractFactory   | Provides an interface for creating families of related objects without specifying their concrete classes. | Creational  |
| Builder   | Separates building a complex object from its parts so you can use the same steps to create different representations. | Creational  |
| Adapter   | Converts one interface into another so that two incompatible interfaces can work together.             | Structural  |
| Facade    | Provides a single, simple interface to a larger body of code (a complex subsystem), hiding all the messy details. | Structural  |
| Decorator | Wraps an object to add new behavior or responsibilities without changing its original code.            | Structural  |
| Proxy     | Acts as a stand-in for another object to control or add extra behavior whenever the real object is accessed. | Structural  |
| Strategy  | Encapsulates interchangeable algorithms or behaviors in separate classes, letting you swap them at runtime. | Behavioral  |
| Observer  | Lets one “subject” object notify several “observer” objects automatically when its state changes.      | Behavioral  |

---

## Running the Examples

Each pattern has its own `*.py` file. Execute any of them via:

```bash
python3 design_patterns/singleton.py
python3 design_patterns/decorator.py
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.