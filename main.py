from mailjet_rest import Client
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import base64

# =============================
# Carregar variáveis do .env
# =============================
load_dotenv()
api_key = os.getenv("MAILJET_API_KEY")
api_secret = os.getenv("MAILJET_API_SECRET")
remetente = os.getenv("REMETENTE")

destinatarios = ["emailExemplo1@email.com","emailExemplo2@email.com"]
# Data e hora formatados
agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

assunto = f"📊 Relatório de Logs - {agora.split()[0]}"

mensagem_html = f"""
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <p>Prezado(a),</p>

    <p>Segue o relatório de <strong>logs do sistema</strong>, gerado automaticamente.</p>

    <p><b>Dados da geração:</b><br>
       📅 Data: {agora.split()[0]}<br>
       ⏰ Hora: {agora.split()[1]}
    </p>

    <p>Este documento contém registros de eventos, alertas e informações úteis para a análise de desempenho.</p>

    <p>Caso precise de suporte adicional, responda diretamente a este e-mail.</p>

    <br>
    <p>Atenciosamente,<br>
       <b>Sistema de Gestão de Logs</b><br>
       Departamento de Tecnologia da Informação</p>
  </body>
</html>
"""

# =============================
# Pasta de logs
# =============================
BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# Pega todos os arquivos da pasta logs
arquivos_log = list(LOGS_DIR.glob("*.log"))

attachments = []
for log_file in arquivos_log:
    with open(log_file, "rb") as f:
        encoded_file = base64.b64encode(f.read()).decode()
        attachments.append({
            "ContentType": "application/octet-stream",
            "Filename": log_file.name,
            "Base64Content": encoded_file
        })
        print(f"✅ Anexado: {log_file.name}")

# =============================
# Enviar via Mailjet
# =============================
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

data = {
    'Messages': [
        {
            "From": {"Email": remetente, "Name": "Sistema de Logs"},
            "To": [{"Email": email} for email in destinatarios],
            "ReplyTo": {"Email": remetente},  # 🔑 Dá credibilidade
            "Subject": assunto,
            "TextPart": "Segue em anexo o relatório de logs do sistema.",
            "HTMLPart": mensagem_html,
            "Attachments": attachments
        }
    ]
}

result = mailjet.send.create(data=data)

if result.status_code == 200:
    print("📧 E-mail enviado com sucesso via Mailjet!")
else:
    print(f"❌ Erro ao enviar e-mail: {result.status_code} - {result.json()}")
