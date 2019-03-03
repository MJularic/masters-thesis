from peewee import *

database = SqliteDatabase(None)


class NgramModel(Model):

    ngram = CharField()
    count = IntegerField(default=0)

    class Meta:
        database = database


class NumberOfGrams(Model):

    gram = IntegerField()
    count = IntegerField()

    class Meta:
        database = database
