"""
 Diseña un programa para determinar si una palabra o frase comienza con una vocal. Toma en cuenta que las vocales no por estar en mayúscula o tener acento dejan de ser vocales.
 750722
"""
#Entradas
palabra = []
palabra = input("Escribe una palabra: ")
palabra = palabra.lower()

#Procesos
if palabra[0] in ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]:
    print(f"'{palabra}' comienza con vocal")
else:
    print(f"'{palabra}' no comienza con vocal")
