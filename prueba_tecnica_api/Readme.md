# Parte 4: Consulta a una API Externa


Supón que necesitas consultar la API de una plataforma externa (por ejemplo, Shopify o DHL) desde
Odoo para obtener información sobre el estado de un pedido o un envío.


**Tarea**: Escribe un ejemplo de código en Python que consulte una API REST externa (puede ser la API de
Shopify o DHL) y muestre los detalles de un pedido o un envío.
El ejemplo debe:

1. Hacer una solicitud GET a la API con las credenciales adecuadas (usa un token o clave de API en
   el ejemplo).
2. Manejar la autenticación (por ejemplo, usando un token en el encabezado).
3. Procesar y mostrar la respuesta de la API en la consola o registro de Odoo.

Ejemplo de URL de una API: https://api.dhl.com/myshipment/tracking


Puedes usar datos de ejemplo o simular la solicitud, pero el código debe ser funcional y mostrar cómo
interactuarías con una API externa

---

## Solución (Odoo 16.0)

Se creó un botón en la vista formulario de las órdenes de venta (sale.order), al pulsar el botón, se ejecuta un método que hace una petición a la API "https://api-eu.dhl.com/track/shipments" de DHL para obtener el estatus de envío. Los datos son estácticos en la consulta.

El resultado de la consulta se muestra en los logs de Odoo.
