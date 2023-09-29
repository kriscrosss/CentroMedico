from Personas.Asistente import Asistente

asistentes = [
    Asistente("Juan Pérez", "12.345.678-9", 30, "+56 9 1234 5678", "juan.perez@example.com", 2000, 40, "2023-01-15", 20),
    Asistente("María López", "23.456.789-0", 28, "+56 9 2345 6789", "maria.lopez@example.com", 1800, 35, "2023-02-20", 15),
    Asistente("Pedro Rodríguez", "34.567.890-1", 35, "+56 9 3456 7890", "pedro.rodriguez@example.com", 2200, 45, "2023-03-25", 25),
    Asistente("Ana García", "45.678.901-2", 32, "+56 9 4567 8901", "ana.garcia@example.com", 1900, 38, "2023-04-10", 18),
    Asistente("Luis Martínez", "56.789.012-3", 29, "+56 9 5678 9012", "luis.martinez@example.com", 2100, 42, "2023-05-05", 22),
    Asistente("Laura González", "67.890.123-4", 27, "+56 9 6789 0123", "laura.gonzalez@example.com", 1750, 37, "2023-06-12", 16),
    Asistente("Carlos Sánchez", "78.901.234-5", 34, "+56 9 7890 1234", "carlos.sanchez@example.com", 2050, 41, "2023-07-18", 21),
    Asistente("Marta Ramírez", "89.012.345-6", 31, "+56 9 8901 2345", "marta.ramirez@example.com", 1950, 39, "2023-08-22", 19),
    Asistente("Eduardo Torres", "90.123.456-7", 28, "+56 9 9012 3456", "eduardo.torres@example.com", 1850, 36, "2023-09-01", 17),
    Asistente("Sofía Silva", "01.234.567-8", 33, "+56 9 0123 4567", "sofia.silva@example.com", 2100, 44, "2023-10-14",  23),
    Asistente("Andrés López", "10.234.567-8", 36, "+56 9 1123 4567", "andres.lopez@example.com", 2250, 46, "2023-11-27", 26),
    Asistente("Isabel Pérez", "11.234.567-8", 29, "+56 9 1223 4567", "isabel.perez@example.com", 1900, 37, "2023-12-03", 19),
    Asistente("Felipe González", "12.234.567-8", 34, "+56 9 1323 4567", "felipe.gonzalez@example.com", 2050, 43, "2024-01-08", 20),
    Asistente("Camila Rodríguez", "13.234.567-8", 31, "+56 9 1423 4567", "camila.rodriguez@example.com", 1950, 40, "2024-02-11", 18),
    Asistente("Diego Martínez", "14.234.567-8", 27, "+56 9 1523 4567", "diego.martinez@example.com", 1750, 35, "2024-03-19",  15),
    Asistente("Valentina Sánchez", "15.234.567-8", 30, "+56 9 1623 4567", "valentina.sanchez@example.com", 1850, 38, "2024-04-24", 17),
    Asistente("Javier Torres", "16.234.567-8", 37, "+56 9 1723 4567", "javier.torres@example.com", 2000, 42, "2024-05-30", 21),
    Asistente("Natalia Silva", "17.234.567-8", 35, "+56 9 1823 4567", "natalia.silva@example.com", 1950, 40, "2024-06-05",  20),
    Asistente("Gonzalo Pérez", "18.234.567-8", 32, "+56 9 1923 4567", "gonzalo.perez@example.com", 1900, 37, "2024-07-09",  18),
    Asistente("Rocío González", "19.234.567-8", 38, "+56 9 2023 4567", "rocio.gonzalez@example.com", 2100, 44, "2024-08-14", 24)
]

# Mostrar la información de los asistentes
for idx, asistente in enumerate(asistentes, start=1):
    print(f"Asistente {idx}:")
    print(f"Nombre: {asistente.nombre}")
    print

