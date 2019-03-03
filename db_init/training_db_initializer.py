from model.training_models_meter import *
from model.training_models_generator import *


class TrainingDbInitializerMeter(object):

    def __init__(self, db_path):
        NgramModel._meta.database.init(db_path)
        NumberOfGrams._meta.database.init(db_path)


class TrainingDbInitializerGenerator(object):

    def __init__(self, db_path):
        WordModel._meta.database.init(db_path)
        ConsequentWordModel._meta.database.init(db_path)
