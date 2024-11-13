# Parte 3: Configuración de un Proceso Logístico

Tu empresa maneja productos a través de múltiples plataformas, y uno de los desafíos es optimizar los
flujos de picking, packing y envío en el almacén. Actualmente, el flujo se gestiona manualmente, pero
deseas automatizarlo en Odoo.


**Tarea**: Describe brevemente cómo configurarías y personalizarías el flujo de trabajo en Odoo para
gestionar automáticamente el proceso de:

1. Picking (selección de productos).
2. Packing (empaquetado).
3. Envío con integración con un sistema de paquetería (por ejemplo, DHL o FedEx).
   No necesitas escribir código para esta tarea, solo describe los pasos principales y las posibles
   personalizaciones.


## Respuesta

1. Primero definir los packing desde el inventario; los diferentes tipos de empaquetados y sus respectivas cantidades.
2. Desde la orden venta, la selección de productos y sus cantidades, al tener 'packings' ya creados, se espera que Odoo automáticamente seleccione el empaquetado correspondiente en relación a la cantidad ingresada, como lo hace de manera estándar.
3. Al confirmar la orden de venta, ejecutar un método que haga un POST a la API para crear un envío de productos:
   1. Definir un apartado para credenciales a esta API.
   2. Crear un diccionario de datos para envío de productos. Se deberá hacer un barrido de todos los productos de la orden de venta para identificar sus precios, medidas, peso y los datos correspondientes que requiere la paquetería
   3. Relizar una petición a través de un método, del cual se deberá guardar en dos nuevos campos de la orden venta; el id de la respuesta para futuras consultas de la transacción y el ID de rastreo del propio envío.
   4. Opcionalmente detonar un envío de correo electrónico, o bien, agregar el ID de rastreo en la plantilla de correo electrónico que se envía al confirmar la cotización.
4. Manejo de errores de la API. Mostrar los errores en el Chatter (a modo de nota para que solo los usuarios internos puedan ver). Esto permitirá conocer cuál ha sido el error en la petición y poder hacer ajustes, de ser necesario.
5. Si existe un error, permitir reintentar crear un envío a través de una solicitud a la paquetería.
