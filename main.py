from OperacionesAritmeticas import  OperacionesArtimeticas
if __name__== "__main__":
    operación=  OperacionesArtimeticas()
    num1,num2 = operación.ingresoNumeros()
    print(f"{num1} + {num2}= {operación.suma(num1,num2)}")