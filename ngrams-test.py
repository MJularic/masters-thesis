import nltk

dw_file = open("rockyou_utf8.txt")
lines = dw_file.readlines()


#unigram

letters = []
max = 1000000
i = 0
unigrams_list = []

for line in lines:
    list_line = list(line.strip())
    unigrams = nltk.ngrams(list_line, 1)

    for unigram in unigrams:
        appender = ""
        appender = appender + unigram[0]
        unigrams_list.append(appender)
    i = i + 1

    if i == max:
        break

freq_unigram = nltk.FreqDist(unigrams_list)
#print(freq_unigram.elements())


#keys = freq_unigram.keys()

#print(freq_unigram.N())
#for k in keys:
#    print(k)
#    print(freq_unigram.N() * freq_unigram.freq(k))


#exit(0)
#bigram
i = 0

bigrams_list = []
for line in lines:
    list_line = list(line.strip())
    bigrams = nltk.ngrams(list_line, 2)

    for bigram in bigrams:
        appender = ""
        appender = appender + bigram[0] + bigram[1]
        bigrams_list.append(appender)
    i = i + 1

    if i == max:
        break


freq_bigram = nltk.FreqDist(bigrams_list)


user_input = input("Enter password to evaluate: ")

list_user_input = list(user_input)

bigram_password = nltk.ngrams(list_user_input, 2)


blist_pass = []
for bigram_pass in bigram_password:
    app = ""
    app = app + bigram_pass[0] + bigram_pass[1]
    blist_pass.append(app)


res = 1
for i in range(len(blist_pass)):
    res = res * (freq_bigram.freq(blist_pass[i]) / freq_unigram.freq(list_user_input[i]))

res = res * freq_unigram.freq(list_user_input[0])

print("Result: " + str(res))