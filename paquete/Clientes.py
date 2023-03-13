class Clientes:
    def __init__(self, nombre, edad, email, direccion):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.direccion = direccion
    
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
    
    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
    
    def __str__(self):
        return self.nombre