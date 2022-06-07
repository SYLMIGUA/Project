#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import formataddr

EMAIL_HTML_TEMPLATE="""<html>
                  <head>
                  </head>
                  <body>
                    <p style ="margin: 5px 0;line-height: 25px;">Bonjour {},<br>
                    <br>
                    Ceci est un mail au format html.
                    <br>
                    {}
                    <br>
                    Bien à vous,<br>
                    {} <br>
                    </p>
                  </body>
                </html>
                """


class EmailSenderClass:

    def __init__(self):
        """ """
        self.logaddr = "testlabs220@gmail.com"
        self.fromaddr = "testlabs220@gmail.com"# alias
        self.password = "<220@Test"#


    def sendMessageViaServer(self,toaddr,msg):
        # Send the message via local SMTP server.
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.logaddr, self.password)
        text = msg.as_string()
        server.sendmail(self.fromaddr, toaddr, text)
        server.quit()
            
                

    def sendHtmlEmailTo(self,destName,destinationAddress,msgBody):
        #Message setup
        msg = MIMEMultipart()
         
        msg['From'] =  "Me<"+self.fromaddr+">"
        msg['To'] = "testlabs221@gmail.com"
        msg['Subject'] = "Hello mail"
        
        hostname=sys.platform
        
            
        txt = EMAIL_HTML_TEMPLATE
        
        txt=txt.format(destName,msgBody,hostname)
        
        #Add text to message
        msg.attach(MIMEText(txt, 'html'))
        
        print("Send email from {} to {}".format(self.fromaddr,destinationAddress))
        self.sendMessageViaServer(destinationAddress,msg)



if __name__ == "__main__":
    email= EmailSenderClass()
    email.sendHtmlEmailTo("Admin","testlabs221@gmail.com","Ceci est un mail automatique envoyé à partir d'un script Python.")
