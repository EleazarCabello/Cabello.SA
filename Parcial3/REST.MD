# Restricciones Rest #

REST (Representational State Transfer) es un estilo arquitectónico utilizado para diseñar servicios web. Se basa en un conjunto de restricciones que deben seguirse para crear una arquitectura web que sea escalable, confiable y compatible con el estado de Internet. Estas restricciones, propuestas por Roy Fielding en su tesis doctoral, ayudan a definir las características y comportamientos de una aplicación web basada en REST.

A continuación, se presentan las principales restricciones REST:

1. Arquitectura cliente-servidor
La arquitectura cliente-servidor es fundamental en REST. Establece una separación clara entre el cliente, que solicita recursos, y el servidor, que los proporciona. El cliente y el servidor pueden evolucionar de forma independiente, lo que permite una mayor flexibilidad y escalabilidad.

2. Sin estado (stateless)
REST es sin estado, lo que significa que cada solicitud del cliente al servidor debe contener toda la información necesaria para comprenderla. El servidor no debe mantener ningún estado de sesión entre solicitudes. Cada solicitud se procesa de forma aislada, lo que facilita la escalabilidad y la recuperación de errores.

3. Interfaz uniforme
La interfaz uniforme es una restricción fundamental en REST. Proporciona una forma consistente de interactuar con los recursos a través de una serie de restricciones:

Identificación de recursos: Cada recurso debe tener un identificador único (URI) que lo distinga de otros recursos.
Manipulación de recursos a través de representaciones: Los clientes manipulan los recursos a través de la representación de los mismos. Por ejemplo, utilizando XML o JSON.
Mensajes autoexplicativos: Cada mensaje debe incluir suficiente información para que el receptor lo comprenda. Esto puede lograrse mediante el uso de encabezados HTTP adecuados.
Hipertexto como motor de la aplicación: La aplicación debe usar enlaces hipertextuales para permitir la navegación y descubrimiento de recursos relacionados.
4. Sistema de capas
REST permite la inclusión de capas intermedias, como servidores proxy o sistemas de caché, entre el cliente y el servidor. Estas capas pueden mejorar la eficiencia, la escalabilidad y la seguridad del sistema.

5. Sistema de caché
REST admite el uso de caché para reducir la latencia y mejorar el rendimiento. Los servidores pueden indicar si una respuesta puede ser almacenada en caché por el cliente, lo que evita la necesidad de realizar solicitudes adicionales al servidor en el futuro.

6. Sistema de código bajo demanda (opcional)
Esta restricción es opcional en REST. Permite que el servidor envíe código ejecutable al cliente, como JavaScript, para extender su funcionalidad. Sin embargo, esta restricción no es ampliamente utilizada en aplicaciones REST modernas.

Al adherirse a estas restricciones, los servicios web REST pueden aprovechar los principios de escalabilidad, confiabilidad, rendimiento y simplicidad, lo que los convierte en una opción popular para la creación de API y servicios web en la actualidad.

