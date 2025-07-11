import pytest # type: ignore
from survey import AnonymousSurvey
#test: saving result
@pytest.fixture #decorator
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey  = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response) #append to responses
    
    for response in responses:
        assert response in language_survey.responses