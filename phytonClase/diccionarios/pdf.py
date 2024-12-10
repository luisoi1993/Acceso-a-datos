from fpdf import FPDF

# Crear un PDF con el contenido teórico sobre diccionarios en Python
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Trabajo de Investigación: Diccionarios en Python", border=False, ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Contenido del PDF
contenido_teorico = """
¿Qué son los diccionarios en Python?

Un diccionario en Python es una estructura de datos que almacena información en forma de pares clave-valor. 
Esto significa que cada valor en el diccionario tiene una "clave" única que permite acceder a ese valor de manera rápida. 
Los diccionarios son mutables, lo que significa que puedes añadir, modificar o eliminar elementos después de crearlos.

¿Cómo se crean los diccionarios?
Puedes crear un diccionario utilizando llaves {}. Por ejemplo:

mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

Operaciones comunes con diccionarios:

1. Acceder a un valor:
   Utiliza la clave para obtener el valor asociado:
   print(mi_diccionario["nombre"])  # Salida: Juan

2. Añadir o modificar elementos:
   Puedes añadir un nuevo par clave-valor o modificar un valor existente:
   mi_diccionario["pais"] = "España"  # Añade un nuevo par
   mi_diccionario["edad"] = 26        # Modifica el valor existente

3. Eliminar elementos:
   Utiliza la función del o el método pop:
   del mi_diccionario["ciudad"]

4. Recorrer un diccionario:
   Puedes usar un bucle for para recorrer claves y valores:
   for clave, valor in mi_diccionario.items():
       print(f"{clave}: {valor}")

Ventajas de los diccionarios:
- Permiten un acceso rápido a los datos mediante claves.
- Son ideales para almacenar información estructurada.

Ejemplo práctico:
El siguiente programa muestra cómo gestionar una agenda utilizando un diccionario.
"""

# Añadir contenido al PDF
pdf.chapter_title("Contenido teórico sobre diccionarios")
pdf.chapter_body(contenido_teorico)

# Guardar el PDF
file_path = "C:/Users/luis/Documents/Diccionarios_Python_Agenda.pdf"
pdf.output(file_path)

file_path
