from model.training_models_generator import *
from db_init.training_db_initializer import TrainingDbInitializerGenerator
import nltk
import os


class GetWordStatistic:

    def __init__(self, text_file, db_path):
        if os.path.exists(text_file):
            self.text_file = text_file
            self.db_path = db_path
            return
        print("Text file or db file does not exist!")

    def create_statistic(self, progress_bar_var=None, progress_bar=None):
        txt_file = open(self.text_file)
        text = txt_file.read()

        sentences = nltk.tokenize.sent_tokenize(text)

        main_iters = int(len(sentences))

        for i in range(main_iters):
            print("iter " + str(i) + "/" + str(main_iters))
            bigrams = nltk.ngrams(sentences[i].split(), 2)

            for gram in bigrams:
                word = gram[0]
                consequent_word = gram[1]
                self.store_to_db(word, consequent_word)

            if progress_bar_var is not None and progress_bar is not None:
                increment = int(100 / main_iters)
                progress_bar_var.set((i + 1) * increment)
                progress_bar.update()

        if progress_bar_var is not None and progress_bar is not None:
            progress_bar_var.set(0)
            progress_bar.update()

    def store_to_db(self, word, consequent_word):
        db_init = TrainingDbInitializerGenerator(self.db_path)
        db = SqliteDatabase(self.db_path)
        db.connect()
        db.create_tables([WordModel, ConsequentWordModel])

        word_id = None

        try:
            word_model = WordModel.get(WordModel.word == word)
            word_id = word_model.id

        except DoesNotExist:
            word_model = WordModel(word=word)
            word_model.save()
            word_id = word_model.id

        try:
            consequent_word_model = ConsequentWordModel.get((ConsequentWordModel.consequent_word == consequent_word) & (ConsequentWordModel.word_id == word_id))
            consequent_word_model.occurrence = consequent_word_model.occurrence + 1
            consequent_word_model.save()

        except DoesNotExist:
            consequent_word_model = ConsequentWordModel(consequent_word=consequent_word, occurrence=1, word_id=word_id)
            consequent_word_model.save()
