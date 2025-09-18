# Proyecto-Final
PROYECTO No. 1: CASO DE ESTUDIO: PLATAFORMA DE GESTIÓN Y EVALUACIÓN DE CURSOS ONLINE
Sistema de Gestión Académica – Documentación
1. Manual de Usuario

Propósito:
Permite registrar usuarios (estudiantes e instructores), crear cursos, inscribir estudiantes, registrar evaluaciones y calificaciones, y consultar reportes.

Instrucciones para el usuario

Ejecutar el sistema en Python 3:

python sistema.py


Seleccionar opciones del menú:

1: Registrar usuario.

2: Crear curso con un instructor existente.

3: Inscribir estudiante en curso.

4: Crear evaluación para un curso.

5: Registrar calificaciones.

6: Consultar cursos.

7: Consultar estudiantes.

8: Consultar evaluaciones.

9: Consultar calificaciones.

10: Reporte de estudiantes con promedio bajo.

11: Eliminar usuario.

12: Eliminar curso.

13: Mostrar usuarios registrados.

0: Salir del sistema.


Validaciones automáticas:
No se puede registrar un usuario con ID duplicado.
No se puede crear un curso con código duplicado.
Solo el instructor del curso puede registrar calificaciones.
Cada evaluación requiere tipo y ponderación.


2. Explicación Técnica
Conceptos aplicados
Abstracción: Clase Usuario como base de Estudiante e Instructor.
Encapsulamiento: Variables privadas y uso de getters/setters.
Herencia: Estudiante e Instructor heredan de Usuario.
Polimorfismo: Método mostrar_info() sobrescrito en subclases.
Estructuras de control: Ciclos while, condicionales if/elif/else.
Listas: usuarios y cursos para almacenar objetos del sistema.


Flujo del sistema
Registrar usuario o instructor.
Crear cursos vinculados a instructores.
Inscribir estudiantes en cursos.
Crear evaluaciones para los cursos.
Registrar calificaciones por el instructor.
Consultar datos y generar reportes.



