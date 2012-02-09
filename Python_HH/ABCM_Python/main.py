import Empleado
import os
from FuncionesIO import Alta_Empleado,Baja_Empleado,Consulta_Empleado,Modificacion_Empleado,Consulta_Empleado_General,Opciones_Profesiones,Opciones_Tecnologia,Opciones_Tipo,Opciones_Consultas
from db import create
from sqlalchemy.sql import select


Emp = Empleado.Empleado()
op = 6
op2 = 6
op3 = 6
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
    try:
        op = int(raw_input("Seleccione una Opcion: "))
    except ValueError:
        op = 6        
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
        op3 = Opciones_Consultas()
        Consulta_Empleado(Emp,and_,User)
        raw_input( "\n\nPresione ENTER para Continuar")
        op = 6
    elif op == 4:
        Modificacion_Empleado(Emp,and_,User,insert)
        raw_input( "\n\nPresione ENTER para Continuar")
        op = 6        
    elif op == 5:
        raw_input( "\n\nSelecciono SALIR, Presione ENTER para Continuar")
        os.system('clear')
    
        
Consulta_Empleado_General(Emp,and_,User)     
     #Para volver a cargar el menu
        
    
