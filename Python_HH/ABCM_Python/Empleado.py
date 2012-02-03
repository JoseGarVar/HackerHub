class Empleado:
    #Abstraccion de los Objetos Empleado
    def __init__(self):
        print "Accediendo A la Base de Datos"
        
    def Personal(self,Numero,Nombre,Apellidos,Profesion,Telefono):
        self.Numero = Numero
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Profesion = Profesion
        self.Telefono = Telefono
        return True
        
        
    def Redes(self,Github = "NO",Twitter = "NO",Facebook = "NO"):
        self.Github = Github
        self.Twitter = Twitter
        self.Facebook = Facebook
        
    def Proyecto(self,NombreP = "",Tipo = "",Tecnologia = "",Repositorio = "",Sitio = "",Contribudores = ""):
        self.NombreP = NombreP
        self.Tipo = Tipo
        self.Tecnologia = Tecnologia
        self.Repositorio = Repositorio
        self.Sitio = Sitio
        self.Contribudores = Contribudores
        
    def Imprimir_Personal(self):
        print "Numero de Empleado" , self.Numero
        print "Nombre:" , self.Nombre , self.Apellidos
        print "Profesion/Ocupacion:" , self.Profesion
        print "Telefono:" ,int(self.Telefono)
        
    def Imprimir_Gustos(self):
        print "Github:" , self.Github
        print "Twitter:" , self.Twitter
        print "Facebook:" , self.Facebook
        
    def Imprimir_Proyecto(self):
        print "Nombre del Proyecto:" , self.NombreP
        print "Tipo:" , self.Tipo
        print "Tecnologia:" , self.Tecnologia 
        print "Repositorio:" , self.Repositorio
        print "Sitio:" , self.Sitio
        print "Contribudores:" , self.Contribudores 
        
    def Alta(self,Numero,Nombre,Apellidos,Profesion,Telefono):
        if self.Personal(Numero,Nombre,Apellidos,Profesion,Telefono) == True:
            print "Dado de Alta..."
        self.Imprimir_Personal()
 
 
 #Falta crear funciones alta, baja, etc       
        
#Guardar con una , y cuando se lea se divide