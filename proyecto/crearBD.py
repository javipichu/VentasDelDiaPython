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
    cursor.execute("insert into proveedores values('idprov1','El Cornet','123-456-789','Av. calle del paraiso Nº56','986123456','ElCortel@gmail.com')")
    cursor.execute("insert into proveedores values('idprov2','Helados La Cumbre','987-654-321','C. Super Mario Bross Nº89','986654987','HeladosLaCumbre@gmail.com')")
    cursor.execute("insert into proveedores values('idprov3','Fit Fruit','563-234-789','C.Abrazamozas Nº76','9869876541','FitFruit@gmail.com')")

    cursor.execute("insert into productos values('idpro1','Zumo de Naranja','Productos nutritivos con sabores frescos', 2000, 1.5$,'idprov3')")
    cursor.execute("insert into productos values('idpro2','Tarrina de Helado','Helados en tarrina de sabores artesanales', 300, 2.5$, 'idprov2')")
    cursor.execute("insert into productos values('idpro3','Tartas','Elavoracion de tartas tradicionales caseras', 1000, 3.5$, 'idprov1')")

    cursor.execute("insert into facturasClientes values(1,'Dia','654987321','Av. de balaidos Nº13','Dia@gmail.com')")
    cursor.execute("insert into facturasClientes values(1,'Dia','321564879','Av. do Alcalde Portanet Nº4','Dia@gmail.com')")

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