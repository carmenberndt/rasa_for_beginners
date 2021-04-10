# https://rasa.com/docs/rasa/custom-actions
from typing import Text, Dict, List, Any, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

import requests
import json
import os


class ValidateHealthForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_health_form"

    async def validate_confirm_exercise(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value:
            return {"confirm_exercise": True}
        else:
            return {"confirm_exercise": False, "exercise": None}