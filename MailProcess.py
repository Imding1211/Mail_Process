#==============================================================================
# 2022/09/29
# Gmail
# Username: ServerProcess55
# Password: Cbdch101632
#==============================================================================

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os.path
import sys

mailto = sys.argv[1]
PID = sys.argv[2]

run = True

content = MIMEMultipart()
content["subject"] = "Process notification"
content["from"] = "ServerProcess55"
content["to"] = mailto 
content.attach(MIMEText("Process PID: "+str(PID)+" done."))

while run:
	if not os.path.exists("/proc/"+PID):

		with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
			try:
				smtp.ehlo()
				smtp.starttls()
				smtp.login("serverprocess55@gmail.com", "rgtrvikzzpdysxei")
				smtp.send_message(content)
				#print("Complete!")
			except Exception as e:
				pass
				#print("Error message: ", e)
				
		run = False