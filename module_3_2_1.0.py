def send_email(message, recipient, *, sender = "universityhelp@gmail.com"):
    if not "@" in recipient or not "@" in sender:
        return print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    domains = ".com", ".ru", ".net"
    if recipient.endswith(domains) and sender.endswith(domains):
        if recipient == sender:
            return print("Нельзя отправить письмо самому себе!")
        if sender == "universityhelp@gmail.com":
            return  print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        if sender != "universityhelp@gmail.com":
            return print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    else:
        return print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
