print("=== Bem-vindo ao Restaurante===")

nome = input("Por favor, informe seu nome: ")

quantidade_pessoas = input("Quantas pessoas estarão na reserva? ")

data_reserva = input("Para qual data deseja reservar? (ex: 08/07/2025): ")
horario_reserva = input("Qual horário deseja reservar? (ex: 19:30): ")

mesas = [None] * 15

while True:
    print("\nMesas:")
    for i in range(15):
        status = "Livre" if mesas[i] is None else "Reservada"
        print(f"{i+1}:{status}", end="  ")

    print("\n\n1-Reservar 2-Cancelar 3-Sair")
    op = input("Opção: ")

    if op == "1":
        num =  int(input("Mesa (1-15): "))
        if mesas[num-1] is None:
            mesas[num-1] = "Reservada"
            print("Mesa reservada!!")
        else:
            print("Já está reservada.")

    elif op == "2":
        num = int(input("Mesa (1-15): "))
        if mesas[num-1] is not None:
            print("Reserva cancelada!!")
        else:
            print("Mesa já está livre.")

    elif op == "3":
        break

    else:
        print("Opção inválida.")



print(f"Nome: {nome}")
print(f"Número de pessoas: {quantidade_pessoas}")
print(f"Data: {data_reserva}")
print(f"Horário: {horario_reserva}")
print("\n.")

