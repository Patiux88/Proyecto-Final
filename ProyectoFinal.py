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

    
#Inscribir estudiantes
def inscribir_estudiantes():
    nombre = input("Ingrese el nombre del estudiante que desea inscribir \n").lower().strip()
    try:
        codigo = int(input("Ingrese el código del curso en el que va a ser inscrito \n"))
    except ValueError:
        print("Error: el código del curso debe ser un número entero.")
        return

    # Buscamos curso
    curso_encontrado = next((curso for curso in cursos if curso.codigo == codigo), None)

    if not curso_encontrado:
        print("No se encontró un curso con ese código.")
        return

    # Buscamos estudiante por nombre
    estudiante_encontrado = next((usuario for usuario in usuarios if isinstance(usuario, Estudiante) and usuario.nombre.lower().strip() == nombre), None)
    #next permite buscar el primer curso cuyo código coincida con codigo para que no se repita
    if not estudiante_encontrado:
        print("No se encontró un estudiante con ese nombre.")
        return

    # Verificamos si ya está inscrito en ese curso el estudiante
    if curso_encontrado in estudiante_encontrado.cursos:
        print(f"El estudiante {estudiante_encontrado.nombre} ya está inscrito en el curso {curso_encontrado.nombre}.")
        return

    # Inscribimos al estudiante
    estudiante_encontrado.cursos.append(curso_encontrado)
    print(f"Estudiante {estudiante_encontrado.nombre} ha sido inscrito en el curso {curso_encontrado.nombre} exitosamente.")

# Crear evaluaciones
def crear_evaluaciones():
    tipo = input("Ingrese el tipo de evaluación que desea crear: \n").lower().strip()
    ponderacion = int(input("Ingrese la ponderación de la evaluación: \n"))
    evaluacion = Evaluacion(tipo, ponderacion)

    codigo = int(input("Ingrese el código del curso en el que desea crear una evaluación: \n"))

    # Buscar curso
    curso_encontrado = None
    for curso in cursos:
        if codigo == curso.codigo:
            curso_encontrado = curso
            break

    if curso_encontrado:
        curso_encontrado.agregar_evaluacion(evaluacion)
        print(f"Evaluación {tipo} agregada al curso {curso_encontrado.nombre}")
    else:
        print("No se encontró un curso con ese código.")

# Registrar calificaciones
def registrar_calificaciones():
    try:
        instructor_id = int(input("Ingrese su id de instructor: "))
        # Buscar instructor
        instructor_encontrado = None
        for u in usuarios:
            if isinstance(u, Instructor) and u.id == instructor_id:
                instructor_encontrado = u
                break

        if instructor_encontrado:
            print(f"Bienvenido al registro de calificaciones, instructor: {instructor_encontrado.nombre}")
            codigos = []

            # Mostrar cursos del instructor
            for curso in cursos:
                if curso.instructor == instructor_encontrado:
                    print(curso.mostrar_info())
                    codigos.append(curso.codigo)

            codigo = int(input("Elija el código del curso en el que desea registrar una calificación: "))

            if codigo in codigos:
                curso_seleccionado = None
                for curso in cursos:
                    if curso.codigo == codigo:
                        curso_seleccionado = curso
                        break

                if curso_seleccionado:
                    # Mostrar evaluaciones del curso
                    tipos = []
                    for e in curso_seleccionado.evaluaciones:
                        print(e.mostrar_info())
                        tipos.append(e.tipo)

                    evaluacion_tipo = input("Elija el tipo de evaluación que desea calificar: ").lower().strip()

                    if evaluacion_tipo in tipos:
                        evaluacion_obj = None
                        for e in curso_seleccionado.evaluaciones:
                            if e.tipo == evaluacion_tipo:
                                evaluacion_obj = e
                                break

                        # Mostrar estudiantes inscritos
                        estudiantes_inscritos = [u for u in usuarios if isinstance(u, Estudiante) and curso_seleccionado in u.cursos]

                        if estudiantes_inscritos:
                            for i, est in enumerate(estudiantes_inscritos, start=1):
                                print(f"{i}. {est.mostrar_info()}")

                            num_est = int(input("Elija el número del estudiante al que desea calificar: ")) - 1

                            if 0 <= num_est < len(estudiantes_inscritos):
                                estudiante_seleccionado = estudiantes_inscritos[num_est]
                                calificacion = float(input("Ingrese la calificación: "))
                                evaluacion_obj.registrar_calificacion(estudiante_seleccionado.id, calificacion)
                                print(f" Calificación registrada para {estudiante_seleccionado.nombre} en {evaluacion_obj.tipo}.")
                            else:
                                print("Número de estudiante inválido.")
                        else:
                            print("No hay estudiantes inscritos en este curso.")
                    else:
                        print("Tipo de evaluación no válido.")
            else:
                print("No se encontró un curso con ese código.")
        else:
            print("Instructor no encontrado.")

    except ValueError:
        print("Error. Debe ingresar un valor numérico.")

#Mostrar usuarios
def mostrar_usuarios():
    #Se usa polimorfismo ya que La lista usuarios puede tener tanto Estudiantes como Instructores.
    #Ambos heredan de Usuario y sobrescriben el método mostrar_info()
    if len(usuarios)==0:
        print("No existen usuarios registrados")
    else:
        for u in usuarios:
            print(u.nombre)
    
# Consultar cursos
def consultar_cursos():
    if len(cursos)==0:
        print("No existen cursos creados")
    else:
        for curso in cursos:
            print(curso.mostrar_info())

# Consultar estudiantes inscritos
def consultar_estudiantes():
    estudiantes_inscritos=[u for u in usuarios if isinstance(u, Estudiante)]
    if len(estudiantes_inscritos)==0:
        print("No hay estudiantes escritos")
    else:
        for e in estudiantes_inscritos:
            print(e.mostrar_info())

# Consultar evaluaciones por cursos
def consultar_evaluaciones():
    if len(cursos)==0:
        print("No existen cursos creados")
    else:
        for i, curso in enumerate(cursos, start=1):
            print(f"{i}. {curso.mostrar_info()}")
            for j, e in enumerate(curso.evaluaciones, start=1):
                print(f"    {j}. {e.mostrar_info()}")
        
# Consultar calificaciones por estudiante
def consultar_calificaciones():
    estudiantes_inscritos = [u for u in usuarios if isinstance(u, Estudiante)]
    if len(estudiantes_inscritos) == 0:
        print("No hay estudiantes inscritos")
    else:
        for est in estudiantes_inscritos:
            print(f"\n{est.mostrar_info()}")
            if len(est.cursos) == 0:
                print("   No está inscrito en ningún curso.")
            else:
                for curso in est.cursos:
                    print(f"   Curso: {curso.mostrar_info()}")
                    if len(curso.evaluaciones) == 0:
                        print("      -No hay evaluaciones registradas.")
                    else:
                        for evalua in curso.evaluaciones:
                            nota = evalua.obtener_calificacion(est.id)
                            if nota is not None:
                                print(f"      -{evalua.mostrar_info()}, Nota: {nota}")
                            else:
                                print(f"      -{evalua.mostrar_info()}, Sin nota")

# Reporte de estudiantes con promedio bajo
def estudiantes_promedio_bajo():
    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    for curso in cursos:
        print(f"\nCurso: {curso.mostrar_info()}")
        estudiantes_inscritos = [u for u in usuarios if isinstance(u, Estudiante) and curso in u.cursos]

        if not estudiantes_inscritos:
            print("   No hay estudiantes inscritos en este curso.")
            continue

        if len(curso.evaluaciones) == 0:
            print("   No hay evaluaciones registradas en este curso.")
            continue

        promedio_bajo = False
        for est in estudiantes_inscritos:
            notas = [
                evalua.obtener_calificacion(est.id) * (evalua.ponderacion / 100)
                for evalua in curso.evaluaciones
                if evalua.obtener_calificacion(est.id) is not None
            ]

            if len(notas) > 0:
                promedio = sum(notas)
                if promedio <= 61:
                    promedio_bajo = True
                    print(f"   {est.mostrar_info()} tiene promedio bajo: {promedio:.2f}")

        if not promedio_bajo:
            print("   Ningún estudiante tiene promedio bajo en este curso.")

#Agregamos eliminar usuario y curso para aplicar los destructores

# Eliminar usuario
def eliminar_usuario():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u.mostrar_info()}")
    try:
        num = int(input("Seleccione el usuario a eliminar: ")) - 1
        if 0 <= num < len(usuarios):
            u = usuarios.pop(num)
            del u
        else:
            print("Número inválido.")
    except ValueError:
        print("Debe ingresar un número.")



                            



