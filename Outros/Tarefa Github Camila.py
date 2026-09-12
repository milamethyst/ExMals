def main():
    print("=== CALCULADORA ===")
    user_input = input("Digite a operação que deseja realizar (utilize +, -, / e x): ")

    operation_type = 0

    for operation in "+-/x":
        if operation in user_input:
            num1, operation_type, num2 = user_input.partition(operation)
            num1 = int(num1)
            num2 = int(num2)
            break

    result = 'inválido'

    match operation_type:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '/':
            if num2 != 0:
                result = num1 / num2 
        case 'x':
            result = num1 * num2
        case default:
            print("Operação inválida!", end=' ')
    
    print(f"O resultado é {result}")

main()