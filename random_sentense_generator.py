import random

def random_word(words):
    return random.choice(words)


names = ["Maria", "Ivan", "Angel", "Violeta", "Gergana"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the sea", "at home", "in the park"]

input("Hello to your first random sentence!")

while True:
    random_name=random_word(names)
    random_place=random_word(places)
    random_verb=random_word(verbs)
    random_noun=random_word(nouns)
    random_adverb=random_word(adverbs)
    random_detail=random_word(details)

    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}')
    input("Click [Enter] to generate new one!")

