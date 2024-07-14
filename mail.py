
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "chetan1915017@gndec.ac.in"
you = "dawinder2001.b@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Sample email"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHello Dudi \n Hope the pant you purchased yesterday is good for you \n BYE DUDU"
#html = open('sample_html_email.html').read()

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
#part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
#msg.attach(part2)

# Send the message via local SMTP server.
#s = smtplib.SMTP('smtp.gmail.com.')
smtpserver = smtplib.SMTP("mail.gndec.ac.in", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login('chetan1915017@gndec.ac.in', '@Ajey!2636')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
smtpserver.sendmail(me, you, msg.as_string())
print("done")
smtpserver.quit()