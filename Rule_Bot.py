import re
import random

class Rule_Bot_by_Somesh:
    Negative_Response = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    Exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    Random_questions = (
        "Why are you here?\n",
        "Are there many humans like you?\n",
        "What do you consume for sustenance?\n",
        "Does Earth have a leader?\n",
        "What planets have you visited?\n",
        "What Technology do you have on this planet?\n"
    )
    def __init__(self):
       self.alienbabb = {
           'describe_about_planet_intent': r'.*\s*your planet.*', 
           'answer_why_intent': r'why\sare.*', 
           'about_Somesh_Raj': r'.*\s*Somesh_Raj.*'
        }

    def Greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am a Rule-Bot. Will you help me learn about your planet?\n")
        if will_help in self.Negative_Response:
            print("\nOkay, Let's just chat then!")
            return
        self.chat()
    def make_exit(self, reply):
        for command in self.Exit_commands:
            if reply == command:
                print("Okay, have a nice day!")
                return True
    def chat(self):
        reply = input(random.choice(self.Random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
    def match_reply(self, reply):
        for key, value in self.alienbabb.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_about_planet_intent':
                return self.describe_about_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_Somesh_Raj':
                return self.about_Somesh_Raj()
        if not found_match:
            return self.no_match_intent()
    def describe_about_planet_intent(self):
        responses = ("My Planet is Pluto.\n", 
                     "It is is a dwarf planet in the Kuiper belt.\n",
                     "A ring of bodies beyond the orbit of Neptune.\n", 
                     "It is the ninth-largest and tenth-most- massive known object to directly orbit the Sun.\n", 
                     "It is the largest known trans-Neptunian object by volume, by a small margin, but is slightly less massive than Eris.\n")
        return random.choice(responses)
    def answer_why_intent(self):
        responses = ("I come in peace.\n",
                     "I'm here to collect data on your planet and its inhabitant.\n",
                     "I heard the coffee is good.\n")
        return random.choice(responses)
    def about_Somesh_Raj(self):
        responses = ("He's a smart boy went from a small village named Bhadai which is situated in Muzaffarpur City in Bihar.\n",
                     "Right Now he's currently pursuing his career in B-Tech in Electrical Engneering From Haldia Institute Of Technology, and Currently he's in final year of his course.\n",
                     "He's an Aspiring Electrical Engineer and Python Developer.\n",
                     "He's an adept Electrical Engineer with a fervor for Python Programming. Skillfully merging engineering precision with coding creativity.\n")
        return random.choice(responses)
    def no_match_intent(self):
        responses = (
            "Please tell me more.\n, Tell me more!.\n", "Why do you say that?\n", "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n", "I see. How do you think?\n", "Why?\n",
            "How do you think I feel when you say that?\n")
        return random.choice(responses)
RuleBot = Rule_Bot_by_Somesh()
RuleBot.Greet()