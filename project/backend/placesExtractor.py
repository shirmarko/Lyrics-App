import nltk
import os
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

class PlacesExtractor:
    def __init__(self):
        pass

    def find_places_in_lyrics(self, lyrics):
        st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz','stanford-ner.jar',encoding='utf-8')
        tokenized_text = word_tokenize(lyrics)
        classified_text = st.tag(tokenized_text) # tagging the words of the song
        ner_places = []
        for i in range(0, len(classified_text) - 1):
            if classified_text[i][1] == 'LOCATION': # filter just the LOCATION words
                if classified_text[i + 1][1] == 'LOCATION':
                    ner_places.append(classified_text[i][0].translate({ord('.'): None}) + " " +
                                    classified_text[i + 1][0].translate({ord('.'): None}))
                    i += 1
                else:
                    ner_places.append(classified_text[i][0].translate({ord('.'): None}))
        copy_places = ner_places.copy()
        for place in ner_places:
            splitted = place.split()
            for word in splitted:
                first_ch = word[0]
                if not first_ch.isupper():
                    copy_places.remove(place)
                    break

        return list(set(copy_places))

