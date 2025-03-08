from Persona import Persona 

class Estudiante(Persona):
    def _init_(self, nombre, edad, direccion, curso):
       
        super()._init_(nombre, edad, direccion)
        self._curso = curso

    def get_curso(self):
        return self._curso

    def set_curso(self, curso):
        self._curso = curso

    def _str_(self):
        
        return f"Datos estudiante: {super()._str_()}, estan en el curso: {self._curso}"