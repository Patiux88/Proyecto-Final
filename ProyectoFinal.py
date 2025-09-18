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

# Registrar usuario
# Registrar usuario con validación de ID único
def registrar_usuario():
    tipo = input("¿Registrar instructor o estudiante? ").strip().lower()
    if tipo not in ["estudiante", "instructor"]:
        raise ValueError("Tipo de usuario inválido")

    try:
        id = int(input("Ingrese su ID: "))
    except ValueError:
        raise ValueError("Error. El ID debe ser un número entero")

    # Validamos que el id no se repita en estudiantes
    if tipo == "estudiante" and any(isinstance(u, Estudiante) and u.id == id for u in usuarios):
        raise ValueError("Este ID ya está registrado para un estudiante")

    # Validamos que el id no se repita en instructores
    if tipo == "instructor" and any(isinstance(u, Instructor) and u.id == id for u in usuarios):
        raise ValueError("Este ID ya está registrado para un instructor")


    nombre = input("Ingrese su nombre: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")

    if tipo == "estudiante":
        carrera = input("Ingrese su carrera: ").strip()
        if not carrera:
            raise ValueError("La carrera no puede estar vacía")
        usuarios.append(Estudiante(id, nombre, carrera))
    else:
        titulo = input("Ingrese su título: ").strip()
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        usuarios.append(Instructor(id, nombre, titulo))

    print(f" {tipo.capitalize()} '{nombre}' registrado correctamente.")

    #Aquí se utilizan muchos raise ValueError para la eficiencia del código y de esa manera hacer validaciones eficientes y correctas.


# Crear curso con validación de código único y profesor existente
def crear_curso():
    try:
        codigo = int(input("Ingrese código del curso: "))
    except ValueError:
        raise ValueError("Código debe ser un número entero")

    # Validamos que el codigo del curso no se repita ya que es unico con any
    if any(c.codigo == codigo for c in cursos):
        raise ValueError("Este código de curso ya está registrado")

    nombre = input("Ingrese el nombre del curso: ").strip()
    if not nombre:
        raise ValueError("El nombre del curso no puede estar vacío")

    try:
        instructor_id = int(input("Ingrese el ID del docente del curso: "))
    except ValueError:
        raise ValueError("ID del instructor debe ser un número entero")

    # Buscar instructor
    instructor_obj = next((u for u in usuarios if isinstance(u, Instructor) and u.id == instructor_id), None) # Verificamos que el instructor no se repita en el mismo curso dos veces
    if instructor_obj is None:
        raise ValueError("Instructor no encontrado")

    cursos.append(Curso(codigo, nombre, instructor_obj))
    print(f" Curso '{nombre}' creado con instructor {instructor_obj.nombre}.")

    


                            



