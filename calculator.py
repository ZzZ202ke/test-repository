python
Копировать
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Крутой Калькулятор")
        master.geometry("300x450")  # Увеличим высоту для красоты

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 1), '.': (4, 2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.master.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.master.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.master.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_percentage_button()
        self.create_plus_minus_button()

    def create_percentage_button(self):      
        button = tk.Button(self.buttons_frame, text="%", bg="#A5A5A5", fg="white", font=('Arial', 20), borderwidth=0, command=self.percentage)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_plus_minus_button(self):
        button = tk.Button(self.buttons_frame, text="+/-", bg="#A5A5A5", fg="white", font=('Arial', 20), borderwidth=0, command=self.plus_minus)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def plus_minus(self):
        try:
            self.current_expression = str(-float(self.current_expression))
            self.update_label()
        except ValueError:
            pass

    def percentage(self):
        try:
            self.current_expression = str(float(self.current_expression) / 100)
            self.update_label()
        except ValueError:
            pass

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F0F0F0",
                               fg="#777777", padx=24, font=("Arial", 16), wraplength=300, justify=tk.RIGHT)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#F0F0F0",
                         fg="black", padx=24, font=("Arial", 35, 'bold'), wraplength=300, justify=tk.RIGHT)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.master, height=221, bg="#F0F0F0")
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#333333", fg="white", font=('Arial', 24),
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#FFA500", fg="white", font=('Arial', 24),
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg="#A5A5A5", fg="black", font=('Arial', 24),
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=0, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Ошибка"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#FFA500", fg="white", font=('Arial', 24),
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_buttons_frame(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

root = tk.Tk()
calc = Calculator(root)
root.mainloop()

