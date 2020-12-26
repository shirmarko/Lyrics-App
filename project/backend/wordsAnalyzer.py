import nltk
import os
import string
import matplotlib
import re
import numpy as np
from PIL import Image
import multidict as multidict
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from wordcloud import WordCloud,STOPWORDS

nltk.download("stopwords")
nltk.download("punkt")
matplotlib.use('Agg')
class WordsAnalyzer:
    def __init__(self):
        self.stop_words = nltk.corpus.stopwords.words("english") + list(string.punctuation) \
        + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) \
        + list(['--']+["''"]+["``"]+[".."]+["..."]+["ii"]+["iii"]+["iv"]+["'s"]+["n't"]+["'re"]+["\'ll"]+["ya\'"]+["\'m"])

    def getFrequencyDictForText(self,sentence):
        fullTermsDict = multidict.MultiDict()
        tmpDict = {}

        # making dict for counting frequencies
        for text in sentence.split(" "):
            val = tmpDict.get(text, 0)
            tmpDict[text.lower()] = val + 1
        for key in tmpDict:
            fullTermsDict.add(key, tmpDict[key])
        return fullTermsDict


    def makeImage(self,text, names):
        d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        music_mask = np.array(Image.open(os.path.join(d, "music_musk.jpeg")))
        wc = WordCloud(width = 3000, height = 2000, random_state=1, background_color="black", colormap='Pastel1', collocations=False, mask=music_mask)
        # generate word cloud
        wc.generate_from_frequencies(text)
        wc.to_file("wordCloud.png")
        # show
        plt.figure(figsize=(10, 10))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        title = 'The Best'
        if len(names)==1:
            title+= "Song is:\n"
        else:
            title += f' {len(names)} Songs Are:\n '
        
        for i in range(0,len(names)):
            if i == (len(names)-1):
                title += names[i]
            else:
                title += names[i]+" \n "
        plt.title(title)
        plt.savefig("wordCloud.png")


    def create_word_cloud(self, data, names):
        data = data.lower()
        data = nltk.word_tokenize(data)
        data_filter = [w for w in data if not w in self.stop_words]
        words = ' '.join(data_filter)
        self.makeImage(self.getFrequencyDictForText(words), names)


    def create_statistics(self, data, title):
        data = data.lower()
        data = nltk.word_tokenize(data)
        data_filter = [w for w in data if not w in self.stop_words]
        freq_words = Counter(data_filter).most_common()
        # filter the words that appear just one time
        freq_words = [tup for tup in freq_words if tup[1]>1]  
        keys= [tup[0] for tup in freq_words]
        freqs = [tup[1] for tup in freq_words]

        # Figure Size 
        fig, ax = plt.subplots(figsize =(16, 9)) 
        # Horizontal Bar Plot 
        ax.barh(keys, freqs) 
        # Remove axes splines 
        for s in ['top', 'bottom', 'left', 'right']: 
            ax.spines[s].set_visible(False) 
        # Remove x, y Ticks 
        ax.xaxis.set_ticks_position('none') 
        ax.yaxis.set_ticks_position('none') 
        # Add padding between axes and labels 
        ax.xaxis.set_tick_params(pad = 5) 
        ax.yaxis.set_tick_params(pad = 10) 
        # Add x, y gridlines 
        ax.grid(b = True, color ='grey', 
                linestyle ='-.', linewidth = 0.5, 
                alpha = 0.2) 
        # Show top values  
        ax.invert_yaxis() 
        
        # Add annotation to bars 
        for i in ax.patches: 
            plt.text(i.get_width()+0.2, i.get_y()+0.5,  
                    str(round((i.get_width()), 2)), 
                    fontsize = 10, fontweight ='bold', 
                    color ='grey') 
        
        # Add Plot Title 
        ax.set_title(f'Lyrics Frequencies Graph\n\nThe song name is: \"{title}\""', 
                    loc ='left' ) 
        
        # Add Text watermark 
        fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12, 
                color ='grey', ha ='right', va ='bottom', 
                alpha = 0.7) 
        
        # Show Plot 
        plt.savefig("statistics.png")

