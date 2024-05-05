# Escreva um programa que leia a velocidade de um carro., se ele utrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$7,00 por cada km acima do limite.


velocidade = float(input("Digite a velocidade do carro em km/h: "))

limite = 80 
if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f"Você foi multado! A multa é de R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")