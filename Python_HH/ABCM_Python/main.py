import Empleado
import os
from FuncionesIO import Alta_Empleado,Baja_Empleado,Consulta_Empleado,Modificacion_Empleado
from db import create
from sqlalchemy.sql import select


MAX_EMP = 100
Emp = Empleado.Empleado()
op = 6
User = create.Users
insert = User.insert()
select = User.select()
delete = User.delete()
#upload = User.save()
and_ = create.and_

while(op > 5 or op < 1):
    #clear_output()
    os.system('clear')
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
        raw_input( "\n\nPresione ENTER para Continuar")
        op = 6
    elif op == 2:
        Baja_Empleado(Emp,delete,and_,User)
        raw_input( "\n\nPresione ENTER para Continuar")
        op = 6
    elif op == 3:
        Consulta_Empleado(Emp,and_,User)
        raw_input( "\n\nPresione ENTER para Continuar")
        op = 6
    elif op == 4:
        Modificacion_Empleado(Emp,and_,User)
        raw_input( "\n\nPresione ENTER para Continuar")
        op = 6        
    elif op == 5:
        raw_input( "\n\nSelecciono SALIR, Presione ENTER para Continuar")
        os.system('clear')
    
        
        
     #Para volver a cargar el menu
        
    
