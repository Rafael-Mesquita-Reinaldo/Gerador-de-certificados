import pandas as pd # para ler o arquivo excel
from fpdf import FPDF #criação de arquivo excel(o que eu mais me adaptei)
from os import makedirs, path # criar e verificar pasta 
import qrcode #gerar o Qrcode
import logging # Para registrar logs do processo

# Configuração do logging para registrar ações e possíveis erros no arquivo 'certificado.log'
logging.basicConfig(level=logging.INFO,filename="certificado.log",format="%(asctime)s - %(message)s")# escolhi o format "asctime", para mostrar a hora e o dia que executou o programa e o "message" para mostrar a mensagem de possíveis erros

#Lendo o arquino do excel
dados = pd.read_excel('dados_participantes.xlsx')

#Verificar se a tabela tem as colunas necessarias para gerar o certificados
if "Nome do Participante" not in dados.columns or "Nome do Curso" not in dados.columns or "Data de Conclusão" not in dados.columns:
    print(" Não tem informações suficientes para gerar o certificado")
    logging.info("Não existe colunas suficientes para fazer o certificados,Verificar excel! ")
    exit(1)
#Verificando se os dados de cada aluno estão completos
for  index,aluno in dados.iterrows():
    if aluno.isna().any(): # nessa caso o "isna" vai verificar se existe alguma linha vazia e o "any" vai voltar o true ou false
        logging.info(f"A linha {index + 1} da tabela está com dado vazio, o certificado vai ser gerado com erro!")
    else:
        logging.info(f"Os dados do {aluno['Nome do Participante']} estão completos")

# verificando se a pasta foi criada
if not path.exists('certificados'):
    makedirs('certificados') # criando a pasta dos certificados
    logging.info("Pasta criada")


#Gerando os certificados
for  index,aluno in dados.iterrows():#iterar com cada linha da tabela
    nome = aluno["Nome do Participante"] #adicionando o nome do participante na variável
    curso = aluno["Nome do Curso"] #adicionando o curso do participante na variável
    data = aluno["Data de Conclusão"]#adicionando a data de conclusão do curso na variável
   
    #criando pdf
    if not path.isfile(f'certificados/certificado_{nome}.pdf'): # Para não duplicar certificados
        pdf = FPDF("P","mm","A4")
        pdf.add_page()
        # colocando o fundo azul
        pdf.set_draw_color(0,0,0) 
        pdf.rect(10,10,190,277) #formato da borda 
        #titulo do pdf
        pdf.ln(20)
        pdf.set_font("Times","B",size = 18)
        pdf.cell(0,10,"CERTIFICADO DE CONCLUSÃO",ln= True, align="C") #incluindo texto no pdf
        pdf.ln(20)
        #corpo do pdf
        pdf.set_font("Arial",size=12)
        pdf.cell(0,10,"Certificamos que",ln=True, align="C")
        
        pdf.set_font("Arial",size=15)
        pdf.cell(0,10,f"{nome}",ln=True, align="C")
        
        pdf.set_font("Arial",size= 10)
        pdf.multi_cell(0,10,f'Concluiu com sucesso  o cuso de {curso} no Centro Universitário Unieuro na data {data} ', align="C" )
        pdf.cell(0,10,"Parabens pela conclusão do curso!!",align= "C")
        
        #colocando a linha para assinatura  
        pdf.line(30, 250, 180, 250)
        pdf.text(87,255, "Assinatura do responsável",)
        # gerando Qrcode
        qr = qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(f"Certificado do aluno {nome}-curso {curso}-data de conclusão-{data}")
        qr.make(fit= True)
        
        #criando a imagem do Qrcode
        img = qr.make_image(fill='black',back_color ='white')
        img.save(f"certificados/Qrcode_{nome}.png")
        
        # adicionando o Qrcode no certificado
        pdf.image(f"certificados/Qrcode_{nome}.png",x=84, y=120, w=50, h=50)
        pdf.text(90,175," validação do certificado")
        #salvando o pdf na pasta 
        pdf.output(f"certificados/certificado_{nome}.pdf")
        logging.info(f"Certificado do {nome} gerado com sucesso!")
    else: 
        logging.info(f"O certificados do {nome} já existe!")
        