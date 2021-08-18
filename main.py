import sys
import smtplib, ssl, time, psutil
import subprocess

# SERVER CONFIG
smtp_server = "smtp.gmail.com"
port = 465 # FOR SSL
# GMAIL CONFIG
sender_email = "mail@gmail.com"
password = input("Type your password for email ",sender_email,": ")
email_reciver = ["michalfurmanczak@gmail.com"]

message = """\
Subject: Server Warning.

You recive this message because, CPU or RAM usage is too high and this might be problem for correct work of application. Plese check it out."""

def main():
    while True:
        if(psutil.virtual_memory().percent >= 70.0):
            sendWarning(False)
        elif(psutil.cpu_percent() >= 70.0):
            sendWarning(True)

        print("Accual Memory Usage Is ", psutil.virtual_memory().percent)
        time.sleep(10) # CHECK PER 10 SECOUND.

def sendWarning(isCPU):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for simple_email in email_reciver:
            server.sendmail(sender_email, simple_email, message)

    # TODO:Add a command line to start linux cpu limit program.
    # if(isCPU):
    #     subprocess.Popen("")

if(__name__) == '__main__':
    try:
        main()
    except MemoryError:
        sys.stderr.write("Maximum Memory Exceeded")
        sys.exit(-1)
