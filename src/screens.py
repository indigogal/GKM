from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Footer, Label, Input, Header
from textual.containers import Center, Middle, Vertical


class ClientesMainMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            with Middle():
                with Vertical():
                    yield Label("Manejo de clientes")
                    yield Button("Agregar", id="add")
                    yield Button("Buscar", id="search")
                    yield Button("Editar", id="edit")
                    yield Button("Desactivar", id="delete")
        yield Footer()

    @on(Button.Pressed, "#add")
    def push_agregar(self) -> None:
        self.app.push_screen("clientesAdd")

    @on(Button.Pressed, "#search")
    def push_search(self) -> None:
        self.app.push_screen("clientesSearch")

    @on(Button.Pressed, "#edit")
    def push_edit(self) -> None:
        self.app.push_screen("clientesEdit")

    @on(Button.Pressed, "#delete")
    def push_delete(self) -> None:
        self.app.push_screen("clientesDelete")


class SearchClientes(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


class EditClientes(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


class DeleteClientes(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


class AddClientes(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            with Middle():
                with Vertical():
                    yield Label("Registrar Cliente")
                    yield Input(placeholder="Nombre")
                    yield Input(placeholder="Email")
                    yield Input(placeholder="Telefono")
                    yield Label("Direccion")
                    yield Input(placeholder="Calle")
                    yield Input(placeholder="Numero")
                    yield Input(placeholder="Numero Interior (opcional)")
                    yield Input(placeholder="Referencias")
                    yield Button("Insertar")
        yield Footer()
