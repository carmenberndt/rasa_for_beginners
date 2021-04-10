# https://rasa.com/docs/rasa/custom-actions
from typing import Text, Dict, List, Any, Union

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class HealthForm(FormAction):
    def name(self) -> Text:
        return "health_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        if tracker.get_slot("confirm_exercise"):
            return ["confirm_exercise", "exercise", "sleep", "stress", "goal"]
        else:
            return ["confirm_exercise", "sleep", "stress", "goal"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None"),
            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),
            ],
            "goal": [
                self.from_text(intent="inform"),
            ]
        }




