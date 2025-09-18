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

Tabla de responsabilidades

Integrante   Carnet   Tarea Asignada  Evidencia en GitHub   Fecha de Entrega Parcial    Validación Docente
Ángel Rodas 1594125   Desarrollador   commits ya hechos            18/08/2025          
                      Documentador
                      Diseñador

¿Cómo manejaron la herencia y el polimorfismo en su diseño? ¿Qué ventajas les
brindó?
La herencia me permitió manejar con mayor facilidad a los estudiantes y a los instructores ya que heredaban usuario y eso facilito mucho el poder manejar a los instructors y estudiantes con una lista (usuarios).
o ¿Qué estructuras de datos fueron más útiles y por qué?
listas y diccionarios ya que me permitían manejar las calificaciones, los usuarios, cursos y evaluaciones.
o ¿Qué errores comunes anticiparon y cómo los controlaron en el código?
errores como el poner un nombre vacío y usar validación, el manejo correcto de listas y diccionarios, manejar bien los ciclos para recorrer las listas y manejar bien las clases.
o ¿Cómo organizaron su trabajo usando Git y GitHub?
Lo organicé utilizando commits en mi rama principal ya que iba añadiendo los diferentes cambios que hacía de manera ordenada.
o ¿Qué mejoras harían si tuvieran más tiempo?
Verificar más las validaciones, hacerlo mas completo y añadir más funciones para hacer un sistema parecido a un portal académico
▪ Reflejar las dificultades encontradas y cómo las resolvieron.

Las dificultades que encontré fueron principalmente el manejo de errores ya que a veces se me hacía confuso utilizarlo, lo resolví verificando cuidadosamente cada validación.
