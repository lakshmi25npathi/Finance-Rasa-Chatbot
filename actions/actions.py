# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

# Corporate Card
#**************************************************************************************************************
# Card Application

class ActionCardApplication(Action):

    def name(self):
        return "action_card_application"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Your card application has been recieved. Do you need anything else? Please enter yes or no?")

        return []

# Card limit

## Available Credit limit

class ActionCardLimit(Action):

    def name(self):
        return "action_CardLimit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card limit is $50000. Do you need anything else? Please enter yes or no?")

        return [SlotSet('card_number',card_no)]

## Credit card limit increase 

class ActionRiseCardLimit(Action):

    def name(self):
        return "action_RiseCardLimit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card limit has been raised by $10000. Do you need anything else? Please enter yes or no?")

        return [SlotSet('card_number',card_no)]

# Registration/Activation/PIN

## Card Registration

class ActionCardRegister(Action):

    def name(self):
        return "action_CardRegister"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        dispatcher.utter_message(text="Your card has been registered. Do you need anything else? Please enter yes or no?")
        
        return []

## Card Activation

class ActionCardActivation(Action):

    def name(self):
        return "action_CardActivation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card has been activated. Do you need anything else? Please enter yes or no?")
        
        return [SlotSet('card_number',card_no)]

## Reset PIN

class ActionResetPIN(Action):

    def name(self):
        return "action_ResetPIN"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your PIN has been changed. Do you need anything else? Please enter yes or no?")

        return [SlotSet('card_number',card_no)]

# Lost / Fraudulent card 

## Lost/Stolen card

class ActionLostCard(Action):

    def name(self):
        return "action_LostCard"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card has been deactivated. Do you need anything else? Please enter yes or no")
        
        return [SlotSet('card_number',card_no)]

## Fraudulent charges

class ActionFraudCharges(Action):

    def name(self):
        return "action_FraudCharges"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="We have sent mail to you about fraud charges. Do you need anything else? Please enter yes or no.")
        
        return [SlotSet('card_number',card_no)]

# Other

## Personal Card Payment/Personal Usage

class ActionCardPayment(Action):

    def name(self):
        return "action_CardPayment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="We have done card payment for your personal usage. Do you need anything else?. Please enter yes or no")

        return [SlotSet('card_number',card_no)]

## Card Statement/Usage history

class ActionCardHistory(Action):

    def name(self):
        return "action_CardHistory"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card history has been sent to your email. Do you need anything else? Please enter yes or no")

        return [SlotSet('card_number',card_no)]

## Card Replacement

class ActionCardRenewal(Action):

    def name(self):
        return "action_CardRenewal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card has been replaced. Do you need anything else?. Please enter yes or no")

        return [SlotSet('card_number',card_no)]

## Card billing address update

class ActionCardBillingAddress(Action):

    def name(self):
        return "action_CardBillingAddress"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):
        
        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card billing address has been updated. Do you need anything else? Please enter yes or no")

        return [SlotSet('card_number',card_no)]

## Card Management Policy

class ActionCardPolicy(Action):

    def name(self):
        return "action_CardPolicy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]):

        card_no = tracker.get_slot('card_number')
        dispatcher.utter_message(text="Your card policy has been sent to your email. Do you need anything else? Please enter yes or no")

        return [SlotSet('card_number',card_no)]
