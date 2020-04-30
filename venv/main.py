import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Abhi'
email['to'] = 'abhikhedekar4241@gmail.com'
email['subject'] = 'Automated mail'

email.set_content(html.substitute({'name': email['to']}), 'html')

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("abhikhedekar55@gmail.com", "mpcihwcbdzwaprwr")
    print("Successful Login")
    smtp.send_message(email)
    print("Successfully sent to " + email['to'])
