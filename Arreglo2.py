listaEst = []
resp = "Sí"
while(resp.upper() != "NO"):
    tam = len(listaEst)
    print("Elementos guardados: ", tam)
    nombres = input("Escriba el nombre del estudiante: ")
    listaEst.append(nombres)
    resp = input("¿Desea agregar más? Sí - NO: ")
    

for est in listaEst:
    print(est)