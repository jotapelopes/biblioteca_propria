def metros_para_centimetros(metros):
    return metros * 100

def ex1():
    metros = float(input('Insira um valor em metros para ser convertido: '))
    cm = metros_para_centimetros(metros)
    print(cm)

def cal_salario(horas, valor_hora):
    return horas * valor_hora

def ex2():
    horas = int(input('Insira quantas horas você trabalha no mês: '))
    valor_hora = float(input('Insira o valor hora: '))
    salario = cal_salario(horas, valor_hora)
    print(salario)

def conv_celsius(temp_f):
    return (temp_f - 32) / 1.8

def ex3():
    temp_f = float(input('Insira o valor em Fahrenheit que deseja converter em Celsius: '))
    conversao = conv_celsius(temp_f)
    print(conversao)

def imc(peso, altura):
    return peso / altura ** 2

def ex4():
    peso = float(input('Insira o seu peso: '))
    altura = float(input('Insira a sua alutra: '))
    imc_v = imc(peso, altura)
    print(imc_v)


def multa(peso):
    return (peso - 30) * 3

def ex5():
    peso = float(input("Informe o peso, em quilos, de peixe: "))
    if peso > 30:
        quilo_exc = quilo_exc(peso)
        v_multa = multa(quilo_exc)
        print(v_multa)
    else:
        v_multa == 0
        print('Não teve multa')

def ex6():
    trabalhoHora = float(input("Quanto você ganha por hora? R$"))
    horaMes = float(input("Quantas horas você trabalha em um mês? "))
    salario = cal_salario(trabalhoHora, horaMes)
    liquido = salario * 0.0088
    print(liquido)

def preco_total(area):
    return ((area / 3) / 18) * 80

def ex7():
    area = float(input("Informe a área que deseja-se pintar, em m²: "))
    preco_final = preco_total(area)
    print(preco_final)
