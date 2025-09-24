import os
from rich.align import Align
from rich.box import box
from rich.console import RenderableType
from rich.table import Table, header

def menuLoop() -> None:
    while True:
        pass

def tablaMenuPrincipal() -> RenderableType:
    table = Table(
        title="Menu principal",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="center")
    table.add_row("1. Ordenes")
    table.add_row("2. Menus y Platillos")
    table.add_row("3. Clientes")
    return Align.center(table)

def clearScreen() -> None:
    if os.name != "nt":
        os.system('clear')
    else:
        os.system('cls')

def create_header() -> RenderableType:
    head = header

def createPanelCentral() -> RenderableType:
    pass
if __name__ == "__main__":
    clearScreen()
    menuLoop()
