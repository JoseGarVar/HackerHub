#Programa HackerHub
UNIDADES = (
    'C E R O ',
    'U N O ',
    'D O S ',
    'T R E S ',
    'C U A T R O ',
    'C I N C O ',
    'S E I S ',
    'S I E T E ',
    'O C H O ',
    'N U E V E ',
    'D I E Z ',
    'O N C E ',
    'D O C E ',
    'T R E C E ',
    'C A T O R C E ',
    'Q U I N C E ',
    'D I E C I S E I S ',
    'D I E C I S I E T E ',
    'D I E C I O C H O ',
    'D I E C I N U E V E ',
    'V E I N T E '
)
DECENAS = (
    'V E N T I ',
    'T R E I N T A ',
    'C U A R E N T A ',
    'C I N C U E N T A ',
    'S E S E N T A ',
    'S E T E N T A ',
    'O C H E N T A ',
    'N O V E N T A ',
    'C I E N '
)
CENTENAS = (
    'C I E N T O ',
    'D O S C I E N T O S ',
    'T R E S C I E N T O S ',
    'C U A T R O C I E N T O S ',
    'Q U I N I E N T O S ',
    'S E I S C I E N T O S ',
    'S E T E C I E N T O S ',
    'O C H O C I E N T O S ',
    'N O V E C I E N T O S '
)

def ordenar(lista):
    for recorrido in range(1,len(lista)):
        for posicion in range(len(lista)-recorrido):
            if lista[posicion] > lista[posicion + 1]:
                lista[posicion],lista[posicion+1] = lista[posicion+1],lista[posicion]
    return


#Numeros = { 0 : "c e r o ", 1 : "u n o ",  2 : "d o s ",  3 : "t r e s ",  4 : "c u a t r o ",  5 : "c i n c o ",  6 : "s e i s ",  7 : "s i e t e ",  8 : "o c h o ",  9 : "n u e v e ",  10 : "d i e z "}


Numero_Usuario = int(raw_input("Ingrese el Numero: "))
i = 0
Cadena_Total = ""



#Numeros mayores de 0 hasta menores de 1000

if Numero_Usuario >= 0 and Numero_Usuario < 1000:
    for cont_unidad in range(Numero_Usuario + 1):
        if cont_unidad <= 20:
            Cadena_Total = Cadena_Total + UNIDADES[cont_unidad]
        elif cont_unidad > 20 and cont_unidad <100:
            if Numero_Usuario > 20 and cont_unidad < 30:
                Cadena_Total = Cadena_Total + DECENAS[0] + UNIDADES[cont_unidad - 20]
                
            elif  Numero_Usuario >= 30 and cont_unidad < 40:
                if cont_unidad == 30:
                    Cadena_Total = Cadena_Total + DECENAS[1]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[1] + UNIDADES[cont_unidad - 30]
                    
            elif  Numero_Usuario >= 40 and cont_unidad < 50:
                if cont_unidad == 40:
                    Cadena_Total = Cadena_Total + DECENAS[2]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[2] + UNIDADES[cont_unidad - 40] 
                    
            elif  Numero_Usuario >= 50 and cont_unidad < 60:
                if cont_unidad == 50:
                    Cadena_Total = Cadena_Total + DECENAS[3]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[3] + UNIDADES[cont_unidad - 50]                        

            elif  Numero_Usuario >= 60 and cont_unidad < 70:
                if cont_unidad == 60:
                    Cadena_Total = Cadena_Total + DECENAS[4]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[4] + UNIDADES[cont_unidad - 60]
                                
            elif  Numero_Usuario >= 70 and cont_unidad < 80:
                if cont_unidad == 70:
                    Cadena_Total = Cadena_Total + DECENAS[5]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[5] + UNIDADES[cont_unidad - 70] 
                                
            elif  Numero_Usuario >= 80 and cont_unidad < 90:
                if cont_unidad == 80:
                    Cadena_Total = Cadena_Total + DECENAS[6]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[6] + UNIDADES[cont_unidad - 80]

            elif  Numero_Usuario >= 90 and cont_unidad < 100:
                if cont_unidad == 90:
                    Cadena_Total = Cadena_Total + DECENAS[7]
                else:
                    Cadena_Total = Cadena_Total + DECENAS[7] + UNIDADES[cont_unidad - 90]
                    
        elif cont_unidad > 99 and cont_unidad <1000:
            if cont_unidad == 100:
                Cadena_Total = Cadena_Total + DECENAS[8]          
            elif cont_unidad > 100 and cont_unidad < 200:
                if cont_unidad > 100 and cont_unidad <= 120:
                    Cadena_Total = Cadena_Total + CENTENAS[0] + UNIDADES[cont_unidad - 100]
                elif cont_unidad > 120 and cont_unidad < 130:
                    Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[0] + UNIDADES[cont_unidad - 120]
                    #Correccion del BUG
                    
                    
                elif cont_unidad >= 130 and cont_unidad < 140:
                    if cont_unidad == 130:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[1] + UNIDADES[cont_unidad - 130]                          
               
                elif cont_unidad >= 140 and cont_unidad < 150:
                    if cont_unidad == 140:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[2] + UNIDADES[cont_unidad - 140]
                        
                elif cont_unidad >= 150 and cont_unidad < 160:
                    if cont_unidad == 150:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[3] + UNIDADES[cont_unidad - 150]
                        
                elif cont_unidad >= 160 and cont_unidad < 170:
                    if cont_unidad == 160:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[4] + UNIDADES[cont_unidad - 160]
                        
                elif cont_unidad >= 170 and cont_unidad < 180:
                    if cont_unidad == 170:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[5] + UNIDADES[cont_unidad - 170]
                        
                elif cont_unidad >= 180 and cont_unidad < 190:
                    if cont_unidad == 180:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[6] + UNIDADES[cont_unidad - 180]

                elif cont_unidad >= 190 and cont_unidad < 200:
                    if cont_unidad == 190:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[0] + DECENAS[7] + UNIDADES[cont_unidad - 190]
            
                        
                        #Del 200 al 300
                        
            elif cont_unidad >= 200 and cont_unidad < 300:
                if cont_unidad == 200:
                    Cadena_Total = Cadena_Total + CENTENAS[1]
                    
                elif cont_unidad > 200 and cont_unidad <= 220:
                    Cadena_Total = Cadena_Total + CENTENAS[1] + UNIDADES[cont_unidad - 200]
                elif cont_unidad > 220 and cont_unidad < 230:
                    Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[0] + UNIDADES[cont_unidad - 220]
                                            
                                            
                                            
                elif cont_unidad >= 230 and cont_unidad < 240:
                    if cont_unidad == 230:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[1] + UNIDADES[cont_unidad - 230]                          
                                       
                elif cont_unidad >= 240 and cont_unidad < 250:
                    if cont_unidad == 240:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[2] + UNIDADES[cont_unidad - 240]
                                                
                elif cont_unidad >= 250 and cont_unidad < 260:
                    if cont_unidad == 250:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[3] + UNIDADES[cont_unidad - 250]
                                                
                elif cont_unidad >= 260 and cont_unidad < 270:
                    if cont_unidad == 260:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[4] + UNIDADES[cont_unidad - 260]
                                                
                elif cont_unidad >= 270 and cont_unidad < 280:
                    if cont_unidad == 270:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[5] + UNIDADES[cont_unidad - 270]
                                                
                elif cont_unidad >= 280 and cont_unidad < 290:
                    if cont_unidad == 280:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[6] + UNIDADES[cont_unidad - 280]
                        
                elif cont_unidad >= 290 and cont_unidad < 300:
                    if cont_unidad == 290:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[1] + DECENAS[7] + UNIDADES[cont_unidad - 290]            


                        #Del 300 al 400
            elif cont_unidad >= 300 and cont_unidad < 400:
                if cont_unidad == 300:
                    Cadena_Total = Cadena_Total + CENTENAS[2]
                                    
                elif cont_unidad > 300 and cont_unidad <= 320:
                    Cadena_Total = Cadena_Total + CENTENAS[2] + UNIDADES[cont_unidad - 300]
                elif cont_unidad > 320 and cont_unidad < 330:
                    Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[0] + UNIDADES[cont_unidad - 320]
                                                            
                                                            
                                                            
                elif cont_unidad >= 330 and cont_unidad < 340:
                    if cont_unidad == 330:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[1] + UNIDADES[cont_unidad - 330]                          
                                                       
                elif cont_unidad >= 340 and cont_unidad < 350:
                    if cont_unidad == 340:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[2] + UNIDADES[cont_unidad - 340]
                                                                
                elif cont_unidad >= 350 and cont_unidad < 360:
                    if cont_unidad == 350:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[3] + UNIDADES[cont_unidad - 350]
                                                                
                elif cont_unidad >= 360 and cont_unidad < 370:
                    if cont_unidad == 360:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[4] + UNIDADES[cont_unidad - 360]
                                                                
                elif cont_unidad >= 370 and cont_unidad < 380:
                    if cont_unidad == 370:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[5] + UNIDADES[cont_unidad - 370]
                                                                
                elif cont_unidad >= 380 and cont_unidad < 390:
                    if cont_unidad == 380:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[6] + UNIDADES[cont_unidad - 380]
                                        
                elif cont_unidad >= 390 and cont_unidad < 400:
                    if cont_unidad == 390:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[2] + DECENAS[7] + UNIDADES[cont_unidad - 390] 

#del 400 al 500

            elif cont_unidad >= 400 and cont_unidad < 500:
                if cont_unidad == 400:
                    Cadena_Total = Cadena_Total + CENTENAS[3]
                                    
                elif cont_unidad > 400 and cont_unidad <= 420:
                    Cadena_Total = Cadena_Total + CENTENAS[3] + UNIDADES[cont_unidad - 400]
                elif cont_unidad > 420 and cont_unidad < 430:
                    Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[0] + UNIDADES[cont_unidad - 420]
                                                            
                                                            
                                                            
                elif cont_unidad >= 430 and cont_unidad < 440:
                    if cont_unidad == 430:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[1] + UNIDADES[cont_unidad - 430]                          
                                                       
                elif cont_unidad >= 440 and cont_unidad < 450:
                    if cont_unidad == 440:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[2] + UNIDADES[cont_unidad - 440]
                                                                
                elif cont_unidad >= 450 and cont_unidad < 460:
                    if cont_unidad == 450:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[3] + UNIDADES[cont_unidad - 450]
                                                                
                elif cont_unidad >= 460 and cont_unidad < 470:
                    if cont_unidad == 460:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[4] + UNIDADES[cont_unidad - 460]
                                                                
                elif cont_unidad >= 470 and cont_unidad < 480:
                    if cont_unidad == 470:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[5] + UNIDADES[cont_unidad - 470]
                                                                
                elif cont_unidad >= 480 and cont_unidad < 490:
                    if cont_unidad == 480:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[6] + UNIDADES[cont_unidad - 480]
                                        
                elif cont_unidad >= 490 and cont_unidad < 500:
                    if cont_unidad == 490:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[3] + DECENAS[7] + UNIDADES[cont_unidad - 490] 
#Numeros del 500 al 600

            elif cont_unidad >= 500 and cont_unidad < 600:
                if cont_unidad == 500:
                    Cadena_Total = Cadena_Total + CENTENAS[4]
                                    
                elif cont_unidad > 500 and cont_unidad <= 520:
                    Cadena_Total = Cadena_Total + CENTENAS[4] + UNIDADES[cont_unidad - 500]
                elif cont_unidad > 520 and cont_unidad < 530:
                    Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[0] + UNIDADES[cont_unidad - 520]
                                                            
                                                            
                                                            
                elif cont_unidad >= 530 and cont_unidad < 540:
                    if cont_unidad == 530:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[1] + UNIDADES[cont_unidad - 530]                          
                                                       
                elif cont_unidad >= 540 and cont_unidad < 550:
                    if cont_unidad == 540:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[2] + UNIDADES[cont_unidad - 540]
                                                                
                elif cont_unidad >= 550 and cont_unidad < 560:
                    if cont_unidad == 550:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[3] + UNIDADES[cont_unidad - 550]
                                                                
                elif cont_unidad >= 560 and cont_unidad < 570:
                    if cont_unidad == 560:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[4] + UNIDADES[cont_unidad - 560]
                                                                
                elif cont_unidad >= 570 and cont_unidad < 580:
                    if cont_unidad == 570:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[5] + UNIDADES[cont_unidad - 570]
                                                                
                elif cont_unidad >= 580 and cont_unidad < 590:
                    if cont_unidad == 580:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[6] + UNIDADES[cont_unidad - 580]
                                        
                elif cont_unidad >= 590 and cont_unidad < 600:
                    if cont_unidad == 590:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[4] + DECENAS[7] + UNIDADES[cont_unidad - 590] 

#Numero del 600 al 700

            elif cont_unidad >= 600 and cont_unidad < 700:
                if cont_unidad == 600:
                    Cadena_Total = Cadena_Total + CENTENAS[5]
                                    
                elif cont_unidad > 600 and cont_unidad <= 620:
                    Cadena_Total = Cadena_Total + CENTENAS[5] + UNIDADES[cont_unidad - 600]
                elif cont_unidad > 620 and cont_unidad < 630:
                    Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[0] + UNIDADES[cont_unidad - 620]
                                                            
                                                            
                                                            
                elif cont_unidad >= 630 and cont_unidad < 640:
                    if cont_unidad == 630:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[1] + UNIDADES[cont_unidad - 630]                          
                                                       
                elif cont_unidad >= 640 and cont_unidad < 650:
                    if cont_unidad == 640:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[2] + UNIDADES[cont_unidad - 640]
                                                                
                elif cont_unidad >= 650 and cont_unidad < 660:
                    if cont_unidad == 650:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[3] + UNIDADES[cont_unidad - 650]
                                                                
                elif cont_unidad >= 660 and cont_unidad < 670:
                    if cont_unidad == 660:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[4] + UNIDADES[cont_unidad - 660]
                                                                
                elif cont_unidad >= 670 and cont_unidad < 680:
                    if cont_unidad == 670:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[5] + UNIDADES[cont_unidad - 670]
                                                                
                elif cont_unidad >= 680 and cont_unidad < 690:
                    if cont_unidad == 680:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[6] + UNIDADES[cont_unidad - 680]
                                        
                elif cont_unidad >= 690 and cont_unidad < 700:
                    if cont_unidad == 690:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[5] + DECENAS[7] + UNIDADES[cont_unidad - 690]
            
#Numeros del 700 al 800

            elif cont_unidad >= 700 and cont_unidad < 800:
                if cont_unidad == 700:
                    Cadena_Total = Cadena_Total + CENTENAS[6]
                                    
                elif cont_unidad > 700 and cont_unidad <= 720:
                    Cadena_Total = Cadena_Total + CENTENAS[6] + UNIDADES[cont_unidad - 700]
                elif cont_unidad > 720 and cont_unidad < 730:
                    Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[0] + UNIDADES[cont_unidad - 720]
                                                            
                                                            
                                                            
                elif cont_unidad >= 730 and cont_unidad < 740:
                    if cont_unidad == 730:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[1] + UNIDADES[cont_unidad - 730]                          
                                                       
                elif cont_unidad >= 740 and cont_unidad < 750:
                    if cont_unidad == 740:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[2] + UNIDADES[cont_unidad - 740]
                                                                
                elif cont_unidad >= 750 and cont_unidad < 760:
                    if cont_unidad == 750:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[3] + UNIDADES[cont_unidad - 750]
                                                                
                elif cont_unidad >= 760 and cont_unidad < 770:
                    if cont_unidad == 760:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[4] + UNIDADES[cont_unidad - 760]
                                                                
                elif cont_unidad >= 770 and cont_unidad < 780:
                    if cont_unidad == 770:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[5] + UNIDADES[cont_unidad - 770]
                                                                
                elif cont_unidad >= 780 and cont_unidad < 790:
                    if cont_unidad == 780:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[6] + UNIDADES[cont_unidad - 780]
                                        
                elif cont_unidad >= 790 and cont_unidad < 700:
                    if cont_unidad == 790:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[6] + DECENAS[7] + UNIDADES[cont_unidad - 790]


#Numeros del 800 al 900

            elif cont_unidad >= 800 and cont_unidad < 900:
                if cont_unidad == 800:
                    Cadena_Total = Cadena_Total + CENTENAS[7]
                                    
                elif cont_unidad > 800 and cont_unidad <= 820:
                    Cadena_Total = Cadena_Total + CENTENAS[7] + UNIDADES[cont_unidad - 800]
                elif cont_unidad > 820 and cont_unidad < 830:
                    Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[0] + UNIDADES[cont_unidad - 820]
                                                            
                                                            
                                                            
                elif cont_unidad >= 830 and cont_unidad < 840:
                    if cont_unidad == 830:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[1] + UNIDADES[cont_unidad - 830]                          
                                                       
                elif cont_unidad >= 840 and cont_unidad < 850:
                    if cont_unidad == 840:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[2] + UNIDADES[cont_unidad - 840]
                                                                
                elif cont_unidad >= 850 and cont_unidad < 860:
                    if cont_unidad == 850:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[3] + UNIDADES[cont_unidad - 850]
                                                                
                elif cont_unidad >= 860 and cont_unidad < 870:
                    if cont_unidad == 860:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[4] + UNIDADES[cont_unidad - 860]
                                                                
                elif cont_unidad >= 870 and cont_unidad < 880:
                    if cont_unidad == 870:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[5] + UNIDADES[cont_unidad - 870]
                                                                
                elif cont_unidad >= 880 and cont_unidad < 890:
                    if cont_unidad == 880:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[6] + UNIDADES[cont_unidad - 880]
                                        
                elif cont_unidad >= 890 and cont_unidad < 900:
                    if cont_unidad == 890:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[7] + DECENAS[7] + UNIDADES[cont_unidad - 890]
#Numeros del 900 al 999

            elif cont_unidad >= 900 and cont_unidad < 1000:
                if cont_unidad == 900:
                    Cadena_Total = Cadena_Total + CENTENAS[8]
                                    
                elif cont_unidad > 900 and cont_unidad <= 920:
                    Cadena_Total = Cadena_Total + CENTENAS[8] + UNIDADES[cont_unidad - 900]
                elif cont_unidad > 920 and cont_unidad < 930:
                    Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[0] + UNIDADES[cont_unidad - 920]
                                                            
                                                            
                                                            
                elif cont_unidad >= 930 and cont_unidad < 940:
                    if cont_unidad == 930:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[1]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[1] + UNIDADES[cont_unidad - 930]                          
                                                       
                elif cont_unidad >= 940 and cont_unidad < 950:
                    if cont_unidad == 940:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[2]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[2] + UNIDADES[cont_unidad - 940]
                                                                
                elif cont_unidad >= 950 and cont_unidad < 960:
                    if cont_unidad == 950:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[3]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[3] + UNIDADES[cont_unidad - 950]
                                                                
                elif cont_unidad >= 960 and cont_unidad < 970:
                    if cont_unidad == 960:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[4]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[4] + UNIDADES[cont_unidad - 960]
                                                                
                elif cont_unidad >= 970 and cont_unidad < 980:
                    if cont_unidad == 970:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[5]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[5] + UNIDADES[cont_unidad - 970]
                                                                
                elif cont_unidad >= 980 and cont_unidad < 990:
                    if cont_unidad == 980:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[6]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[6] + UNIDADES[cont_unidad - 980]
                                        
                elif cont_unidad >= 990 and cont_unidad < 900:
                    if cont_unidad == 890:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[7]
                    else:
                        Cadena_Total = Cadena_Total + CENTENAS[8] + DECENAS[7] + UNIDADES[cont_unidad - 990]
elif Numero_Usuario > 999:
    print "Numero Mayor que el Limite Permitido"

#for cont in range(Numero_Usuario + 1):
#    Cadena_Total = Cadena_Total + Numeros[cont]
    
print Cadena_Total

lista = Cadena_Total.split()

print lista

ordenar(lista)

print lista


lista_no_repetidos = []

for x in lista:
    if x not in lista_no_repetidos:
        lista_no_repetidos.append(x)
print (lista_no_repetidos)
