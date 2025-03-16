# Gerador de certificados
 Nesse projeto eu faço um script que faz a geração de certificados simples em pdf, através de dados que estão em uma tabela no excel, contendo a lista de participantes, cursos e datas de conclusão.
 ### Linguagem usada:
 + Python 3.8
### Requisitos para rodar o script:
#### Bibliotecas:
+ Pandas
+ OS
+ fpdf
+ logging
+ qrcode
#### Como instalar:
+ pip install pandas fpdf qrcode
+ Ás outras já fazem parte do Python
### Como usar o script:
+ Criar tabela no excel ( modelo de tabela no final do readme)
+ Com as sequintes colunas:
   + Nome do Participante
   + Nome do Curso
   + Data de Conclusão
+ Salva o arquivo com o nome "dados_participantes.xlsx"
+ No formato ".xlsx"
+ Colocar o arquivo "dados_participantes.xlsx" na mesma pasta do código antes de rodar o script
+ A pasta onde vai ficar o certificados e o QRCode vai ser criada automaticamente ao rodar o script
+ Escolher A IDE de sua preferência e execute o script
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
+ Mesmo adicionando outra pessoa na tabela e executar o script de novo, não vai gerar certificados duplicados, apenas de certificados que não existe ainda
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



 
 
 
