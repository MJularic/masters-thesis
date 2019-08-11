import random
import string


class AlphanumericMarkov:

    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    punctuation = string.punctuation
    digits = string.digits
    states = [0, 1, 2, 3]

    #state 0 = lower_case, state 1 = upper_case, state 2 = digits, state 3 = special_characters

    transition_matrix_default = [[1/4, 1/4, 1/4, 1/4],
                                 [1/4, 1/4, 1/4, 1/4],
                                 [1/4, 1/4, 1/4, 1/4],
                                 [1/4, 1/4, 1/4, 1/4]]

    def __init__(self, initial_state=None):
        secure_random = random.SystemRandom()

        if initial_state is None:
            self.state = secure_random.choice(self.states)
            return

        self.state = initial_state

    def generate_password(self, length):

        password = ''

        for i in range(length):
            secure_random = random.SystemRandom()
            new_state = secure_random.choices(self.states, self.transition_matrix_default[self.state], k=1)[0]

            if new_state == 0:
                password = password + secure_random.choice(self.lower_case_letters)
            if new_state == 1:
                password = password + secure_random.choice(self.upper_case_letters)
            if new_state == 2:
                password = password + secure_random.choice(self.digits)
            if new_state == 3:
                password = password + secure_random.choice(self.punctuation)

            self.state = new_state
        return password
