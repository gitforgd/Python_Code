class Product:
    id=78
    name="Amul"

    def display(self):
        print(f"Id is {self.id} and name is {self.name}")

class A (Product):
    count=50
    category="Butter"

    def display(self):
        super().display()
        print(f"Count is {self.count} Category is {self.category}")

class B (Product):
    count=90
    category="Milk"

    def display(self):
        super().display()
        print(f"Count is {self.count} Category is {self.category}")

class C (Product):
    count=56
    category="Choco"

    def display(self):
        super().display()
        print(f"Count is {self.count} Category is {self.category}")

a=A()
a.display()
b=B()
b.display()
c=C()
c.display()