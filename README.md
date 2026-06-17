# Proyecto Final Python C1 — OdontoCare

## Introducción

El objetivo principal de este proyecto es integrar los distintos contenidos del curso y aplicarlos al desarrollo de una solución backend completa y funcional. Para ello, el estudiante deberá implementar un sistema que combine los siguientes componentes fundamentales:

* **Framework Backend**: Desarrollo de una API REST utilizando Flask, organizada de forma profesional mediante Blueprints para asegurar modularidad y escalabilidad.
* **Persistencia de Datos**: Uso de una base de datos SQLite, gestionada a través de SQLAlchemy como ORM para modelar entidades, relaciones y operaciones CRUD.
* **Seguridad**: Implementación de un mecanismo de autenticación basado en tokens, garantizando el acceso seguro a los distintos recursos del sistema.
* **Cliente Externo**: Creación de un script independiente en Python que consuma los servicios de la API utilizando la biblioteca `requests`, demostrando la correcta interacción entre cliente y servidor.
* **Arquitectura Distribuida y Comunicación entre Servicios**: Creación de imágenes en Docker.

Este objetivo busca consolidar las competencias del nivel C1, permitiendo al estudiante demostrar su capacidad para diseñar, desarrollar e integrar un backend completo con un enfoque profesional.

---

## Escenario del Proyecto

Una red de clínicas dentales ha decidido modernizar sus operaciones creando una aplicación a la medida para gestionar las citas de los pacientes y la disponibilidad de los odontólogos. Actualmente, el sistema se maneja de forma manual, lo que provoca errores frecuentes, duplicidad de información y falta de trazabilidad en los procesos administrativos.

Como desarrollador backend asignado al proyecto, tu misión consiste en diseñar y construir una solución integral, robusta y escalable, que permita cubrir todas las necesidades del nuevo sistema de gestión **OdontoCare**. Para ello, se requiere el desarrollo de una API RESTful profesional, siguiendo buenas prácticas de arquitectura de software, seguridad y persistencia de datos.

El sistema debe permitir la administración eficiente de la información mediante los siguientes módulos esenciales:

* Pacientes
* Doctores
* Centros médicos o clínicas
* Citas médicas

Toda la información gestionada por la API debe persistir en una base de datos confiable. Además, el acceso a los recursos debe estar controlado mediante un mecanismo de autenticación basado en tokens (JWT o similar), garantizando que solo los usuarios autorizados puedan interactuar con los datos.

El formato de comunicación de todos los servicios será exclusivamente **JSON**, por lo que cada endpoint debe responder consistentemente en este formato, tanto en operaciones exitosas como en el manejo de errores.

El estudiante deberá definir y organizar adecuadamente la estructura del proyecto. Adicionalmente, deberá incluir un archivo `requirements.txt` para cada proyecto, en el cual se especifiquen todas las librerías y dependencias necesarias, incorporando aquellas que considere pertinentes para el correcto desarrollo de la actividad.

---

## Objetivos Principales del Sistema

* Diseñar una API RESTful organizada, modular y mantenible.
* Implementar operaciones CRUD para pacientes, doctores, centros y citas.
* Garantizar la persistencia de la información en una base de datos (SQL o NoSQL).
* Incorporar un sistema de autenticación segura por tokens.
* Asegurar que todas las respuestas se entreguen en formato JSON.
* Aplicar buenas prácticas como validación de datos, manejo de excepciones, paginación y documentación básica del API.
* Implementar una arquitectura distribuida basada en contenedores Docker.

---

## Arquitectura de la Solución

Para garantizar un desarrollo ordenado, escalable y alineado con buenas prácticas de ingeniería de software, la API debe implementarse utilizando una arquitectura modular basada en **Blueprints de Flask**. Esto permitirá separar la lógica del sistema por dominios funcionales, facilitando su mantenimiento, comprensión y reutilización.

La solución no debe concentrar todo el código en un solo archivo. En su lugar, se exige una estructura organizada que distribuya la lógica en módulos claros y coherentes. La API deberá estructurarse, como mínimo, con los siguientes componentes:

---

### auth_bp — Autenticación y Gestión de Usuarios

Encargado de todas las operaciones relacionadas con el acceso seguro al sistema. Debe incluir:

* Registro de usuarios autorizados.
* Inicio de sesión mediante validación de credenciales.
* Generación y validación de tokens de autenticación (JWT).
* Manejo de errores de acceso.

Este módulo garantiza que todas las acciones dentro del sistema sean realizadas solo por usuarios autenticados.

---

### admin_bp — Administración y Gestión de Centros, Pacientes y Doctores

Módulo orientado a tareas administrativas, encargado de configurar los elementos base del sistema. Debe incluir:

* Creación de entidades principales: centros médicos, pacientes y doctores.
* Carga de datos, tanto masiva como individual, utilizando archivos en formato JSON cuando sea requerido.
* Opciones de consulta para todos los tipos de registros, permitiendo:

  * Búsqueda individual por ID.
  * Visualización opcional de una lista completa de registros.

Este módulo está diseñado para usuarios con roles administrativos o de gestión.

---

### citas_bp — Gestión Operativa de Citas

Responsable del núcleo funcional de **OdontoCare**: la planificación, administración y control de citas médicas. Debe incluir:

* Creación, actualización, consulta y eliminación de citas.
* Validación de disponibilidad de doctores y centros.
* Reglas operativas para evitar conflictos en la agenda.
* Respuestas en formato JSON con mensajes claros y estructurados.

Este módulo será el más utilizado durante la operación diaria d

**Nota**: El resto de la actividad se encuentra descrito en el enunciado del ejercicio. El estudiante debe leer detenidamente cada uno de los puntos de la actividad para desarrollar correctamente el ejercicio. 

---

## Requisitos de Entrega y Demostración

La entrega final del proyecto no solo incluye el código fuente, sino también la demostración práctica y la evidencia del correcto funcionamiento del sistema basado en microservicios.

---

### Código Funcional (Fork en Git)

El requisito fundamental es la entrega del código fuente completo y funcional.

* **Plataforma**: El código debe estar alojado en un repositorio Git.
* **Contenido**: El repositorio debe incluir todos los componentes del sistema **OdontoCare**, siguiendo la arquitectura distribuida definida, con servicios independientes para **Usuarios/Administración** y **Citas**.
* El estudiante debe desarrollar y presentar un conjunto de scripts que demuestren de forma práctica el funcionamiento de los servicios y su correcta interacción.

---

### Pruebas de Integración (Opcional)

De forma opcional, se pueden incluir o desarrollar pruebas de integración que validen la comunicación entre los distintos servicios y el acceso externo a los endpoints expuestos.

Las pruebas de integración podrán incluir cualquiera de los siguientes métodos:

* Scripts que realicen llamadas directas a los endpoints del servicio (utilizando librerías HTTP o comandos como `curl`).
* Implementación de pruebas unitarias utilizando **unittest** o el módulo **flask.testing**.

---

### Documentación de Pruebas de Endpoints

Se deberá entregar documentación o scripts que incluyan, de forma clara y ordenada, la siguiente información para cada prueba de endpoint realizada:

* **Endpoint utilizado**: Ruta completa del servicio REST.
* **Archivo de entrada**: Cuerpo de la solicitud enviado, obligatoriamente en formato **JSON**.

---

### Video Explicativo

Se requiere una demostración visual, clara y concisa del aplicativo desarrollado.

**Requisitos del video:**

* **Duración máxima**: 5 minutos.
* **Contenido**: Debe evidenciar claramente el funcionamiento completo del aplicativo, incluyendo la interacción entre los microservicios.
* **Funcionamiento**: Mostrar el flujo de trabajo del sistema, desde la inicialización de los servicios hasta la creación de una cita médica, destacando la comunicación RESTful entre los módulos.

