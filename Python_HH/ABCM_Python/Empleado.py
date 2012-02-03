class Empleado:
    #Abstraccion de los Objetos Empleado
    def __init__(self,Nombre,Apellidos,Profesion,Telefono,Numero):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Profesion = Profesion
        self.Telefono = Telefono
        self.Numero = Numero
        
    def Redes(self,Github,Twitter,Facebook):
        self.Github = Github
        self.Twitter = Twitter
        self.Facebook = Facebook
        
    def Proyecto(self,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribudores):
        self.NombreP = NombreP
        self.Tipo = Tipo
        self.Tecnologia = Tecnologia
        self.Repositorio = Repositorio
        self.Sitio = Sitio
        self.Contribudores = Contribudores
        
    def Imprimir_Personal(self):
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
        
    def Alta(self):
        
 
 
 #Falta crear funciones alta, baja, etc       
        