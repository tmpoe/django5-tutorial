from dataclasses import dataclass
import datetime
from typing import Generic, TypeVar

from django.test import TestCase
from django.utils import timezone
from parameterized import parameterized

from ..models import Question

# Create your tests here.

_T = TypeVar('_T')

class Specification(Generic[_T]):
        def is_satisfied_by(self, other: _T) -> bool:
            ...

class QuestionModelWasPublishedRecentlyTests(TestCase):
    class PubDateFutureSpecification(Specification):
        def is_satisfied_by(self, other):
            return other is False
        
    class PubDateOldSpecification(Specification):
        def is_satisfied_by(self, other):
            return other is False
        
    class PubDateRecentSpecification(Specification):
        def is_satisfied_by(self, other):
            return other is True
        
    @dataclass
    class QuestionModelWasPublishedRecentlyTestCaseInput:
         pub_date: datetime
         author: str
         question_text: str

    @dataclass
    class QuestionModelWasPublishedRecentlyTestCaseExpectation:
        was_published_recently: Specification[bool]

    @parameterized.expand(
        [
            (
                QuestionModelWasPublishedRecentlyTestCaseInput(author='me', question_text='asd', pub_date=timezone.now() + datetime.timedelta(hours=1)),
                QuestionModelWasPublishedRecentlyTestCaseExpectation(was_published_recently=PubDateFutureSpecification())
            ),
            (
                QuestionModelWasPublishedRecentlyTestCaseInput(author='me', question_text='asd', pub_date=timezone.now() - datetime.timedelta(hours=6000)),
                QuestionModelWasPublishedRecentlyTestCaseExpectation(was_published_recently=PubDateOldSpecification())
            ),
            (
                QuestionModelWasPublishedRecentlyTestCaseInput(author='me', question_text='asd', pub_date=timezone.now() - datetime.timedelta(minutes=1)),
                QuestionModelWasPublishedRecentlyTestCaseExpectation(was_published_recently=PubDateRecentSpecification())
            )
        ],
        ids=[
             'Future pub date',
             'Old pub date',
             'Recent pub date',
        ]
    )
    def test_was_published_recently(
            self, test_case_input,
            test_case_expectation: QuestionModelWasPublishedRecentlyTestCaseExpectation
        ):
        """
        GIVEN: A Question object with a pub date
        WHEN: was published recently is called
        THAN: returns result according to specification
        """
        was_published_recently = Question(author=test_case_input.author, question_text=test_case_input.question_text, pub_date=test_case_input.pub_date).was_published_recently()
        self.assertTrue(test_case_expectation.was_published_recently.is_satisfied_by(was_published_recently))