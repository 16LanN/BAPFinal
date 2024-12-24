import pandas as pd

df = pd.read_json('text.json') #Название вашего json файла

def prefix_function(prefix):
    prefix_index = [0] * len(prefix)
    counter = 0

    for i in range(1, len(prefix)):
        while counter > 0 and prefix[i] != prefix[counter]:
            counter = prefix_index[counter - 1]

        if prefix[i] == prefix[counter]:
            counter += 1
        prefix_index[i] = counter
    return prefix_index


def kmp(text, target):
    prefix = prefix_function(target)
    pos = []
    counter = 0

    for i in range(len(text)):
        while counter > 0 and text[i] != target[counter]:
            counter = prefix[counter - 1]

        if target[counter] == text[i]:
            counter += 1
        if counter == len(target):
            pos.append(i - counter + 1)
            counter = prefix[counter - 1]
    return pos

for i in range(len(df)):

    text = df['text'][i]
    target = df['target'][i]

    print(f'Шаблон "{target}" в тексте "{text}", встречается на позициях: {kmp(text, target)}')