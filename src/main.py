from textual.app import App, ComposeResult
from textual.containers import Middle, Center
from textual.widgets import Footer, Header, Label
from clientScreens import AddClientes, ClientesMainMenu, DeleteClientes, EditClientes, SearchClientes
from pyfiglet import Figlet


class ProyectoApp(App):
    CSS_PATH = "styles.tcss"

    BINDINGS = [("C", "push_screen('clientes')", "Clientes"),
                ("O", "order_menu", "Ordenes"),
                ("M", "menu_menu", "Menus y Platillos")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Center():
            with Middle():
                yield Label(Figlet(font="big").renderText("Ghost Kitchen Manager"))
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "GKM"
        self.sub_title = "Ghost Kitchen Manager"
        # Installs
        # Clientes
        self.install_screen(ClientesMainMenu(), name="clientes")
        self.install_screen(EditClientes(), name="clientesEdit")
        self.install_screen(AddClientes(), name="clientesAdd")
        self.install_screen(SearchClientes(), name="clientesSearch")
        self.install_screen(DeleteClientes(), name="clientesDelete")
        # Ordenes

        # Menus y Platillos

#    def action_menu_menu(self):
#        self.push_screen(ClientesMainMenu)
#
#    def action_client_menu(self):
#        pass
#
#    def action_order_menu(self):
#        pass


if __name__ == "__main__":
    app = ProyectoApp()
    app.run()
