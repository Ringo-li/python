import unittest
from survey import AnonymousSurvey

class TestSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        question = "What langua did you learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn("English", my_survey.responses)

    def test_store_three_reponse(self):
        """测试三个答案会被妥善保存"""
        question = "What language did you learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()