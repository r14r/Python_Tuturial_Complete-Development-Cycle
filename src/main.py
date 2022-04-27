from CalculatorLib import calculator


def main():

    sum=calculator.add(3,5)
    print(f"Sum of 3+5={sum}")

    print( calculator.fac(0))
    print( calculator.fac(1))
    print( calculator.fac(4))

    print( calculator.fac(-1))
    
if __name__ == "__main__":
    main()