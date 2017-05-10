def main():
    try:
        numbers = input("Enter two integers,"
                "separated by a comma: ").split(',')
        number1 = int(numbers[0])
        number2 = int(numbers[1])
        result = number1 / number2
        print("Result is " + str(result))
    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("A comma may be missing in the input")
    except:
        print("Something wrong in the input")
    else:
        print("No exceptions")
    finally:
        print("The finally clause is executed")
main()