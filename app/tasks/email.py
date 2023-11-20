"""
Backend : tasks : email
=========================
This module contains the methods to process and send email.
"""
from email.message import EmailMessage


def send_email(
    subject: str,
    sender: str,
    recipent: str,
    body: str,
    attachments: dict,
) -> None:
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipent
    message.set_content(body)
    message.send