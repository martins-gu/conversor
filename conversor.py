def converter_dolar_para_reais():
    cotacao_dolar = 5.69
    dolares = float(input("Digite o valor em dólares (USD): "))
    reais = dolares * cotacao_dolar
    print(f"{dolares} USD equivale a R$ {reais:.2f}")

def converter_real_para_dolar():
    cotacao_dolar = 5.69
    reais = float(input("Digite o valor em reais (BRL): "))
    dolares = reais / cotacao_dolar
    print(f"{reais} BRL equivale a US$ {dolares:.2f}")

def menu():
    while True:
        print("\nConversor de Moedas")
        print("[1] Converter Dólar para Real")
        print("[2] Converter Real para Dólar")
        print("[0] Sair")
        opcao = input("Escolha Uma opção: ")

        if opcao == '1':
            converter_dolar_para_reais()
        elif opcao =='2':
            converter_real_para_dolar()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    menu()