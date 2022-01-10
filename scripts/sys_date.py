from datetime import date

def get_date():
  today = date.today()
  dia_hoje = today.strftime("%d/%m/%Y")
  dia_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
  dia_da_semana = dia_semana[today.weekday()].lower()
  data_completa = f"""{dia_da_semana}, {dia_hoje}"""
  return data_completa
