import time

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.results = []
        self.start_time = time.time()

    def add_result(self, result):
        self.results.append(result)

    def total_time(self):
        return int(time.time() - self.start_time)

    def score(self):
        return sum(r.is_correct for r in self.results)

    def percentage(self):
        return round((self.score() / len(self.questions)) * 100, 2)

