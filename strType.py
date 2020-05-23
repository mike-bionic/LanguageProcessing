from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
# % matplotlib inline

bible = gutenberg.open('bible-kjv.txt')
bible = bible.readlines()
res = bible[:5]
print(res)

# sentence = "I love coding on python, because it gives me and enormous ability to use the Data processing!"

