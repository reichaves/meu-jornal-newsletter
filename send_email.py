from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from scraper_portal import *
from scraper_impresso import capa_jornal
from print_portal import *
from sys_date import get_date
import os

manchete_globo_com = link_globo_com()
manchete_g1 = link_g1()
manchete_valor = link_valor()
manchete_uol = link_uol()
manchete_folha = link_folha()
manchete_estadao = link_estadao()
manchete_oglobo = link_oglobo()
manchete_metropoles = link_metropoles()

data_completa = get_date()

impressa_links = capa_jornal()

anexo_g1 = print_g1()
anexo_globo_com = print_globo_com()
anexo_oglobo = print_oglobo()
anexo_uol = print_uol()

email = Mail(
      from_email = "meu.jornal.gabriela@gmail.com", 
      to_emails = ["gabriela.caesar.2019@gmail.com", "gabriela.caesar@g.globo", "carina.dourado@ebc.com.br"], 
      subject = f"""Meu jornal - {data_completa}""", 
      html_content = f"""<h1>Meu jornal - {data_completa}</h1>
      <h2>Projeto final de <a href='http://gabrielacaesar.com/' target='_blank'>Gabriela Caesar</a></h2>
      <h3>Este projeto apoia o jornalismo profissional. O acesso a informações muda vidas. Ajude a imprensa. Assine jornais, sites e revistas. Apoie grandes e pequenos veículos. Busque informações antes de opinar. Cheque informações antes de compartilhar.</h3>
      <h4>(versão 1.0)</h4>
      <h3>Manchete dos principais portais</h3>
      <p>Globo.com: {manchete_globo_com}</p>
      <p>g1: {manchete_g1}</p>
	<p>Valor: {manchete_valor}</p>
	<p>UOL: {manchete_uol}</p>
	<p>Folha: {manchete_folha}</p>
	<p>Estadão: {manchete_estadao}</p>
	<p>O Globo: {manchete_oglobo}</p>
	<p>Metrópoles: {manchete_metropoles}</p>
      </br>
      </br>
      <h3>Capa das versões impressas</h3>
      <p>Folha:</p><img src={impressa_links[0]}></br></br></br></br>
      <p>Estadão:</p><img src={impressa_links[1]}></br></br></br></br>
      <p>O Globo:</p><img src={impressa_links[2]}></br></br></br></br>
      <p>Valor:</p><img src={impressa_links[3]}>
      """
      )

email.attachment = [anexo_g1, anexo_globo_com, anexo_oglobo, anexo_uol]

SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
api = SendGridAPIClient(SENDGRID_API_KEY)
api.send(email)
