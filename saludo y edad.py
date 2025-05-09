import tkinter as tk

def mostrar_mensaje():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    if nombre.strip() and edad.strip().isdigit():
        ventana_principal.destroy()
        ventana_saludo = tk.Tk()
        ventana_saludo.title("Saludo")
        mensaje = f"Hola {nombre}, mucho gusto.\nVeo que tienes {edad} años."
        tk.Label(ventana_saludo, text=mensaje, font=("Arial", 16), justify="center").pack(padx=20, pady=40)
        ventana_saludo.mainloop()

ventana_principal = tk.Tk()
ventana_principal.title("Introducir datos")

tk.Label(ventana_principal, text="Introduce tu nombre:", font=("Arial", 12)).pack(pady=(10, 0))
entrada_nombre = tk.Entry(ventana_principal, font=("Arial", 12))
entrada_nombre.pack(pady=(0, 10))

tk.Label(ventana_principal, text="Introduce tu edad:", font=("Arial", 12)).pack()
entrada_edad = tk.Entry(ventana_principal, font=("Arial", 12))
entrada_edad.pack(pady=(0, 10))

tk.Button(ventana_principal, text="Enviar", font=("Arial", 12), command=mostrar_mensaje).pack(pady=20)

ventana_principal.mainloop()