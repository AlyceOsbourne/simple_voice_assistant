import os
from datetime import datetime
from collections import namedtuple
from random import choice

from dotenv import load_dotenv
from enum import Enum
from Levenshtein import distance

load_dotenv()

data = {
    'name': os.getenv('NAME', 'Alex'),
    'version': os.getenv('VERSION', '0.0.1'),
    'owner_name': os.getenv('OWNER_NAME', 'Alyce'),
}


class VoiceAction(
    namedtuple(
        'VoiceAction',
        [
            'input_patterns',
            'output_patterns',
            'format_function'
        ])):

    def distance(self, input_string):
        return min(distance(input_string, pattern) for pattern in self.input_patterns)

    @staticmethod
    def all():
        for action in VoiceAction.__subclasses__():
            if issubclass(action, Enum):
                for _action in action.__members__.values():
                    yield _action.value
            else:
                yield action

    @staticmethod
    def closest(input_string, min_distance=3):
        closest, dist = None, min_distance
        for act in VoiceAction.all():
            act_dist = act.distance(input_string)
            if act_dist < dist:
                closest, dist = act, act_dist

        return closest

    def __call__(self, input_string):
        return choice(self.output_patterns).format(self.format_function(input_string))


class VoiceActions(
    VoiceAction,
    Enum
):
    TellTime = ('What time is it', 'What is the time', 'Tell me the time'), \
               ('The time is {}', 'It is currently {}'), \
               lambda *args: datetime.now().strftime('%H:%M')

    TellDate = ('What date is it', 'What is the date', 'Tell me the date'), \
               ('The date is {}', 'It is currently {}'), \
               lambda *args: datetime.now().strftime('%d %B %Y')

    TellName = ('What is your name', 'Tell me your name', 'Who are you'), \
               ('My name is {}', 'I am {}', 'I am called {}', 'Folks call me {}', 'I like to be known as {}'), \
               lambda *args: data['name']

    Greeting = ('Hello', 'Hi', 'Hey', 'What\'s up', 'Hey there', 'Hi there', 'Hello there', 'Hey there'), \
               ('Hello {}', 'Hi {}', 'Hey {}', 'What\'s up {}', 'Hey there {}', 'Hi there {}', 'Hello there {}'), \
               lambda *args: data['owner_name']

    TellVersion = ('What is your version', 'Tell me your version', 'What version are you running?'), \
                  ('My version is {}', 'I am currently on version {}', 'I am on version {}'), \
                  lambda *args: data['version']
