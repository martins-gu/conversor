def converter_dolar_para_reais():
    try:
        cotacao_dolar = 5.69
        dolares = float(input("Digite o valor em dólares (USD): "))
        reais = dolares * cotacao_dolar
        print(f"{dolares} USD equivale a R$ {reais:.2f}")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def converter_real_para_dolar():
    try:
        cotacao_dolar = 5.69
        reais = float(input("Digite o valor em reais (BRL): "))
        dolares = reais / cotacao_dolar
        print(f"{reais} BRL equivale a US$ {dolares:.2f}")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def menu():
    while True:
        try:
            print("\nConversor de Moedas")
            print("[1] Converter Dólar para Real")
            print("[2] Converter Real para Dólar")
            print("[0] Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                converter_dolar_para_reais()
            elif opcao == '2':
                converter_real_para_dolar()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro inesperado no menu: {e}")

if __name__ == "__main__":
    menu()