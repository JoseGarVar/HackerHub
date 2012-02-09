Red = raw_input("Usted cuenta con Facebook (Responda SI/NO):")        
if Red == "NO":
                        Facebook = "NO"
                        Mal = 0
elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                        print "Responda en Mayusculas SI o NO"
                        Mal == 1
elif Red == "SI":
                        Facebook ="http://www.facebook.com/" + raw_input("\nDigite su Nombre de Usuario Facebook: ")
                        print Facebook
                        Mal = 0   