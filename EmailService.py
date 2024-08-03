import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    @staticmethod
    def send_welcome_email(to_email):
        password = os.getenv("EMAIL_PASSWORD")
        from_email = os.getenv("EMAIL_USERNAME")

        if not password or not from_email:
            raise ValueError("Email credentials are not set in environment variables.")

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Welcome to EmpowerU!'

        html_content = """
            <html>
            <body>
                <h2>Dear User,</h2>
                <p>Welcome to <b>EmpowerU</b>! We are excited to have you on board.</p>
                <p>Feel free to explore our platform and discover amazing courses and resources.</p>
                <p>If you have any questions or need assistance, don't hesitate to reach out to us.</p>
                <br/>
                <p>Best regards,<br/>The EmpowerU Team</p>
            </body>
            </html>
        """
        msg.attach(MIMEText(html_content, 'html'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.send_message(msg)
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
            raise