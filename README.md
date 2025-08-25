# mailjet-automation

Projeto em Python que implementa a automação do envio de e-mails utilizando a API do Mailjet.
O sistema simula um cenário de monitoramento de logs de banco de dados, permitindo o envio automático de notificações por e-mail com os registros coletados.

Este projeto foi desenvolvido com Python 3.12.7, garantindo compatibilidade com as últimas funcionalidades da linguagem.

## Passo a passo

## Crie o ambiente virtual
O ambiente virtual do Python serve para isolar as dependências de cada projeto, evitando conflitos entre pacotes e versões. 
Na pasta do seu projeto, execute:

#### Linux/Mac:
```python
python3 -m venv venv
```

#### Windows:
No windows por questão de seguraçã tem uma Execution Policy (Política de Execução) que define quais scripts podem ser executados no sistema. Por padrão, em muitas versões do Windows, essa política é configurada como Restricted, que não permite rodar nenhum script (.ps1), justamente para evitar que scripts maliciosos sejam executados automaticamente, protegendo o usuário de vírus ou alterações não autorizadas.

Para contornar isso basta usar o comando:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Após iniciar o ambiente virtual normalmente:
```python
python -m venv venv
```

Isso cria uma pasta chamada venv/ com os binários e libs do projeto.

## Ative o ambiente virtual

#### Linux/Mac:
```python
source venv/bin/activate
```
#### Windows (PowerShell):
```python
.\venv\Scripts\Activate
```

## Instale as dependências
```python
pip install -r requirements.txt
```

## Configurando chaves de acesso (```.env```)
Você consegue a API Key e o API Secret criando uma conta gratuita no Mailjet. <br>

####  Disponível em https://www.mailjet.com/
Depois de confirmar seu e-mail e acessar o painel, vá até:
```Account Settings > API Key Management```. 
Lá o Mailjet já fornece uma chave pública (API Key) e uma chave privada (API Secret), que são usadas para autenticar suas requisições. O campo REMETENTE deve ser preenchido com o e-mail remetente que você validou previamente na plataforma (em Senders & Domains), pois o Mailjet só permite envio a partir de endereços confirmados

Os dados obtidos deve ser informados no arquivo ```.env``` contendo:
- MAILJET_API_KEY= **************
- MAILJET_API_SECRET= ***********
- REMETENTE= seuEmail@email.com
#### Após alterar as credenciais por motivos de segurança, adicione o arquivo ```.env``` ao ```.gitignore```.”


##  Configurando o arquivo ```main.py```
Para o envio correto é necessário informar os email destinatário na declaração:
```python
destinatarios = ["emailExemplo1@email.com","emailExemplo2@email.com"]
``` 

## Executar programa principal
Dentro do ambiente virtual (venv):

#### Linux/Mac:
```python
python3 main.py
```

#### Windows:
```python
python main.py
```

## Observações:
E-mails enviados por este sistema através do Mailjet podem ser classificados como **Spam** ou **Promoções** em alguns provedores (ex: Gmail, Outlook).  
 
 Para evitar isso, recomenda-se:  
- Validar e autenticar o domínio e remetente no painel do Mailjet (SPF, DKIM e DMARC).  
- Usar endereços de remetente corporativos (ex.: `no-reply@seudominio.com`) em vez de e-mails pessoais (Gmail, Hotmail, etc.).  
- Pedir ao destinatário para marcar o remetente como "Confiável" ou "Não é Spam".  

## Sair com ambiente virtual
Para desativar o ambiente virtual quando não for mais usar:
```python
deactivate
```

