print("1 constant", True)
print("2 constant", False)
print("3 constant", None)
print(oct(5), f"є рівним {oct(5)}")
print(ord('a'), f"є рівним {ord('a')}")
#цикли і розгалуження
c = 5
print("Значить с=5" if c else "Значить с!=5")

list = ['54', c, '32']
for cicle in list :
    print(cicle)
#помилки
c1 = 'fff'
try:
    print("Що буде якщо c/c1", c/c1, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")
#функція і контекст-менеджер
pth = "README.md"
func = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", func)
with open(pth, 'a') as f_obj:
    f_obj.write(f'намагаюсь писати код. {func("Andrii", "Onufrak")}')
