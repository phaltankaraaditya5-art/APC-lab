from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer, correct_answer):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self, answer, correct_answer):
        return answer == correct_answer


class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer, correct_answer):
        return answer == correct_answer


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer, correct_answer):
        return correct_answer.lower() in answer.lower()


mcq = MCQQuestion()
tf = TrueFalseQuestion()
desc = DescriptiveQuestion()

print(mcq.evaluate_answer("A", "A"))
print(tf.evaluate_answer("True", "True"))
print(desc.evaluate_answer("Python is a programming language", "programming"))