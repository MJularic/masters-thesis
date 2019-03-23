from model.training_models_meter import *
from db_init.training_db_initializer import TrainingDbInitializerMeter
import nltk
import math


class CalculateProbability:

    def __init__(self, db_path):
        self.db_path = db_path

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

        db_init = TrainingDbInitializerMeter(self.db_path)
        db = SqliteDatabase(self.db_path)
        db.connect()

        num_of_unigrams = NumberOfGrams.get(NumberOfGrams.gram == 1)
        unigrams_count = num_of_unigrams.count

        num_of_bigrams = NumberOfGrams.get(NumberOfGrams.gram == 2)
        bigrams_count = num_of_bigrams.count

        probability_result = 0

        first_character = NgramModel.get(NgramModel.ngram == unigrams_list[0])

        probability_result = probability_result + math.log2(first_character.count / unigrams_count)

        for i in range(len(bigrams_list)):
            unigram = NgramModel.get(NgramModel.ngram == unigrams_list[i])
            bigram = NgramModel.get(NgramModel.ngram == bigrams_list[i])

            probability_unigram = unigram.count / unigrams_count
            probability_bigram = bigram.count / bigrams_count

            probability_result = probability_result +  math.log2(probability_bigram / probability_unigram)

        print("Score for password: " + str(password_text) + " is " + str(abs(probability_result)))
        return abs(probability_result)
