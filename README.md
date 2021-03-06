### mensagem inicial
Bem-vindo/a!
Este projeto apoia o jornalismo profissional. O acesso a informações muda vidas. Ajude a imprensa. Assine jornais, sites e revistas. Apoie grandes e pequenos veículos. Busque informações antes de opinar. Cheque informações antes de compartilhar

### sobre
O **Meu jornal** é um serviço gratuito para facilitar o acesso ao jornalismo profissional

### autoria
gabriela caesar (com orientações de [Alvaro Justen - Turicas](https://github.com/turicas), Bernardo Vianna e Eduardo Cuducos)           
contato sobre o projeto: ``meu.jornal.gabriela@gmail.com`` e ``gabriela.caesar.2019@gmail.com``

### última atualização
13/01/2022

### como funciona
Você recebe uma newsletter todo dia, com as capas do jornal impresso e também com os prints e as manchetes dos principais portais de notícias

### o que já faz
- newsletter é disparada todo dia, às 7h
- envia as manchetes dos portais de notícias
- envia as capas da versão impressa dos jornais
- envia um print screen de 100vh de quatro portais

### tecnologia usada
- python
- heroku
- github

### bibliotecas usadas
- ``sendgrid``
- ``apiflash``
- ``requests``
- ``lxml``
- ``beautifulsoup4``
- ``urllib3``
- ``pybase64``
- ``os``
- ``datetime``
- ``flask``

### próximas versões
- usa ``lxml`` em vez de ``beautifulsoup4`` no scraper_portal.py
- permite que a pessoa se cadastre na newsletter
- URL da imagem da capa dos jornais será própria

### abrangência
Scraper dos portais:        
globo.com, g1, Valor, UOL, Folha, Estadão, O Globo e Metrópoles

Scraper das capas dos jornais impressos:        
Folha, Estadão, O Globo e Valor

Print screen dos portais:          
globo.com, g1, O Globo e UOL
