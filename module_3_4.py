def single_root_words(root_word = '' , *other_words):
    same_words = []
    for i in other_words:
        root_word_l = root_word.lower()
        i_l = i.lower()
        if i_l.count(root_word_l):
            same_words.append(i)
        if root_word_l.count(i_l):
            same_words.append(i)
    return same_words


result1 = single_root_words( 'rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)