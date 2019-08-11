from model.training_models_meter import *
from db_init.training_db_initializer import TrainingDbInitializerMeter
import nltk
import math


class CalculateProbability:
    ngrams = {}

    def __init__(self, db_path):
        db_init = TrainingDbInitializerMeter(db_path)
        db = SqliteDatabase(db_path)
        db.connect()

        all_ngrams = NgramModel.select()

        for ngram in all_ngrams:
            self.ngrams[ngram.ngram] = ngram.count

        self.unigram_count = NumberOfGrams.get(NumberOfGrams.gram == 1).count
        self.bigram_count = NumberOfGrams.get(NumberOfGrams.gram == 2).count
        db.close()

    def load_ngrams(self, db_path):
        db_init = TrainingDbInitializerMeter(db_path)
        db = SqliteDatabase(db_path)
        db.connect()

        ngrams = {}

        all_ngrams = NgramModel.select()

        for ngram in all_ngrams:
            ngrams[ngram.ngram] = ngram.count

        db.close()
        return ngrams

    def calculate_probability(self, password_text):
        password_text_list = list(password_text)
        unigrams = nltk.ngrams(password_text_list, 1)
        bigrams = nltk.ngrams(password_text_list, 2)

        unigrams_list = []

        for gram in unigrams:
            unigrams_list.append(gram[0])

        bigrams_list = []

        for gram in bigrams:
            bigrams_list.append("" + gram[0] + gram[1])

        probability_result = 0

        first_character_count = self.ngrams[unigrams_list[0]]

        probability_result = probability_result + math.log2(first_character_count / self.unigram_count)


        for i in range(len(bigrams_list)):
            unigram_count = self.ngrams[unigrams_list[i]]
            bigram_count = 1
            try:
                bigram_count = self.ngrams[bigrams_list[i]]
            except Exception:
                pass
            probability_unigram = unigram_count / self.unigram_count
            probability_bigram = bigram_count / self.bigram_count

            probability_result = probability_result + math.log2(probability_bigram / probability_unigram)

        return abs(probability_result)

cp = CalculateProbability("database/n-gram.db")
print(cp.calculate_probability("Diplomski1234!"))