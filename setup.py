from setuptools import setup , find_packages

setup(
    name="CasaDelLibro",
    version="1.0",
    author="David",
    author_email="dalonsofernandez@danielcastelao.org",
    license="GLP",
    platforms="Unix",
    clasifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.4",
                "Operating System :: Linux Ubuntu"
                ],
    description="Proyecto DI con sphinx reportlab y mysqllite",
    keywords="empaquetado instalador paquetes",
    packages=find_packages(),
    #data_files=[('datos', ['dat/datos.txt'])],
    package_data={
        "": ["*.txt", "*.rst", "*.glade", "*.py"],
        "proyecto": ["*"],
        "Imagenes_Docu": ["*"],
    },
    entry_points={'console_scripts': ['openProyect = proyecto.CasaDelLibro:main', ], }
)