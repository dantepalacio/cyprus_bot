from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSetTypeCompany(Action):
    def name(self) -> Text:
        return "action_companies_type_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("result", "Main types of companies")]

class ActionRegisterCompany(Action):
    def name(self) -> Text:
        return "action_register_company_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("result", "How to register a company in Cyprus")]

class ActionObligations(Action):
    def name(self) -> Text:
        return "action_obligations_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("result", "Obligations and payments(Fees)")]

class ActionBecomeResident(Action):
    def name(self) -> Text:
        return "action_become_resident_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("result", "How to become a tax resident in Cyprus")]


class ActionTaxCalculator(Action):
    def name(self) -> Text:
        return "action_tax_calculator_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("result", "Tax Calculator")]


class ActionIndividualTaxation(Action):
    def name(self) -> Text:
        return "action_individual_taxation_set_slot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        return [SlotSet("result", "Individual taxation")]






