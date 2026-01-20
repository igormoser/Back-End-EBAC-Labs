print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

while True:
        opcao = input("Digite o número da operação desejada: ").strip()
        if opcao not in ["1", "2", "3", "4"]:
            print("Operação inválida, Tente novamente.")
            continue
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida, digite apenas números!")
            continue

        if opcao == "1":
            print("Resultado:", num1 + num2)
        elif opcao == "2":
            print("Resultado:", num1 - num2)
        elif opcao == "3":
            print("Resultado:", num1 * num2)
        elif opcao == "4":
            if num2 == 0:
                print("Sem divisão por zero!")
            else:
                print("Resultado:", num1 / num2)

        while True:
            continuar = input("Deseja continuar? [S/N] ").strip().lower()
            if continuar in ["s", "n"]:
                break
            print("Opção inválida, Tente novamente.")

        if continuar == "n":
            print("Saindo do programa...")
            break