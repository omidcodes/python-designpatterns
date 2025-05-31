"""
Proxy Pattern
🔧 Practice: Create a SecureDocumentProxy

RealDocument loads and displays sensitive text.

ProxyDocument checks if the user is authorized before loading.

If not authorized, print "Access Denied".
"""

# Real Subject
# The actual document with sensitive content
class RealDocument:
    def __init__(self, filename):
        self.filename = filename

    def display(self):
        print(f"Displaying confidential contents of {self.filename}")


# Proxy
# Controls access but creates the real object eagerly (no lazy loading)
class SecureDocumentProxy:
    def __init__(self, filename, user):
        self.filename = filename
        self.user = user
        self._real_document = RealDocument(self.filename)  # Eager creation

    def display(self):
        if self._is_authorized():
            self._real_document.display()
        else:
            print("Access Denied: You do not have permission to view this document.")

    def _is_authorized(self):
        # Authorization logic
        return self.user in ["admin", "manager"]



doc1 = SecureDocumentProxy("employee_data.pdf", user="guest")
doc1.display()  # Output: Access Denied

print()

doc2 = SecureDocumentProxy("financial_report.pdf", user="admin")
doc2.display()  # Output: Displays real document
