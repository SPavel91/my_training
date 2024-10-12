com = "moc."
ru = "ur."
net = "ten."
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    m = 0
    q = 0
    w = 0
    r = 0
    for i in recipient:
        if i == "@":
            break
        if i != "@":
            continue
    for j in sender:
        if j == "@":
            break
        if j != "@":
            continue
    if i == j == "@":
        m = 1
    if com == recipient[:-5:-1]:
        q = 1
    if ru == recipient[:-4:-1]:
        q = 1
    if net == recipient[:-5:-1]:
        q = 1
    if com == sender[:-5:-1]:
        w = 1
    if ru == sender[:-4:-1]:
        w = 1
    if net == sender[:-5:-1]:
        w = 1
    if q + m + w != 3:
        r = 1
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    if recipient == sender:
        r = 1
        print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        if r != 1:



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')