import pandas as pd
from rich import box
from rich import table
from rich.align import Align
from rich.console import RenderableType
from rich.panel import Panel
from rich.table import Table

def tablaMenuPrincipal() -> RenderableType:
    table = Table(
        title="Menu principal",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("1. Ordenes")
    table.add_row("2. Menus y Platillos")
    table.add_row("3. Clientes")
    return Align.center(table)

# Ordenes
def tablaMenuOrdenes() -> RenderableType:
    table = Table(
        title="Ordenes",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("1. Crear Orden")
    table.add_row("2. Reporte de ordenes")
    table.add_row("3. Reporte de ordenes por cliente")
    return Align.center(table)
## Crear Orden
def tablaCrearOrdenID() -> RenderableType:
    table = Table(
        title="Crear Orden",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca el ID del cliente que desea crear el pedido")
    return Align.center(table)

def tablaCrearOrdenqtySalud() -> RenderableType:
    table = Table(
        title="Crear Orden",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca la cantidad de menus saludables deseada")
    return Align.center(table)

def tablaCrearOrdenqtyEcon() -> RenderableType:
    table = Table(
        title="Crear Orden",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca la cantidad de menus saludables deseada")
    return Align.center(table)
## Mostrar Ordenes por cliente
def tablaPedirIDCliente() -> RenderableType:
    table = Table(
        title="Buscar Ordenes",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca el ID del cliente")
    return Align.center(table)

# Clientes
def tablaMenuClientes() -> RenderableType:
    table = Table(
        title="Clientes",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("1. Registrar Cliente")
    table.add_row("2. Listar Clientes")
    return Align.center(table)

def tablaCrearClientes1() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca el Nombre del cliente")
    return Align.center(table)

def tablaCrearClientes2() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca Email del cliente")
    return Align.center(table)

def tablaCrearClientes3() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca telefono del cliente")
    return Align.center(table)

def tablaCrearClientes4() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca Calle ")
    return Align.center(table)

def tablaCrearClientes5() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca numero de la direccion")
    return Align.center(table)

def tablaCrearClientes6() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca numero interior")
    return Align.center(table)

def tablaCrearClientes7() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca Codigo Postal")
    return Align.center(table)

def tablaCrearClientes8() -> RenderableType:
    table = Table(
        title="Crear Cliente",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("Introduzca Referencias para la direccion de entrega")
    return Align.center(table)

# Menus y Platillos
def tablaMenuPlatillos() -> RenderableType:
    table = Table(
        title="Menus y Platillos",
        box=box.MINIMAL,
        show_header=False
    )
    table.add_column(justify="left")
    table.add_row("1. Crear Platillo")
    table.add_row("2. Crear Menu")
    table.add_row("3. Listar Platillos")
    table.add_row("4. Listar Menus")
    return Align.center(table)

# Mostrar DataFrame
def display_dataframe_in_box(df: pd.DataFrame, title: str) -> RenderableType:
    rich_table = Table(
        title=title,
        show_header=True,
        header_style="magenta",
        box=box.MINIMAL
    )
    for column in df.columns:
        rich_table.add_column(str(column), style="cyan", justify="left")
    for index, row in df.iterrows():
        row_values = [str(x) for x in row]
        rich_table.add_row(*row_values)
    boxed_output = Panel(
        rich_table,
        title=f"[white]{title}[/white]",
        border_style="blue", 
        expand=True 
    )
    return boxed_output

