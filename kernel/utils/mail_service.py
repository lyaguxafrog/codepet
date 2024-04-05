# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.settings import (
    SMTP_PORT,
    SMTP_PASSWORD,
    SMTP_SERVER,
    SMTP_USER
)
from fundraising.models import Payment


def send_email_about_payment(
        payment: Payment
        ) -> None:
    """
    Сервис отправки сообщений об оплате

    :param payment: Объект платежа, откуда берется информация

    :return: None
    """
    collect_name = payment.pay_to.collect_name
    payment_sum = payment.sum
    payer_email = payment.payer.email

    # создаем сообщение
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = payer_email
    msg['Subject'] = "Оплата прошла успешно"

    body = f"Оплата прошла успешно, Вы пожертвовали {payment_sum} в {collect_name}"
    msg.attach(MIMEText(body, 'plain'))

    # отправляем сообщение
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, payer_email, msg.as_string())
            print(f"Email sent to {payer_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

