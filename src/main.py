import os
import pandas as pd
import pymysql
from rich.align import Align
from rich import box
from rich.console import Console, RenderableType
from rich.table import Table
from rich.panel import Panel
from tablas import *
from connHelper import *
import orderFuncs
import clientFuncs
import menuFuncs

console = Console()

def menuLoop(conn:pymysql.Connection) -> None:
    while True:
        console.print(Align.center(createPanelCentrado(tablaMenuPrincipal()),vertical="middle"))
        console.print(Align.center("Introduzca su opcion"))
        user_input = input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")
        match user_input:
            # Ordenes
            case "1":
                console.print(Align.center(createPanelCentrado(tablaMenuOrdenes())))
                menu_input = input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")
                match menu_input:
                    case "1":
                        params = []
                        console.print(Align.center(tablaCrearOrdenID()))
                        params.append(int(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")))
                        console.print(Align.center(tablaCrearOrdenqtySalud()))
                        params.append(int(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")))
                        console.print(Align.center(tablaCrearOrdenqtyEcon()))
                        params.append(int(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")))
                        if (orderFuncs.createOrden(conn,clienteID=params[0],qtySaludable=params[1],qtyEcon=params[2])):
                            console.print(Align.center("Orden capturada correctamente!"))
                    case "2":
                        console.print(display_dataframe_in_box(pd.DataFrame(orderFuncs.getAllOrdenes(conn),
                        columns=[
                        "ID Orden","ID Cliente","Qty Saludable",
                        "Qty Economico","Precio Total","En Curso",
                        "Fecha Apartado","Semana Asignada","Año"]),
                        title="Ordenes"))
                    case "3":
                        console.print(Align.center(tablaPedirIDCliente()))
                        userID = (int(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")))
                        console.print(display_dataframe_in_box(pd.DataFrame(orderFuncs.getOrdenesFromUser(conn,userID),
                        columns=[
                        "ID Orden","ID Cliente","Qty Saludable",
                        "Qty Economico","Precio Total","En Curso",
                        "Fecha Apartado","Semana Asignada","Año"]),
                        title="Ordenes"))
            # Clientes
            case "3":
                console.print(Align.center(createPanelCentrado(tablaMenuClientes())))
                menu_input = input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")
                match menu_input:
                    case "1":
                        params = []
                        console.print(tablaCrearClientes1())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes2())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes3())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes4())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes5())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes6())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes7())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearClientes8())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        if(clientFuncs.addCliente(conn,params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7])):
                            console.print(Align.center("Se inserto el cliente correctamente"))
                    case "2":
                        console.print(display_dataframe_in_box(pd.DataFrame(clientFuncs.getClientes(conn),columns=[
                            "ID Cliente",
                            "Nombre",
                            "Telefono",
                            "Email",
                            "Calle",
                            "Numero",
                            "Numero Interior",
                            "CP",
                            "Referencias"
                        ]),title="Clientes"))

            # Menus y platillos
            case "2":
                console.print(Align.center(createPanelCentrado(tablaMenuPlatillos())))
                menu_input = input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")
                match menu_input:
                    case "1":
                        params = []
                        console.print(tableCrearPlatillo1())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tableCrearPlatillo2())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tableCrearPlatillo3())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        menuFuncs.createPlatillo(conn,params[0],params[1],params[2])
                        pass
                    case "2":
                        params = []
                        platillos = []
                        console.print(tablaCrearMenu1())
                        params.append(str(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> ")).lower())
                        console.print(tablaCrearMenu2())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        console.print(tablaCrearMenu3())
                        params.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        for i in range(1,5):
                            console.print(tablaCrearMenu5(i))
                            platillos.append(input("\n" + " " * (os.get_terminal_size().columns // 2 - 2) + "> "))
                        menuFuncs.createMenu(conn,platillos,params[0],params[1],params[2])
                    case "4":
                        console.print(display_dataframe_in_box(pd.DataFrame(menuFuncs.getMenus(conn),columns=[
                            "ID Menu",
                            "Tipo",
                            "Semana",
                            "Año",
                            "Precio"
                        ]),"Menus"))
                    case "3":
                        console.print(display_dataframe_in_box(pd.DataFrame(menuFuncs.getPlatillos(conn),columns=[
                            "ID Platillo",
                            "Nombre",
                            "Descripcion",
                            "Costo"
                        ]),"Platillos"))
                        pass
            
def clearScreen() -> None:
    if os.name != "nt":
        os.system('clear')
    else:
        os.system('cls')

# def create_header() -> RenderableType:
    # head = header

def createPanelCentrado(_contenido: RenderableType) -> RenderableType:
    return Panel(
        _contenido,
        title='GKM',
        border_style='white',
        expand=False
    )

if __name__ == "__main__":
    clearScreen()
    menuLoop(createConn())
