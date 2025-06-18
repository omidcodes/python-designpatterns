'''
Abstract Factory Pattern 
The Abstract Factory pattern provides an interface for creating families of related or dependent objects 
without specifying their concrete classes. 
It allows you to produce families of products that belong together and ensures that
 you use only objects from a single family at a time.

Factory Method vs Abstract Factory :
- Factory Method: delegates creation of a single product to subclasses via an overridden factory method.
- Abstract Factory: provides an interface to create whole families of related products
                   without specifying their concrete classes.

Components:
1. Abstract Products:
2. Concrete Products (Windows):
3. Concrete Products (Mac):
4. Abstract Factory:
5. Concrete Factories:
6. Client code uses only interfaces declared by Abstract Factory and Abstract Products.

'''  

from abc import ABC, abstractmethod

# Abstract Product: Button
class Button(ABC):
    @abstractmethod
    def paint(self) -> None:
        """Render the button on the screen."""
        pass

# Abstract Product: Checkbox
class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> None:
        """Render the checkbox on the screen."""
        pass

# Concrete Product: WindowsButton
class WindowsButton(Button):
    def paint(self) -> None:
        print("Rendering a button in Windows style.")

# Concrete Product: WindowsCheckbox
class WindowsCheckbox(Checkbox):
    def paint(self) -> None:
        print("Rendering a checkbox in Windows style.")

# Concrete Product: MacButton
class MacButton(Button):
    def paint(self) -> None:
        print("Rendering a button in macOS style.")

# Concrete Product: MacCheckbox
class MacCheckbox(Checkbox):
    def paint(self) -> None:
        print("Rendering a checkbox in macOS style.")

# Abstract Factory: GUIFactory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory: WindowsFactory
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory: MacFactory
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client code
def configure_ui(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.paint()
    checkbox.paint()

if __name__ == '__main__':
    # Decide which factory to use at runtime
    for os_name, factory in [('Windows', WindowsFactory()), ('macOS', MacFactory())]:
        print(f"\nConfiguring UI for {os_name}:")
        configure_ui(factory)  # The client code remains the same regardless of the factory
