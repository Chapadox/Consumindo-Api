#Consumindo Api de Clima da https://hgbrasil.com
#Feito Por Eduardo Santos
#Comentei as linhas para melhor entendimento

#importa a biblioteca de requests
import requests


print('''
##################################
                                #
                                #
     Consulte o Clima           #
                                #
                                #
#################################                               
''')

# Token de Acesso
token = input('Digite Seu Token: ')

if token == '':
    print('Por Favor Digite Um Token De Acesso')
    exit()
    
# Cidade Para Consulta de Clima
cidade = input('Digite uma Cidade/Estado:  ')

if cidade == '':
    print('Por Favor Digite Uma Cidade')
    exit()

# Url Passando os parametros da busca 
url = 'https://api.hgbrasil.com/weather?&key=' + token
url_2 = 'https://api.hgbrasil.com/weather?fields=only_results,temp,city_name,date,description,currently&city_name=' + cidade + '&key=' + token


#request Na URL e Tambem No Json
request = requests.get(url= url)
request_2 = requests.get(url_2) 
json = request.json()
json_2 = request_2.json()


#Validando Token
a = json['valid_key']
if a == False:
    print('Token Invalido')
    exit()

#Informaçoes Do json 
print('\n' 'Nome Da Cidade: {}'.format(json_2['city_name']))
print('Temperatura: {}'.format(json_2['temp']))
print('Data: {}'.format(json_2['date']))
print('Descrição: {}'.format(json_2['description']))
print('Atualmente: {}'.format(json_2['currently']))