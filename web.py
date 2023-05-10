from bottle import route, run, template
from bib import metros_para_centimetros


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/ex1/<metros:float>')
def ex1_route(metros):
    cm = metros_para_centimetros(metros)
    return template('{{cm}} cm', cm=cm)

from bib import cal_salario

@route('/ex2/<horas:int>/<valor_hora:float>')
def ex2_route(horas, valor_hora):
    salario = cal_salario(horas, valor_hora)
    return template('R${{s}}' , s=salario)

from bib import conv_celsius, imc, multa, preco_total

@route('/ex3/<temp_f:float>')
def ex3_route(temp_f):
    conversao = conv_celsius(temp_f)
    return template('R${{c}}' , c=conversao)

@route('/ex4/<peso:float>/<altura:float>')
def ex4_route(peso, altura):
    imc_v = imc(peso, altura)
    return template('{{imc}}' , imc=imc_v)

@route('/ex5/<peso:float>')
def ex5_route(peso):
    v_multa = multa(peso)
    return template('{{v_multa}}' , v_multa=v_multa)

@route('/ex6/<trabalhoHora:float>/<horaMes:float>')
def ex6_route(trabalhoHora, horaMes):
    salario = cal_salario(trabalhoHora, horaMes)
    return template('R${{salario}}' , salario=salario)

@route('/ex7/<area:float>')
def ex7_route(area):
    preco_final = preco_total(area)
    return template('R${{preco_final}}' , preco_final=preco_final)

run(host='localhost', port=8081)
