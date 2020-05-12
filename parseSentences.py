from nltk.tokenize import sent_tokenize,word_tokenize

text = "Good evening Mr. Mukam. How are you doing there and how is Japan? I hope to see you soon in Turkmenistan. Send me your contact."

print(sent_tokenize(text))

for i in word_tokenize(text):
    print(i)

