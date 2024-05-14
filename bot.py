import smtplib
from email.message import EmailMessage
import getpass   ### after opening your text editor install the packages first that is (smtplib) and import it 

favorite_emails = {
    'Your Favorite Person Eamil': 'Put their name here',
    'Your Favorite Person Eamil': 'Put their name here', ## You can add more persons,if you want.
}

def send_email(recipient_email, recipient_name, email_content , sender_email):
    server_mine = smtplib.SMTP("smtp.gmail.com",587)
    server_mine.starttls()
    server_mine.login(sender_email,sender_pass)
    message = EmailMessage()
    message.set_content(email_content)
    message['Subject'] = 'A message for you'
    message['From'] = sender_email
    message['To'] = recipient_email
    
    server_mine.send_message(message)
    print(f"Email sent successfully to {recipient_name} ({recipient_email})")
    server_mine.quit()

def main():
    try:
        email_content = input("Enter your message: ")


        print("List of Favorite Recipients:")
        for i, (email, name) in enumerate(favorite_emails.items(), 1):
            print(f"{i}. {name} ({email})")

        selection = int(input("Select a recipient by number (1, 2, etc.): "))
        recipient_email = list(favorite_emails.keys())[selection - 1]
        recipient_name = list(favorite_emails.values())[selection - 1]
        sender_email = 'Your Email Address'
        sender_pass = getpass.getpass("Enter your password: ")

        send_email(recipient_email, recipient_name ,email_content ,sender_email,sender_pass)
        
    except (IndexError,ValueError):
        print("invalid selection")
        
if __name__ == "__main__":
    main() 