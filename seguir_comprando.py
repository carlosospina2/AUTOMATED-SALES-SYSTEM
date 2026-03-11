from registro_venta import registro_ventas 

def seguir_comprando():    
    lista = []
    corriendo = True
    while corriendo:
        opcion = input("¿Desea comprar algo? (si/no): ")
        if opcion == "si":
            item = registro_ventas()
            lista.append(item)
            print("Producto registrado con éxito.")
        elif opcion == "no":
            print("\n--- RESUMEN DE SU COMPRA ---")
            total_final = 0
            for i in lista:
                print(f"Producto: {i[0]} | Precio unitario: {i[1]} | Cantidad: {i[2]} | Total a pagar: {i[3]}")
                total_final = total_final + i[3]
            print("-" * 30)
            print("TOTAL FINAL A PAGAR: $", total_final)
            print("Gracias por su compra, vuelva pronto")
            corriendo = False
        else:
            print("ERROR!!! Solo ingrese si o no")