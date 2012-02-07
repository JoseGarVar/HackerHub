import Empleado
from FuncionesIO import Alta_Empleado,Baja_Empleado,Consulta_Empleado
from db import create
from sqlalchemy.sql import select


MAX_EMP = 100
Emp = Empleado.Empleado()
op = 6
User = create.Users
insert = User.insert()
select = User.select()
delete = User.delete()
and_ = create.and_

while(op > 5 or op < 1):
    #clear_output()
    print "---------------------------------"
    print "1.- Alta de Empleado"
    print "2.- Baja de Empleado"
    print "3.- Consulta de Empleado"
    print "4.- Modificar Empleado"
    print "5.- SALIR"
    op = int(raw_input("Seleccione una Opcion: "))
    print "---------------------------------"




#Altas
    if op == 1:   
        Alta_Empleado(Emp,insert)
        op = 6
    elif op == 2:
        Baja_Empleado(Emp,delete,and_,User)
        op = 6
    elif op == 3:
        Consulta_Empleado(Emp,and_,User)
        op = 6
        
        
     #Para volver a cargar el menu
        
    
