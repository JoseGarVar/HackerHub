Lista = []

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
        return True
        
    def Proyecto(self,NombreP = "",Tipo = "",Tecnologia = "",Repositorio = "",Sitio = "",Contribudores = ""):
        self.NombreP = NombreP
        self.Tipo = Tipo
        self.Tecnologia = Tecnologia
        self.Repositorio = Repositorio
        self.Sitio = Sitio
        self.Contribudores = Contribudores
        return True
        
    def Imprimir_Personal(self):
        print "Numero de Empleado" , self.Numero
        print "Nombre:" , self.Nombre , self.Apellidos
        print "Profesion/Ocupacion:" , self.Profesion
        print "Telefono:" ,self.Telefono
        
    def Imprimir_Redes(self):
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
        
    def Alta(self,Numero,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook):
        if self.Personal(Numero,Nombre,Apellidos,Profesion,Telefono) == True and self.Redes(Github,Twitter,Facebook) == True:
            print "---------------------------------"
            print "Alta Satisfactoria\n"
            print "---------------------------------"
            self.Imprimir_Personal()
            self.Imprimir_Redes()
            self.Agregar_Lista(Numero,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook)
            print Lista
            
    def Agregar_Lista(self,Numero,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook):
        Lista.append(Numero)
        Lista.append(Nombre)
        Lista.append(Apellidos)
        Lista.append(Profesion)
        Lista.append(Telefono)
        Lista.append(Github)
        Lista.append(Twitter)
        Lista.append(Facebook)
        
 
 
 #Falta crear funciones alta, baja, etc       
        
#Guardar con una , y cuando se lea se divide

