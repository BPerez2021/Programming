#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Labs\LabTwo'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Lab 2 Part 1: Using Python to Analyze Texts
#  The first portion of this lab will involve applying concepts from the in-class exercise in order to perform common analyses. Complete any cells that are marked as ON YOUR OWN.
#%% [markdown]
# 
#  First, you will need to install some dependencies:
# 
#  
#  - Install BSD-DB according to the instructions here:
#  https://github.com/c-w/Gutenberg
#

#  - Next, we'll install a library for downloading texts from gutenberg via pip. After selecting the appropriate shell for Anaconda, type the following into the terminal:
#  
#  ```bash
#  pip install gutenberg


###### My Error: Command "python setup.py egg_info" failed with error code 1 in C:\Users\BR057071\AppData\Local\Temp\3\pip-install-vf9h6wqt\bsddb3\
# Typed in to google
# Some Websites:
#       https://stackoverflow.com/questions/35991403/pip-install-unroll-python-setup-py-egg-info-failed-with-error-code-1
#               pip install --upgrade setuptools
#                       Could not install packages due to an EnvironmentError: [WinError 5] Access is denied: 'c:\\programdata\\miniconda3\\lib\\site-packages\\__pycache__\\easy_install.cpython-37.pyc' Consider using the `--user` option or check the permissions.
#               pip install ez_setup
#                       no error message; attemped pipinstall gutenberg again
#                               Error message popped up again (see "My Error")
#               easy_install -U setuptools
#                       error: [WinError 5] Access is denied: 'C:\\ProgramData\\Miniconda3\\Scripts\\easy_install-script.py'
#       https://askubuntu.com/questions/975523/pip-install-gives-command-python-setup-py-egg-info-failed-with-error-code-1#  
#  Classmate helped and now it has been successfully installed, may have down some steps backwards          
#  
# 
# 
# - Finally, install TextBlob and necessary corpora:
#  ```na;j
#  pip install -U textblob
#  python -m textblob.download_corpora
#  ```

#%%
# Let's begin by downloading and using the version of Moby Dick published on Project Gutenberg.
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

text = strip_headers(load_etext(2701)).strip()
blob = TextBlob(text)
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
# This will save the text to a local .txt file in this directory.
source = open('Labs/mobydick.txt','w',encoding="utf-16",newline='\n')
source.write(text)
source.close()


#%%
type(text)


#%%
blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])


#%%
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)


#%%
from operator import itemgetter  

d = blob.word_counts
for key, value in sorted(d.items(), key = itemgetter(1), reverse = True):
    print(key, value)


#%%
max = 0
index = 0
# Find the longest sentence in the work
for key, sentence in enumerate(blob.sentences):
    if(len(sentence.words) > max):
        max = len(sentence.words)
        index = key


#%%
# Find the longest word in the work
max = 0
for key, word in enumerate(blob.words):
    if(len(word) > max):
        max = len(word)
        index = key
print(max)
print(blob.words[index])

#%% [markdown]
# # Parts of Speech
# 
# Another method Montfort described is to use the tags to count certain parts of speech. Below is an example that uses a single sentence, but the same could be applied to a full manuscript.

#%%

pride = TextBlob('''It is a truth universally acknowledged, 
that a single man in possession of a good fortune, must be in 
want of a wife.''')


#%%
def adjs(pride):
    count = 0
    for (word, tag) in pride.tags:
        if tag == 'JJ':
            count = count + 1
    return count


#%%
adjs(pride)

#%% [markdown]
# # Creating Figures
# There are many ways to create figures. Below is one example of a table. You can save the figure to a file. 
# 
# ```
# conda install -c plotly
# ```

#%%
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ])
fig.show()

#%% [markdown]
# # Lab 2

#%%
# [2-1] ON YOUR OWN:

# Choose a text that was not previously analyzed above from Project Gutenberg.
# 1. Write code that retrieves and writes the text to a file in the current project. You may save it to any file, but I recommend to save it to the lab2 subdirectory.
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

text = strip_headers(load_etext(1065)).strip()
blob = TextBlob(text)
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
# This will save the text to a local .txt file in this directory.
source = open('Labs/TheRaven.txt','w',encoding="utf-16",newline='\n')
source.write(text)
source.close()

#%%
# 2. Write code that retrieves the text (if downloaded) and saves it to a variable. 
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

text = strip_headers(load_etext(1065)).strip()
blob = TextBlob(text)
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
# This will save the text to a local .txt file in this directory.
source = open('Labs/TheRaven.txt','w',encoding="utf-16",newline='\n')
source.write(text)
source.close()
print(text)


#%%
# 3. Create a TextBlob from the variable above. This may involve locating the end of the header. 
# Save the resulting TextBlob for use in the following cells. 
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

text = strip_headers(load_etext(1065)).strip()
blob = TextBlob(text)
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
# This will save the text to a local .txt file in this directory.
source = open('Labs/TheRaven.txt','w',encoding="utf-16",newline='\n')
source.write(text)
source.close()
book = TextBlob(text)
#print(book)
#Used https://textblob.readthedocs.io/en/dev/quickstart.html#get-word-and-noun-phrase-frequencies for assistance
book.words.count('tapping')



#%%
# [2-2] ON YOUR OWN:

# Write code that finds the top 5 longest sentences in the work. You may store or display them however you choose, and you may build off of the code above that finds the longest sentence.
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

text = strip_headers(load_etext(1065)).strip()
blob = TextBlob(text)
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
# This will save the text to a local .txt file in this directory.
source = open('Labs/TheRaven.txt','w',encoding="utf-16",newline='\n')
source.write(text)
source.close()
max = 6
index = 0
for key, sentence in enumerate(blob.sentences):
    if(len(sentence.words) > max):
        max = len(sentence.words)
        index = key
        print(sentence)
#Only provided 4 sentences even though I request 5 and even attempted to request 6 sentences to test
#%%
# [2-3] ON YOUR OWN:

# Using the code above for figures, create a new table that lists the top 10 most frequent words and how many times they occur in that text.
#Don't have the knowledge nor the ability to make tables
#Used Lab Computers
