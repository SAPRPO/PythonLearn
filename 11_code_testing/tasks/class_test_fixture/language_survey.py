from survey import AnonymousSurvey

question = "What language did your first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' at any time you want to quit\n")
while(True):
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)
print("\nThank you to everyone who participated in survey!")
language_survey.show_results()
