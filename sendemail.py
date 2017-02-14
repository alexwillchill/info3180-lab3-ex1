import smtplib
from_addr = 'alexthegreatwilliams@gmail.com'
to_addr = 'alexthegreatwilliams@gmail.com'
from_name= 'Alex'
to_name='Alex'
subject= 'Wazzup!'
msg='Hows it going bruh'
message = """From: {from_name} <{from_addr}>
To: {to_name} <{to_addr}>

Subject: {subject}
{msg}
"""

message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)
# Credentials (if needed)
username = 'alexthegreatwilliams@gmail.com'
password = '{fvkjyklaojqewpgn}'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 