import os
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
import google.generativeai as genai
from dotenv import load_dotenv

# Read .env file
load_dotenv()

# IMAP server login credentials
IMAP_SERVER = os.getenv('IMAP_SERVER')
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
# SMTP server settings
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = 587

def fetch_new_mail():
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(USERNAME, PASSWORD)

    # Select the mailbox you want to access (e.g., 'INBOX')
    mail.select('INBOX')

    # Search for emails based on criteria (e.g., 'UNSEEN' for unread emails)
    status, data = mail.search(None, 'UNSEEN')

    # Get the list of email IDs
    email_ids = data[0].split()

    # Setup Gemini AI
    genai.configure(api_key = os.getenv('GEMINIAI_KEY'))
    model = genai.GenerativeModel('gemini-pro')

    # Loop through each email ID and fetch the corresponding email
    for email_id in email_ids:
        status, data = mail.fetch(email_id, '(RFC822)')
        raw_email = data[0][1]

        # Parse the raw email data
        msg = email.message_from_bytes(raw_email)

        # Extract relevant information from the email
        subject = msg['Subject']
        sender = msg['From']

        # Iterate through the email parts to extract the content
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                response = model.generate_content(part.get_payload(decode=True).decode('utf-8'))
                reply = response.text

                send(USERNAME, sender, 'Re: '+subject, reply)

            print('No new email.')

    # Close the connection to the IMAP server
    mail.logout()


def send(sender, recipient, subject, message):
    # Create the email message
    msg = MIMEText('Hi,\n\n' + message + '\n\nBest,\nIngenius.')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Connect to the SMTP server
    smtp_conn = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_conn.starttls()

    # Login to the SMTP server
    smtp_conn.login(USERNAME, PASSWORD)

    # Send the email
    smtp_conn.sendmail(sender, recipient, msg.as_string())

    print('Reply sent.')

    # Close the connection to the SMTP server
    smtp_conn.quit()


if __name__ == '__main__':
    fetch_new_mail()