def previsao_energia_solar(dia):
    energia_solar = {
        1: 9.5,
        2: 8.2,
        3: 7.0,
        4: 6.5,
        5: 9.0,
        6: 5.0,
        7: 10.0
    }
    # Retorna a previsão correspondente ao dia ou 0 caso o dia seja inválido
    return energia_solar.get(dia, 0)


def controlar_dispositivos(energia_solar, dispositivos_usados):
    dispositivos = {
        "Luz": 0.5,
        "Aquecedor": 2.0,
        "Eletrodoméstico": 1.5,
        "Ventilador": 0.3,
        "Micro-ondas": 1.2,
        "Computador": 0.8,
        "TV": 1.0
    }

    total_consumo = 0

    for dispositivo, horas_uso in dispositivos_usados.items():
          # Calcula o consumo de cada dispositivo
        if dispositivo in dispositivos:
            consumo_dispositivo = dispositivos[dispositivo] * horas_uso
            total_consumo += consumo_dispositivo
             # Mostra o consumo detalhado para cada dispositivo
            print(f"Você consumiu {consumo_dispositivo:.2f} kWh com o(a) {dispositivo} por {horas_uso} horas.")

    return total_consumo


def gerenciamento_energia():
    while True:
          # Solicita ao usuário o dia que deseja consultar
        dia_atual = input("Informe o dia da semana (1 - Segunda, 2 - Terça, ..., 7 - Domingo) ou 0 para sair: ")

        if dia_atual == '0':
               # Encerra o programa se o usuário digitar 0
            print("Programa encerrado.")
            break

        if dia_atual.isdigit():
            dia_atual = int(dia_atual)
            if dia_atual < 1 or dia_atual > 7:
                print("Dia inválido! Por favor, digite um número entre 1 e 7.")
                  # Valida se o dia informado está entre 1 e 7
                continue
           # retorna a previsão de energia solar para o dia informado
            energia_solar = previsao_energia_solar(dia_atual)
            print(f"\nPrevisão de energia solar para hoje (dia {dia_atual}): {energia_solar:.2f} kWh")

            dispositivos_usados = {}
            for dispositivo in ["Luz", "Aquecedor", "Eletrodoméstico", "Ventilador", "Micro-ondas", "Computador", "TV"]:
                horas_uso = input(f"Quantas horas você usou o(a) {dispositivo} hoje? ")
                if horas_uso.isdigit():
                    horas_uso = int(horas_uso)
                    dispositivos_usados[dispositivo] = horas_uso
                else:
                    # Se o usuário inserir um valor inválido, assume 0 horas
                    print("Entrada inválida! Por favor, insira um número válido de horas.")
                    dispositivos_usados[dispositivo] = 0
             # Calcula o consumo total com base nos dispositivos usados
            total_consumo = controlar_dispositivos(energia_solar, dispositivos_usados)

              # Compara o consumo total com a previsão de energia solar
            print(f"\nTotal de energia consumida hoje: {total_consumo:.2f} kWh")
            if total_consumo <= energia_solar:
                print("Parabéns! O seu consumo está dentro da previsão de energia solar.")
                   # Mensagem de erro para entrada inválida
            else:
                print(f"Você excedeu a previsão de energia solar em {total_consumo - energia_solar:.2f} kWh.")

            print("-" * 50)
        else:
            print("Entrada inválida! Por favor, insira um número.")


gerenciamento_energia()
