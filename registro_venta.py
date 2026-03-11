def registro_ventas():
    estado = True
    while estado:  
        try:
            nombre = input("Ingrese el nombre del producto: ")  
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("¿Cuántos productos desea comprar?: "))
            subtotal = precio * cantidad  
            estado = False
            # Devolvemos los datos como una tupla
            return (nombre, precio, cantidad, subtotal)
        except ValueError:       
            print("¡ERROR! Debe ingresar un número. Intente de nuevo.")