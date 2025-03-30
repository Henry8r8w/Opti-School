from models import setup_database, fetch_recipients
from send_email import send_email
#from visualization import plot_email_trends, plot_email_status

def main(plot = True):
    setup_database()
    recipients = fetch_recipients()

    if not recipients:
        print(" No recipients found in the db!")
        return  

    for recipient in recipients:
        recipient_email, company, representative = recipient[0], recipient[1], recipient[2]
        print(f"{recipient} is to be sent")
        if "@" not in recipient_email:
            print(f"invalid email detected. Skipping: {recipient_email} ")
            continue

        send_email(
            recipient_email=recipient_email,
            company=company,
            representative=representative,
            sender_name="YourName",
            subject="The Title You Will Be Sending",
            template_path="./assets/email_template.txt",
        )
    if plot:
        plot_email_status()

if __name__ == "__main__":
    main()
