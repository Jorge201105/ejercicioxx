"""
1.- Menu
2.- Cambiar jugos
3.- modificar/eliminar ingredientes
4.- estimación de tiempos
5.- mostrar
6.- salir

"""
from jugos.menu import menu
from jugos.crear_bebida import crear_bebida
from jugos.seleccionar_base import seleccionar_base




def main():
    vaso =crear_bebida()


    while True:
        opcion = input("opcion")
        if opcion == "1":
            print(vaso)
        elif opcion =="2":
            print("2")
        elif opcion =="3":
            print("3")
        elif opcion =="4":
            print("4")
        elif opcion =="5":
            print("5")
        else:
            print("salir")  


if __name__ == "__main__":
    main()  