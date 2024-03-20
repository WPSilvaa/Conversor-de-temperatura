print ( "Bem vindo a Calculadora de IMC" )

pergunta_nome = input( "Qual é o seu nome?" ) 
print ( "Olá", pergunta_nome )
idade = input ( "Qual sua idade?" )
peso = float (input ( "Qual seu peso (em KG)? "))
altura  =  float ( input ( "Qual sua altura (em metros e usando ponto)? " ))

IMC = (peso / (altura * altura ))
print ( "Seu IMC é:", IMC )

if IMC < 16.9:
    print ( "Muito abaixo do peso" )
elif IMC < 18.4:
    print ( "Abaixo do peso" )
elif IMC < 24.9:
    print ( "Peso normal" )
elif IMC < 29.9:
    print ( "Acima do peso" )
elif IMC < 34.9:
    print ( "Obesidade grau I" )
elif IMC < 39.9:
    print ( "Obesidade grau II" )
else:
    print ( "Obesidade grau III" )


  
