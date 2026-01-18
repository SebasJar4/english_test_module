class QuestionResult:
    def __init__(self, question, user_answer, time_spent):
        self.question = question
        self.user_answer = user_answer
        self.time_spent = time_spent

    @property
    def is_correct(self):
        return self.user_answer == self.question.answer

