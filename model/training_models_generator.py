from peewee import *

database = SqliteDatabase(None)


class WordModel(Model):
    word = CharField()

    class Meta:
        database = database


class ConsequentWordModel(Model):
    consequent_word = CharField()
    occurrence = IntegerField(default=0)
    word_id = IntegerField()

    class Meta:
        database = database
