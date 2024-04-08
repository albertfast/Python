salaryJack = 5000
salaryAlbert = 4000
tax = 0.27

print(salaryJack - (salaryJack * tax))
print(salaryAlbert - (salaryAlbert * tax))

# Degisken Tanimlama Kurallari
# rakam ile baslayamaz  # 1number = 10 boyle yapilamaz
number1 = 40
number2 = 20
print(number1)
print(number2)
number1 += number2
print(number1)
number1 += 100
print(number1)

# Buyuk kucuk harf duyarliligi vardir

age = 25
AGE = 32

print(age)
print(AGE)

# Turkce karakter kullanmayalim

# x = 1
# y = 2.3
# name = "Albert"
# isStudent = True

x , y , name , isStudent = (2, 2.3, "Albert", True)  # 4 tane degiskene ayni anda atama yapmis olduk
print(x * y)
print(y)
print(name)
print(isStudent)
