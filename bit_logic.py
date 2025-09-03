class BitFromTron:                 
    def __init__(self):
        self.what_bit_knows = ["tron", "creator", "mcp", "master control program", "flynn", "mother", "user", "alan", "dillinger", "yora", "program"]
       
    def user_asks_bit(self):
        question = input("BIT IS LISTENING... \n")
        if question == "exit" or question ==  "quit":
            end_of_line()
        elif question == "ext":
            print("Did you mean \"exit\"?")
            exit_question = input("Type Y/n: ")
            if exit_question == "Y":
                end_of_line()
            elif exit_question == "n":
                return self.bit_answer_user(question)
        else:
            return self.bit_answer_user(question)


    def does_bit_know(self, know_answer):
        if know_answer == True:
            return True 
        else:
            return False
            
    def bit_answer_user(self, question):
        answer = False
        for word in self.what_bit_knows:
            if word.lower() in question.lower():
                answer = True

        if self.does_bit_know(answer) == True:
            return "YES" 
        else:
            return "NO"


def critical_bit_error():
    print("<! BIT CRITICAL ERROR !>")
    print("END OF LINE")
    exit()


def end_of_line():
    print("END OF LINE")
    exit()
try:
    while True:
        bit = BitFromTron()
        print(bit.user_asks_bit())

except KeyboardInterrupt: 
    print("*USER USE OF CTRL+C,\n")
    print("END OF LINE*\n")

