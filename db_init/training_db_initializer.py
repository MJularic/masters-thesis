from model.training_models import *


class TrainingDbInitializer(object):

    def __init__(self, db_path):
        NgramModel._meta.database.init(db_path)
        NumberOfGrams._meta.database.init(db_path)
