# Parte 2: Desarrollo de un Método en Odoo (Python)


Supongamos que tu empresa necesita crear una funcionalidad personalizada en Odoo que envíe
automáticamente una notificación por correo electrónico a un cliente cuando se confirme una orden de
venta. El correo debe incluir un resumen de la orden de venta.


**Tarea**: Desarrolla un método en Python para un modelo Odoo (por ejemplo, sale.order) que realice lo
siguiente:

1. Se dispare cuando se confirme una orden de venta.
2. Recupere la información del cliente y el resumen de la orden.
3. Envíe un correo electrónico al cliente con el resumen de la orden y la fecha tentativa de entrega.
   Puedes utilizar código de ejemplo, pero asegúrate de que esté lo suficientemente completo para mostrar
   tu enfoque de solución


---

## Solución (Odoo 16.0)

Se creó una plantilla de correo electrónico, el cual es enviado cuando se pulsa al botón 'Confirmar' en la Orden de venta.
