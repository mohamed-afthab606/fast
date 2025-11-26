from fastapi import FastAPI
from pydantic import BaseModel
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")

class EmailRequest(BaseModel):
    email: str
    subject: str
    message: str


@app.post("/send-email")
def send_email(req: EmailRequest):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = req.email
        msg["Subject"] = req.subject

        msg.attach(MIMEText(req.message, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, req.email, msg.as_string())
        server.quit()

        return {"status": "success", "message": f"Email sent to {req.email}"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
