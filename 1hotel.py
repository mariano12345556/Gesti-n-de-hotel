
from datetime import datetime

with open("huespedes.txt", "a") as archivo:
    pass

with open("habitaciones.txt", "a") as archivo:
    pass

with open("reservas.txt", "a") as archivo:
    pass


def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar huésped")
        print("2. Ver todas las habitaciones") 
        print("3. Registrar reserva")
        print("4. Realizar Check-In")
        print("5. Realizar Check-Out")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_huesped()

        elif opcion == "2":
            ver_habitaciones()

        elif opcion == "3":
            registrar_reserva()

        elif opcion == "4":
            check_in()

        elif opcion == "5":
            check_out()

        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida.")

def registrar_huesped():
    print("\n--- Registrar huésped ---")

    nombre = input("Ingrese el nombre: ")
    while True:
        try:
            dni = int(input("Ingrese el DNI: "))
            if dni < 10000000 or dni > 99999999 :
                print("DNI inválido. Debe ser un número de 8 dígitos.")
            else:
                contador = 0
                existe = False
                with open("huespedes.txt", "r") as archivo:
                    for linea in archivo:
                        datos = linea.strip().split(",")
                        contador +=1
                        if datos[2].strip() == str(dni):
                            existe = True
                if existe:
                    print("Ya existe un huesped registrado con ese DNI.")
                    return
                else:
                    id_huesped = contador + 1
                    with open("huespedes.txt", "a") as archivo:
                        archivo.write(f"{id_huesped},{nombre},{dni}\n")
                    print(f"Huésped registrado: ID: {id_huesped}, Nombre: {nombre}, DNI: {dni}")
                    return

        except ValueError:      #valida que no se ingrese un valor no numérico
            print("DNI inválido. Debe ser un número de 8 dígitos.")
    





def ver_habitaciones():
    print("\n--- Habitaciones ---\n")

    print(f"{'Número':<10}{'Tipo':<15}{'Estado':<15}")
    print("-" * 40)

    with open("habitaciones.txt", "r") as archivo:
        for linea in archivo:
            habitacion = linea.strip().split(",")

            print(f"{habitacion[0]:<10}{habitacion[1]:<15}{habitacion[2]:<15}")



def registrar_reserva():
    print("\n--- Registrar reserva ---")

    print("ingrese el número de DNI del huésped:")
    dni = input("DNI: ")
    existeR = False
    id_huesped = None
    with open("huespedes.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[2].strip() == str(dni):
                existeR = True
                id_huesped = datos[0].strip()       #acá guardo id huesped para hacer la reserva al final
        if existeR:                                 #si el huesped está registrado muestra si hay habitaciones disponibles
            contadorD = 0
            with open("habitaciones.txt", "r") as archivo:
                for linea in archivo:
                    habitacion = linea.strip().split(",")
                    if habitacion[2].strip() == "Disponible":
                        contadorD += 1
                        print(f"habitacion disponible: {habitacion[0]}, Tipo: {habitacion[1]}")
                else:
                    if contadorD == 0:
                        print("No hay habitaciones disponibles")
                        return
                if contadorD > 0:                   #si el contador es mayor a 0 es porque hay habitaciones 
                    while True:
                        hay_disponible = False
                        print("Ingrese la habitación que desea reservar:")
                        numero_habitacion = input("Número de habitación: ")
  
                        with open("habitaciones.txt", "r") as archivo:
                            for linea in archivo:
                                habitacion = linea.strip().split(",")
                                if numero_habitacion == habitacion[0] and habitacion[2].strip() == "Disponible":
                                    hay_disponible = True
                                    break    
                            if hay_disponible:
                                break     #acá ya validó que la habitacion proporcionada es correcta a las disponibles y si no baja y y vuelve a mostrar la lista para reingresar una habitación disponible. una vez que valida sale del while

                            print("esta habitación no está disponible. Vuelve a revisar la lista de disponibles")
                            with open("habitaciones.txt", "r") as archivo:
                                for linea in archivo:
                                    habitacion = linea.strip().split(",")
                                    if habitacion[2].strip() == "Disponible":
                                        print(f"habitacion disponible: {habitacion[0]}, Tipo: {habitacion[1]}")
                    if hay_disponible:
                        # Validar fecha de entrada y salida
                        while True:
                            try:
                                fecha_entrada = datetime.strptime(input("Ingrese la fecha de entrada (dd/mm/aaaa): "),"%d/%m/%Y")
                                break
                            except ValueError:
                                print("Fecha inválida. Debe tener el formato dd/mm/aaaa.")
                        while True:
                            try:
                                fecha_salida = datetime.strptime(input("Ingrese la fecha de salida (dd/mm/aaaa): "),"%d/%m/%Y")
                                if fecha_salida <= fecha_entrada:
                                    print("La fecha de salida debe ser posterior a la fecha de entrada.")
                                else:
                                    break
                            except ValueError:
                                print("Fecha inválida. Debe tener el formato dd/mm/aaaa.")

                        hay_conflicto = False

                        try:
                            with open("reservas.txt", "r") as archivo:
                                for linea in archivo:

                                    datos = linea.strip().split(",")
                                    # datos[0] id reserva
                                    # datos[1] id huesped
                                    # datos[2] es el número de habitación
                                    # datos[3] fecha entrada
                                    # datos[4] fecha salida
                                    # datos[5] estado

                                    if datos[2].strip() == numero_habitacion and datos[5].strip() == "Activa":

                                        entrada_existente = datetime.strptime(datos[3].strip(), "%d/%m/%Y")
                                        salida_existente = datetime.strptime(datos[4].strip(), "%d/%m/%Y")

                                        # Comprobar si las fechas se pisan
                                        if fecha_entrada < salida_existente and fecha_salida > entrada_existente:
                                            hay_conflicto = True
                                            break

                        except FileNotFoundError:
                            # Si no existe reservas.txt significa que todavía no hay reservas
                            pass


                        if hay_conflicto:
                            print("La habitación ya está reservada para esas fechas.")
                            return

                        else:
                            print("La reserva está disponible.")

                            contador = 0

                            try:
                                with open("reservas.txt", "r") as archivo:
                                    for linea in archivo:
                                        contador += 1

                            except FileNotFoundError:
                                pass

                            id_reserva = contador + 1

                            with open("reservas.txt", "a") as archivo:
                                archivo.write(f"{id_reserva},{id_huesped},{numero_habitacion},"f"{fecha_entrada.strftime('%d/%m/%Y')},"f"{fecha_salida.strftime('%d/%m/%Y')},Activa\n")

                            print("\nReserva registrada correctamente.")
                            print(f"ID de reserva: {id_reserva}")



def check_in():

    print("\n--- Check-In ---")

    id_reserva = input("Ingrese el ID de la reserva: ")

    existe = False
    numero_habitacion = ""

    with open("reservas.txt","r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0].strip() == id_reserva:
                existe = True
                numero_habitacion = datos[2].strip()
                if datos[5].strip() != "Activa":
                    print("La reserva no está activa.")
                    return
                break
        if not existe:
            print("Reserva no encontrada.")
            return

    nuevas_lineas = []

    with open("habitaciones.txt", "r") as archivo:
        for linea in archivo:
            habitacion = linea.strip().split(",")
            if habitacion[0].strip() == numero_habitacion:
                habitacion[2] = "Ocupada"
            nuevas_lineas.append(",".join(habitacion) + "\n")

    # Sobrescribimos el archivo con la información actualizada
    with open("habitaciones.txt", "w") as archivo:
        archivo.writelines(nuevas_lineas)

    nuevas_lineas = []
    with open("reservas.txt", "r") as archivo:
        for linea in archivo:
            reserva = linea.strip().split(",")
            if reserva[0].strip() == id_reserva:
                reserva[5] = "En curso"
            nuevas_lineas.append(",".join(reserva) + "\n")

    with open("reservas.txt", "w") as archivo:
        archivo.writelines(nuevas_lineas)
    print("Check-in realizado correctamente.")



def check_out():
    print("\n--- Check-out ---")
    id_reserva = input("Ingrese el ID de la reserva: ")

    existe = False
    numero_habitacion = ""

    with open("reservas.txt","r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0].strip() == id_reserva:
                existe = True
                numero_habitacion = datos[2].strip()
                if datos[5].strip() != "En curso":
                    print("La reserva no está en curso.")
                    return
                break
        if not existe:
            print("Reserva no encontrada.")
            return

    nuevas_lineas = []

    with open("habitaciones.txt", "r") as archivo:
        for linea in archivo:
            habitacion = linea.strip().split(",")
            if habitacion[0].strip() == numero_habitacion:
                habitacion[2] = "Disponible"
            nuevas_lineas.append(",".join(habitacion) + "\n")


    with open("habitaciones.txt", "w") as archivo:
        archivo.writelines(nuevas_lineas)

    nuevas_lineas = []
    with open("reservas.txt", "r") as archivo:
        for linea in archivo:
            reserva = linea.strip().split(",")
            if reserva[0].strip() == id_reserva:
                reserva[5] = "Finalizada"
            nuevas_lineas.append(",".join(reserva) + "\n")

    with open("reservas.txt", "w") as archivo:
        archivo.writelines(nuevas_lineas)
    print("Check-out realizado correctamente.")


if __name__ == "__main__":
    menu_principal()