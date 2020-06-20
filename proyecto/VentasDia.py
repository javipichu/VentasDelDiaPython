import gi

from proyecto.CrearFactura import CrearFactura
from proyecto.Inventario import Inventario
from proyecto.NuevoProv import NuevoProv
from proyecto.listaProveedores import listaProveedores

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentasdelDia():
    """Ventana Principal Ventas del dia.
    
    """

    def __init__(self):
        """Constructor de la Ventana Principal
        """
        builder = Gtk.Builder()
        builder.add_from_file("VentasDia.glade")

        self.ventana = builder.get_object("Main")

        ##AÑADIMOS LA CABECERA
        cabeceira = Gtk.HeaderBar(title="Ventana Principal")
        cabeceira.set_subtitle("Bienvenido a Los Productos del Dia")
        cabeceira.props.show_close_button = True

        self.ventana.set_titlebar(cabeceira)

        señales = {
            "on_btnAñadirProv_clicked": self.on_btnAñadirProv_clicked,
            "on_btnModProv_clicked": self.on_btnModProv_clicked,
            "on_btnFactura_clicked": self.on_btnFactura_clicked,
            "on_btnInventario_clicked": self.on_btnInventario_clicked,
            "on_btnSalir_clicked": Gtk.main_quit,
            "on_Main_destroy": Gtk.main_quit
        }

        builder.connect_signals(señales)

        self.ventana.show_all()

    def on_btnAñadirProv_clicked(self, boton):
        """Abre la ventana Añadir Proveedor

        """
        self.ventana.hide()
        NuevoProv(self.ventana)

    def on_btnModProv_clicked(self, boton):
        """Abre la ventana Modificar Proveedor
                """
        self.ventana.hide()
        listaProveedores(self.ventana)

    def on_btnFactura_clicked(self, boton):
        """Abre la ventana Crear Factura
        """
        self.ventana.hide()
        CrearFactura(self.ventana)

    def on_btnInventario_clicked(self, boton):
        """Abre la ventana Inventario
        """
        self.ventana.hide()
        Inventario(self.ventana)


def main():
    VentasdelDia()
    Gtk.main()


if __name__ == "__main__":
    VentasdelDia()
    Gtk.main()
