import os
import nltk
from model.training_models import *
from db_init.training_db_initializer import TrainingDbInitializer


class GetStatistic:

    def __init__(self, password_file, db_path):

        if os.path.exists(password_file):
            self.db_path = db_path
            self.password_file = password_file
            return

        print("Password file or db_path does not exist!")

    def create_statistic(self, n, progress_bar_var=None, progress_bar=None):
        pass_file = open(self.password_file)
        lines = pass_file.readlines()
        maximum = int(len(lines) / 30)

        main_iters = int(len(lines) / maximum)
        k = 0

        for i in range(main_iters):
            #print("Main iteration number: " + str(i))
            #print("k: " + str(k))
            #print("till: " + str((i+1)*maximum))

            parsed_n_grams = []

            for j in range(k, (i + 1) * maximum):
                list_line = list(lines[j].strip())

                ngrams = nltk.ngrams(list_line, n)

                for gram in ngrams:
                    appender = ""
                    for g in gram:
                        appender = appender + g
                    parsed_n_grams.append(appender)

            self.store_to_db(nltk.FreqDist(parsed_n_grams), n)

            if progress_bar_var is not None and progress_bar is not None:
                increment = int(90 / main_iters)
                progress_bar_var.set((i + 1) * increment)
                progress_bar.update()

            k = (i + 1) * maximum

        #print("Do the rest!")
        #print("From: " + str(main_iters * maximum))
        #print("To: " + str(len(lines)))

        parsed_n_grams = []

        for j in range(main_iters * maximum, len(lines)):
            list_line = list(lines[j].strip())

            ngrams = nltk.ngrams(list_line, n)

            for gram in ngrams:
                appender = ""
                for g in gram:
                    appender = appender + g
                parsed_n_grams.append(appender)

        self.store_to_db(nltk.FreqDist(parsed_n_grams), n)

        progress_bar_var.set(100)

    def store_to_db(self, freq, n):

        db_init = TrainingDbInitializer(self.db_path)
        db = SqliteDatabase(self.db_path)
        db.connect()
        db.create_tables([NgramModel, NumberOfGrams])

        keys = freq.keys()

        for k in keys:
            try:
                gram = NgramModel.get(NgramModel.ngram == k)
                num_of_occurences = freq.freq(k) * freq.N()
                num_of_occurences = int(round(num_of_occurences))
                gram.count = gram.count + num_of_occurences
                gram.save()
            except DoesNotExist:
                num_of_occurences = freq.freq(k) * freq.N()
                num_of_occurences = int(round(num_of_occurences))
                gram = NgramModel(ngram=k, count=num_of_occurences)
                gram.save()

        try:
            number_of_grams = NumberOfGrams.get(NumberOfGrams.gram == n)
            number_of_grams.count = number_of_grams.count + freq.N()
            number_of_grams.save()

        except DoesNotExist:
            number_of_grams = NumberOfGrams(gram=n, count=freq.N())
            number_of_grams.save()
