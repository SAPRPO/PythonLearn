class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question) #show question
    
    def store_response(self, new_response):
        self.responses.append(new_response) #save answer
    
    def show_results(self):
        """show all answers"""
        print("Survey results:")
        for r in self.responses:
            print(f'- {r}')
