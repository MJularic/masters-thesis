from model.training_models_generator import *
from db_init.training_db_initializer import TrainingDbInitializerGenerator
import random


class WordMarkov:

    def __init__(self, db_path):
        self.db_path = db_path
        self.secure_random = random.SystemRandom()

    def generate_password(self, length):
        db_init = TrainingDbInitializerGenerator(self.db_path)
        db = SqliteDatabase(self.db_path)
        db.connect()

        password = ""
        choice = " "
        generated = 0

        while generated < length:

            try:
                word = WordModel.get(WordModel.word == choice)
                id = word.id
                choice = self.get_consequent_word(id)
                password = password + " " + choice
                generated = generated + 1

            except DoesNotExist:
                random_id = self.secure_random.randint(1, 27260)
                word = WordModel.get_by_id(random_id)
                choice = self.get_consequent_word(random_id)
                if generated == 0:
                    password = password + word.word
                    password = password + " " + choice
                    generated = generated + 2
                else:
                    password = password + " " + word.word
                    generated = generated + 1
                    if generated >= length:
                        break

                    password = password + " " + choice
                    generated = generated + 1

        return password

    def get_consequent_word(self, id):
        consequent_words = ConsequentWordModel.select().where(ConsequentWordModel.word_id == id)
        consequent_words_list = list(consequent_words)

        next_words = []
        occurrence = []

        for w in consequent_words_list:
            next_words.append(w.consequent_word)
            occurrence.append(w.occurrence)

        choice = self.secure_random.choices(next_words, occurrence, k=1)[0]

        return choice


wm = WordMarkov("/home/mj/diplomski-rad/database/word.db")
print(wm.generate_password(4))
