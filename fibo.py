num = int(input("Digite um número: "))


fib1 = 0
fib2 = 1
fib_atual = 0


while fib_atual < num:
    fib_atual = fib1 + fib2
    fib1 = fib2
    fib2 = fib_atual

if fib_atual == num:
    print(num, "pertence à sequência de Fibonacci!")
else:
    print(num, "não pertence à sequência de Fibonacci!")
