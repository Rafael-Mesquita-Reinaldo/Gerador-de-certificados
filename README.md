# Gerador de certificados
 Nesse projeto eu faço um script que faz a geração de certificados simples em pdf, através de dados que estão em uma tabela no excel, contendo a lista de participantes, cursos e datas de conclusão.
 ### Linguagem usada:
 + Python 3.8
### Requisitos para rodar o script:
#### Bibliotecas Necessárias:
+ pandas (para manipular o Excel)
+ os (para gerenciar arquivos e diretórios)
+ fpdf (para gerar PDFs)
+ logging (para registrar logs do processo)
+ qrcode (para criar QR Codes)
#### Como instalar:
+ pip install pandas fpdf qrcode
+ Ás outras já fazem parte do Python
### Como usar o script:
#### 1º Criar tabela no excel ( modelo de tabela no final do readme)
+ Com as sequintes colunas:
   + Nome do Participante
   + Nome do Curso
   + Data de Conclusão
+ Salva o arquivo com o nome "dados_participantes.xlsx" no formato ".xlsx"
#### 2º: Colocar o Arquivo na Mesma Pasta do Código
+ O script buscará automaticamente o arquivo na mesma pasta onde está sendo executado
 #### 3º: Executar o script
+ Escolher A IDE de sua preferência e execute o script
#### 4º: A Pasta dos Certificados e QR Codes será Criada Automaticamente
+ O script cria a pasta certificados/ para armazenar os PDFs
+ Cada certificado terá o nome certificado_NomeDoParticipante.pdf.
#### (opcional) 5º: Personalização
+ Se quiser pode mudar o nome das pastas manualmente, fica ao seu critério!
#### Obs: O arquivo do excel vai está no repositório junto com o código!
### O que tem no certificado:
+ Nome do participante
+  Nome do curso
+  Data de conclusão
+  Mensagem de congratulação
+  QR Code para validação
+  Linha para assinatura
### Alguns Recursos:
+ O script verifica automaticamente se o Excel tem todas as colunas necessárias
+ Se a pasta certificados/ não existir, o script cria automaticamente
+ Arquivos de log são salvos em certificado.log para monitoramento
+ O QR Code gerado contém os detalhes do certificado e pode ser usado para validação
+ Evita certificados duplicados: Se você adicionar mais participantes na planilha e executar o script novamente, ele só gerará os certificados que ainda não existem
### Possíveis Erros:
#### 1º:O arquivo Excel não tem as colunas necessárias:
+ Verifique se o Excel tem as colunas "Nome do Participante", "Nome do Curso" e "Data de Conclusão"
+ Corrija o nome das colunas se estiverem diferentes
#### 2º:O script não encontra o arquivo Excel:
+ Verifique se o caminho está correto e se o arquivo existe
#### 3º: Os PDFs não estão sendo gerados:
+ Verifique se o nome dos participantes não tem caracteres especiais
+ Tente rodar o script como administrador para evitar restrições de permissão
### Licença:
+ Este projeto é de uso livre para fins acadêmicos e profissionais.
### Exemplo de tabela no excel:
![Image](https://github.com/user-attachments/assets/c30d6f4c-6f1a-4d32-8f61-20671df9e27f)



 
 
 
