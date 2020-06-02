import os
from sqlite3 import dbapi2

"""
    Genera la base de datos y le introduce unos datos iniciales.
"""
try:
    ###Creamos la base de datos y generamos cursosr para ejecutar las consultas.
    baseDatos = dbapi2.connect("BaseDeDatos.dat")
    cursor = baseDatos.cursor()

    ###Creamos las tablas que vamos a usar
    cursor.execute("create table proveedores(id text, nombre text,CIF text, direccion text, telefono text, correo text)")
    cursor.execute("create table productos(id text, nombre text , descripcion text, cantidadStock number, precioUnidad number,idProv text)")
    cursor.execute("create table facturasClientes(idFactura number, nombreCliente text, telefono text, direccion text, correo text)")
    cursor.execute("create table facturasInfo(idFactura number,idProducto text, cantidad number)")

    ###Rezlizamos Inserts en las tablas para tener valores.
    cursor.execute("insert into proveedores values('idprov1','Galaxia','123-675-453','Av. Castelao Nº56','986456784','galaxiaeditorial@gmail.com')")
    cursor.execute("insert into proveedores values('idprov2','Xerais','444-678-453','C.Urzaiz Nº89','988789563','xeraiseditorial@gmail.com')")
    cursor.execute("insert into proveedores values('idprov3','Rodeira','563-234-789','C.Genaro de la Fuente Nº76','986097094','rodeiraeditorial@gmail.com')")

    cursor.execute("insert into productos values('idpro1','Os Arriscados','Miguel Anxo Mouriño', 300, 19,'idprov1')")
    cursor.execute("insert into productos values('idpro2','Enderezo descoñecido','Kressmann Taylor', 50, 25, 'idprov2')")
    cursor.execute("insert into productos values('idpro3','A pedra da serpe','Milio Rodríguez Cueto', 60, 27, 'idprov3')")

    cursor.execute("insert into facturasClientes values(1,'Lafer','658741236','C. Galeraias Calvario Nº7','lafer@gmail.com')")
    cursor.execute("insert into facturasClientes values(1,'Papeles','658741236','C. Genaro de la Fuente Nº56','papeles@gmail.com')")

    cursor.execute("insert into facturasInfo values(1,'pro1',2)")
    cursor.execute("insert into facturasInfo values(2,'pro2',1)")

    ###Realizamos commit en la BD
    baseDatos.commit()

###Cremos una excepcion para lo errores y finalmente cerramos la conexion
except (dbapi2.DatabaseError):
    print("ERROR BD")
finally:
    print("Cerramos conexionBD")
    cursor.close()
    baseDatos.close()