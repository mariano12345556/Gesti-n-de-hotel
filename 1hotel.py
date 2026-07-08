#El sistema deberá administrar reservas y ocupación de habitaciones dentro de un hotel.
#  Podrá contemplar registro de huéspedes, check-in, check-out, control de habitaciones disponibles y cálculo de estadías.
# La solución también podrá incorporar distintos tipos de habitaciones y estadísticas de ocupación.





def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar huésped")
        print("2. Ver habitaciones disponibles") 
        print("3. Registrar reserva")
        print("4. Realizar Check-In")
        print("5. Realizar Check-Out")
        print("6. Ver estadísticas de ocupación")
        print("7. Salir")
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
            estadisticas()

        elif opcion == "7":
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
                    print("El huésped ya está registrado.")
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
    print("\n--- Habitaciones disponibles ---")

    with open("habitaciones.txt", "r") as archivo:
        for linea in archivo:
            habitacion = linea.strip().split(",")
            print(f"Habitación: {habitacion[0]}, Tipo: {habitacion[1]}, Estado: {habitacion[2]}")
    print()

def registrar_reserva():
    print("Función registrar reserva.")


def check_in():
    print("Función check-in.")

def check_out():
    print("Función check-out.")

def estadisticas():
    print("Función estadísticas.")

if __name__ == "__main__":
    menu_principal()