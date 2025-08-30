

class BitFromTron:
    def __init__(self):
        self.what_bit_knows = ["tron", "creator", "mcp", "master control program", "flynn", "mother", "user"]

    def user_asks_bit(self):
        question = input("Bit is listening: ")
        return self.bit_answer_user(question)

    def does_bit_know(self, know_answer):
        if know_answer == True:
            return True
        else:
            return False

    def bit_answer_user(self, question):
        answer = False
        for w in self.what_bit_knows:
            if w.lower() in question.lower():
                answer = True

        if self.does_bit_know(answer) == True:
            return "YES" 
        else:
            return "NO"

bit = BitFromTron()
print(bit.user_asks_bit())
