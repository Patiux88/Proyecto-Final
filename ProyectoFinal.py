from abc import ABC, abstractmethod #Se aplica abstracción

# Listas globales
usuarios = []
cursos = []

# Clase base Usuario
class Usuario(ABC):
    def __init__(self, id, nombre, rol):
        self.__id = id                       #Se aplica encapsulamiento
        self.__nombre = nombre
        self.__rol = rol

    # getters y setters
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def rol(self):
        return self.__rol

    @abstractmethod
    def mostrar_info(self):
        pass

    def __del__(self):
        print(f"Usuario {self.nombre} con ID {self.id} ha sido eliminado.")


# Clase hija Estudiante     #Aquí se aplica herencia
class Estudiante(Usuario):
    def __init__(self, id, nombre, carrera):
        super().__init__(id, nombre, rol="Estudiante")
        self.__carrera = carrera
        self.__cursos = []

    @property
    def carrera(self):
        return self.__carrera

    @property
    def cursos(self):
        return self.__cursos

    def agregar_curso(self, curso):
        self.__cursos.append(curso)

    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Carrera: {self.__carrera}, Cursos: {[c.nombre for c in self.__cursos]}"
    
    def __del__(self):
        print(f"Estudiante {self.nombre} ha sido eliminado.")

# Clase hija Instructor
class Instructor(Usuario):
    def __init__(self, id, nombre, titulo):
        super().__init__(id, nombre, rol="Instructor")
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

    def mostrar_info(self):
        return f"Instructor: {self.nombre}, Título: {self.__titulo}"
    
    def __del__(self):
        print(f"Instructor {self.nombre} ha sido eliminado.")

# Clase Curso
class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__instructor = instructor
        self.__evaluaciones = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def instructor(self):
        return self.__instructor

    @property
    def evaluaciones(self):
        return self.__evaluaciones

    def agregar_evaluacion(self, evaluacion):
        self.__evaluaciones.append(evaluacion)

    def mostrar_info(self):
        return f"Código: {self.__codigo} - Nombre: {self.__nombre} - Instructor: {self.__instructor.nombre}"
    
    def __del__(self):
        print(f"Curso {self.nombre} ha sido eliminado.")

# Clase Evaluacion
class Evaluacion:
    def __init__(self, tipo, ponderacion):
        self.__tipo = tipo
        self.__ponderacion = ponderacion
        self.__calificaciones = {}  # { estudiante_id: nota }

    @property
    def tipo(self):
        return self.__tipo

    @property
    def ponderacion(self):
        return self.__ponderacion

    def registrar_calificacion(self, estudiante_id, nota):
        self.__calificaciones[estudiante_id] = nota

    def obtener_calificacion(self, estudiante_id):
        return self.__calificaciones.get(estudiante_id, None)

    def mostrar_info(self):
        return f"Tipo: {self.__tipo} (Ponderación: {self.__ponderacion}%)"
    
    def __del__(self):
        print(f"Evaluación {self.tipo} ha sido eliminada.")



                            



