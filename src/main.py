from CalculatorLib import calculator

def pythagoras(a, b):
    return calculator.sqr(a) + calculator.sqr(b)

def main():

    sum = calculator.add(3, 5)
    print(f"Sum of 3+5={sum}")

    print(f"Pythagors of 3 and 4 is {pythagoras(3,4)}")

    print(calculator.fac(0))
    print(calculator.fac(1))
    print(calculator.fac(4))

    # print(calculator.fac(-1))


if __name__ == "__main__":
    main()
