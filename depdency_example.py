#  In an email notification system, the "EmailSender" class may depend on the "SMTPServer" class to send emails. The "EmailSender" class has a dependency on the "SMTPServer" class to fulfill its functionality.

# B
class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send(self, message):
        print("sending message from {} to {}".format(message.sender, message.receiver))

# A
class EmailSender:
    def send_email(self, message, smtp_server):
        smtp_server.send(message)

def main():
    smtp_server = SMTPServer("smtp.google.com", 587)
    email_sender = EmailSender()
    email_sender.send_email("Hello world", smtp_server)

main()

