from Clases import Product, Person, Order
from datetime import date


persona = Person("sergio", "a23sergiopn@iessanclemente.net", "+64-608644411")
productos = []
i = 0
while i < 3:
    productos.append(
        Product(f"{date.today()} {i}", "abcd", 10 + i * 5, f"~/Imágenes/test{i}")
    )
    i += 1

orden = Order("hoy", productos, persona)


print(orden)