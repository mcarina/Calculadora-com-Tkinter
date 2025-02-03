from tkinter import Tk, Entry, Button

root = Tk()
root.title("Marcy's calculadora")
root.resizable(False, False)
root.geometry("400x440")

display = Entry(root, width=20, font=('Arial', 24), bd=16, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4)

def button_click(value):
    current = display.get()
    display.delete(0, "end")  # Limpa o display
    display.insert("end", current + value)

def calculate():
    try:
        result = eval(display.get())  # Avalia a expressão matemática
        display.delete(0, "end")
        display.insert("end", str(result))  # Exibe o resultado corretamente
    except Exception:
        display.delete(0, "end")
        display.insert("end", "Erro")

def clear():
    display.delete(0, "end")

buttons = [
    ('C', 1, 0),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

# Adicionando os botões à interface
for (text, row, col) in buttons:
    if text == "=":
        button = Button(root, text=text, width=5, height=2, font=('Arial', 18),  bd=1, command=calculate)
    elif text == "C":
        button = Button(root, text=text, width=5, height=2, font=('Arial', 18), bd=1, command=clear)
    else:
        button = Button(root, text=text, width=5, height=2, font=('Arial', 18), bd=1, command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col)


root.mainloop()