from almacenClases import Product, Person3, Order
from datetime import date


persona = Person3("sergio", "a23sergiopn@iessanclemente.net", "+64-608644411")
productos = []
i = 0
while i < 3:
    productos.append(
        Product(f"Producto {i}", "abcd", 10 + i * 5, f"~/Imágenes/test{i}")
    )
    i += 1

orden = Order(f"{date.today()}", productos, persona)


print(orden)
