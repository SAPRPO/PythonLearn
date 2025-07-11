from survey import AnonymousSurvey
#test: saving result

def test_store_single_response():
    question = "What language did you first learn to speak?"
    language_survey  = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response():
    question = "What language did you first learn to speak?"
    language_survey  = AnonymousSurvey(question)
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response) #append to responses
    
    for response in responses:
        assert response in language_survey.responses