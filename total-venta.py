"""
Determinar total de venta.
Si la venta es mayor a 1000, aplicar 5% de descuento.
"""

# Declaraciones
MIN_VENTA_P_DESC = 1000
DESCUENTO = 0.05

# Entradas
cantidad = float(input("¿Cuántos artículos? "))
precio = float(input("Precio unitario: "))

# Proceso
total = cantidad * precio
if total > MIN_VENTA_P_DESC:
    # total = total * (1 - DESCUENTO)
    pass

# Salidas
print("El total es", total)
