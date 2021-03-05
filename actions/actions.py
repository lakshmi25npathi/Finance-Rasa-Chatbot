# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Corporate Card
#**************************************************************************************************************
# Card Application

class ActionCardApplication(Action):

    def name(self):
        return "action_card_application"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card application has been recieved")

        return []

# Card limit

## Available Credit limit

class ActionCardLimit(Action):

    def name(self):
        return "action_CardLimit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card limit is $50000")

        return []

## Credit card limit increase 

class ActionRiseCardLimit(Action):

    def name(self):
        return "action_RiseCardLimit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card limit has been raised by $10000")

        return []

# Registration/Activation/PIN

## Card Registration

class ActionCardRegister(Action):

    def name(self):
        return "action_CardRegister"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Please enter your name and empolyee ID")
        
        return []

## Card Activation

class ActionCardActivation(Action):

    def name(self):
        return "action_CardActivation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Please enter your name and empolyee ID")
        
        return []

## Reset PIN

class ActionResetPIN(Action):

    def name(self):
        return "action_ResetPIN"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your PIN has been changed")

        return []

# Lost / Fraudulent card 

## Lost/Stolen card

class ActionLostCard(Action):

    def name(self):
        return "action_LostCard"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="To deactivate stolen card, please enter your card number")

        return []

## Fraudulent charges

class ActionFraudCharges(Action):

    def name(self):
        return "action_FraudCharges"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Please enter your credit card number")
        
        return []

# Other

## Personal Card Payment/Personal Usage

class ActionCardPayment(Action):

    def name(self):
        return "action_CardPayment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="How much you want make a personal payment")

        return []

## Card Statement/Usage history

class ActionCardHistory(Action):

    def name(self):
        return "action_CardHistory"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card history has been sent to your email")

        return []

## Card Replacement

class ActionCardRenewal(Action):

    def name(self):
        return "action_CardRenewal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card has been replaced with card number xxxxx")

        return []

## Card billing address update

class ActionCardBillingAddress(Action):

    def name(self):
        return "action_CardBillingAddress"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card billing address has been updated")

        return []

## Card Management Policy

class ActionCardPolicy(Action):

    def name(self):
        return "action_CardPolicy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card policy has been sent to your email")

        return []
