### mensagem inicial
Bem-vindo/a!
Este projeto apoia o jornalismo profissional. O acesso a informações muda vidas. Ajude a imprensa. Assine jornais, sites e revistas. Apoie grandes e pequenos veículos. Busque informações antes de opinar. Cheque informações antes de compartilhar

### sobre
O **Meu jornal** é um serviço gratuito para facilitar o acesso ao jornalismo profissional

### autoria
gabriela caesar (com orientações de [Alvaro Justen - Turicas](https://github.com/turicas), Bernardo Vianna e Eduardo Cuducos)

### última atualização
12/01/2022

### como funciona
Você recebe uma newsletter todo dia, com as principais manchetes e capas de jornal

### o que já faz
- newsletter é disparada todo dia, às 5h
- envia as manchetes dos portais de notícias
- envia as capas da versão impressa dos jornais
- envia um print screen de 100vh de quatro portais

### tecnologia utilizada
- python
- heroku
- sendgrid
- apiflash
- requests
- lxml
- beautifulsoup4
- urllib3
- pybase64
- os 
- datetime
- flask

### próximas versões
- usa ``lxml`` em vez de ``beautifulsoup4`` no scraper_portal.py
- permite que a pessoa se cadastre na newsletter
- URL da imagem da capa dos jornais será própria

### abrangência
Scraper dos portais:        
globo.com, g1, Valor, UOL, Folha, Estadão, O Globo e Metrópoles

Scraper das capas dos jornais impressos:        
Folha, Estadão, O Globo e Valor
