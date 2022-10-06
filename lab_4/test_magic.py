import functions_magic
from unittest import TestCase

""" TODO create a test case to test the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
class TestFunctionsMagic(TestCase):

    def test_generate_url_for_question(self):
        # check that expected URL is returned for an example question

        #  https://8ball.delegator.com/magic/JSON/ 
        example_question = 'Will I ever love again?'
        self.assertEqual('https://8ball.delegator.com/magic/JSON/Will I ever love again?', functions_magic.generate_url_for_question(example_question))


    def test_extract_answer_from_response(self):
        # create example dictionaries that match expected API response, check that the correct answer is extracted and returned

        magic_dictionary = {
            'question': 'Will it be sunny tomorrow?', 
            'answer': 'Yes', 
            'type': 'Affirmative'
            }

        self.assertEqual('Yes', functions_magic.extract_answer_from_response(magic_dictionary))

        # create example dictionaries with a different structure to the one returned from the API, check that the function returns None
        new_structure_dictionary = {}

