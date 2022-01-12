### mensagem inicial
Bem-vindo/a!
Este projeto apoia o jornalismo profissional. O acesso a informações muda vidas. Ajude a imprensa. Assine jornais, sites e revistas. Apoie grandes e pequenos veículos. Busque informações antes de opinar. Cheque informações antes de compartilhar.

### sobre
O **meu jornal** é um serviço gratuito para facilitar o acesso ao jornalismo profissional pela newsletter Meu Jornal.

### autoria
gabriela caesar (com orientações de [Alvaro Justen - Turicas](https://github.com/turicas), Bernardo Vianna e Eduardo Cuducos)

### última atualização
12/01/2022

### o que já faz
- newsletter é disparada todo dia, às 5h
- envia as manchetes dos portais de notícias
- envia a capa da versão impressa dos jornais

### próximas versões
- usa ``lxml`` em vez de ``beautifulsoup4`` no scraper_portal.py
- permite que a pessoa se cadastre na newsletter
- enviar um print screen de 100vh de cada portal
- URL da imagem da capa dos jornais será própria

### como funciona
Você recebe um e-mail todo dia, com as principais manchetes.
Manchete é a chamada principal de um jornal impresso ou de um portal de notícias.

Para utilizar o serviço, você deve:
- cadastrar-se para receber as newsletters

Scraper dos portais abrange:
globo.com, g1, Valor, UOL, Folha, Estadão, O Globo e Metrópoles.

Scraper das capas dos jornais impressos abrange:
Folha, Estadão, O Globo e Valor
