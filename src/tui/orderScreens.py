from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label, Input
from textual.containers import Center, Middle, Vertical

class OrdersMainMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            with Middle():
                with Vertical():
                    yield Label("Manejo de Ordenes")
                    yield Button("Agregar", id="add")
                    yield Button("Buscar", id="search")
                    yield Button("Desactivar", id="delete")
        yield Footer()

class AddOrders():
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
