def add(a, b): 
 
    return a + b 
def subtract(a, b): 

    return a - b 
def main(): 
    print("🎯 Добро пожаловать в калькулятор!") 
     
    try: 
        num1 = float(input("Введите первое число: ")) 
        num2 = float(input("Введите второе число: ")) 
        operation = input("Выберите операцию (+, -): ") 
         
        if operation == '+': 
            result = add(num1, num2) 
            print(f"Результат: {num1} + {num2} = {result}") 
        elif operation == '-': 
            result = subtract(num1, num2) 
            print(f"Результат: {num1} - {num2} = {result}") 
        else: 
            print("❌ Неизвестная операция!")
         def multiply(a, b): 
         """Умножение двух чисел""" 
         return a * b 
         def divide(a, b): 
         """Деление двух чисел""" 
         if b == 0: 
         raise ValueError("Деление на ноль!") 
         return a / b 
         # Обновите функцию main():def main(): 
             print("🎯 Добро пожаловать в калькулятор!") 
              
             try: 
                 num1 = float(input("Введите первое число: ")) 
                 num2 = float(input("Введите второе число: ")) 
                 operation = input("Выберите операцию (+, -, *, /): ") 
                  
                 if operation == '+': 
                     result = add(num1, num2) 
                 elif operation == '-': 
                     result = subtract(num1, num2) 
                 elif operation == '*': 
                     result = multiply(num1, num2) 
                 elif operation == '/': 
                     result = divide(num1, num2) 
                 else: 
                     print("❌ Неизвестная операция!") 
                     return 
                      
                 print(f"Результат: {num1} {operation} {num2} = {result}") 
                      
             except ValueError as e: 
                 print(f"❌ Ошибка: {e}") 
             except ZeroDivisionError: 
                 print("❌ Ошибка: деление на ноль!")
             
    except ValueError: 
        print("❌ Ошибка: введите числа корректно!") 
if __name__ == "__main__": 
    main() 

