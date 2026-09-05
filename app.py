# Programa de calculadora de consumo elétrico inteligente
# Autor: Davi Cardoso

# Entrada
nome = input("digite o nome do aparelho: ")
potencia = int(input("potência do aparelho em watts: "))
horasDia = int(input("tempo médio de uso diário em horas: "))

# Processamento
consumo_kwh = (potencia * horasDia * 30) / 1000
custoTotal = (potencia * horasDia * 30) / 1000 * 0.83

# Saída 
print(f"O consumo mensal do(a) {nome} é de {consumo_kwh} kWh.")
print(f"Custo mensal do {nome} é de {custoTotal}")
