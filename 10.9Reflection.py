Devowel

#%%

def devowel(Phrase):
    List = list(Phrase)
    vowel = ["a", "e", "i", "o", "u"]
    for letter in List:
        if letter.lower () in vowel:
            List.remove(letter)
    Phrase = ''.join(List)
    return Phrase