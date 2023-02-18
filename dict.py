#!/usr/bin/env python3
import time
import requests
import json
from termcolor import colored

def unofficial_mariam_webster():
    word = str(input("Enter a word to lookup in the dictionary: ")).strip()
    response = requests.get(f'https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=<YOUR_MARIAM_WEBSTER_API_KEY>')
    # print(response.text)
def dictionary_api_official_call():
    word = str(input("Enter a word to lookup in the dictionary: ")).strip()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    content = response.text
    arr = json.loads(content)
    obj = arr[0]
    meanings = obj["meanings"]
    print("Definitions:")

    no_of_meanings = len(meanings)
    partsOfSpeech = ['interjection', 'verb', 'noun', 'pronoun', 'adjective', 'adverb', 'preposition', 'conjunction']
    for i in range(no_of_meanings):
        for partOfSpeech in partsOfSpeech:
            if (partOfSpeech == meanings[i]['partOfSpeech']):
                print(f"When it is a {meanings[i]['partOfSpeech']}, {word} means: '{meanings[i]['definitions'][0]['definition']}'") #\n Synonyms: {meanings[i]['synonyms']},\n Anthonyms: {meanings[i]['antonyms']}.\n")
    
    if "phonetic" in obj.keys():
        print(f"Pronounciation: {obj['phonetic']}")
    elif "phonetics" in obj.keys():
        # Solution 1
        #if len(obj['phonetics']) == 0: print("Pronounciation: not found")
        #else:
        #    print(f"Pronounciation: {obj['phonetics'][1]['text']}")
        # Solution 2 (better)
        try:
            print(f"Pronounciation: {obj['phonetics'][1]['text']}")
        except IndexError:
            print("Pronounciation: not found")


counter = time.perf_counter()

def main():
    try:
        dictionary_api_official_call()
    except KeyError:
        print(colored("That is not a real word... Try again"))
        main()

if __name__ == "__main__":
    main()

#if counter > 5:
#    print("It seens like the official api is down... Downgrading to Mariam-Webster....")
#    unofficial_mariam_webster()


#print(f"When it is a {obj['meanings'][1]['partOfSpeech']}, {word} means {obj['meanings'][0]['definitions'][0]['definition']},\n Synonyms: {obj['meanings'][0]['synonyms']},\n Anthonyms: {obj['meanings'][0]['antonyms']}.\n")
#print(f"When it is a {obj['meanings'][0]['partOfSpeech']}, {word} means {obj['meanings'][0]['definitions'][0]['definition']},\n Synonyms: {obj['meanings'][0]['synonyms']},\n Anthonyms: {obj['meanings'][0]['antonyms']}.")
#print(f"When it is a {obj['meanings'][0]['partOfSpeech']}, {word} means {obj['meanings'][0]['definitions'][0]['definition']},\n Synonyms: {obj['meanings'][0]['synonyms']},\n Anthonyms: {obj['meanings'][0]['antonyms']}.")
#print(f"When it is a {obj['meanings'][0]['partOfSpeech']}, {word} means {obj['meanings'][0]['definitions'][0]['definition']},\n Synonyms: {obj['meanings'][0]['synonyms']},\n Anthonyms: {obj['meanings'][0]['antonyms']}.")
