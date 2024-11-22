import colorama
import inspect

# для перегляду всіх атрибутів та методів модуля
print(dir(colorama))

# функція help() для отримання більш детальної інформації про модуль
help(colorama)

# для перегляду доступних методів у конкретному класі або об'єкті
print(inspect.getmembers(colorama))