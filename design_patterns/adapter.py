"""
Adapter Pattern
🔧 Practice: Adapt a legacy printer class

Legacy class: OldPrinter with old_print(text)

New interface: NewPrinter.print(text)

Create PrinterAdapter that maps one to the other.

🧠 Bonus: Create a list of both old and new printer objects and treat them uniformly using the adapter.
"""

# Adaptee
class OldPrinter:
    
    def old_print(self, text):
        print(f"Printing from an old printer : {text}")


# Adapter
class PrinterAdapter:

    def __init__(self, old_printers_list : list[OldPrinter]):
        self.old_printers_list = old_printers_list


    def print(self, text):
        print("============ NEW PRINTER ============") # Optionally adding new behaviors along the way
        self.old_printer.old_print(text)

# Target
class NewPrinter(PrinterAdapter):
    pass


old_printer_obj = OldPrinter()
NewPrinter(old_printer=old_printer_obj).print("Hello")