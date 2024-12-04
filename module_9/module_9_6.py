def all_variants(text):
    length = len(text)
    text_ = ""
    index = 1
    for i in range(length):
        yield text[i]
        text_ += text[i]

    for j in range(length):
        try:
            yield text[j] + text_[index]
            index += 1
        except IndexError:
            yield text_


a = all_variants("abc")
for i in a:
    print(i)