#comentario1
palabras=[]
for i in range(5):
    palabra=input(f"ingese la palabra " )
    palabras.append(palabra)
    
#comentario2
def ordenar_por_tamano(palabras):
    return sorted(palabras,key=len,reverse=True)

#comentario3
while True:
    print("\nseleccione una opcion: ")
    print("1.orden alfabetico")
    print("2.orden de tamano, de la mas larga a la mas corta")
    print("3.orden aleatorio")
    print("4.orden inverso al ingresado")
    print("5.orden igual al ingresado")
    print("6.salir")
    
    seleccion=input("****opcion: ")
    
    match seleccion:
        case"1":
            palabras_ordenadas=sorted(palabras)
                
        case"2":
            palabras_ordenadas=ordenar_por_tamano(palabras)
            
        case"3":
            palabras_ordenadas=palabras
            import random 
            random.shuffle(palabras)
            
        case"4":
            palabras_ordenadas=list(reversed(palabras))
            
        case"5":
            palabras_ordenadas=palabras
               
        case"6":
            print("*-*-*-*-*-*-*-*-*-*-*-*-ADIOS-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            break
        case"7":
            print("****************************************opcion no valida.elija una opcion del 1-6********************************************")
            continue
        
     #comentario4
    print("\n palabras ordenadas:")
    for palabra in palabras_ordenadas:
         print(palabra)
        
        
    