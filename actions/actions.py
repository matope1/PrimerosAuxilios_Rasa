from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from typing import Any, Text, Dict, List

from rag.rag_pipeline import ask_rag


class ActionRag(Action):

    def name(self) -> Text:
        return "action_rag"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        question = tracker.latest_message.get("text")
        intent = tracker.latest_message.get("intent", {}).get("name", "desconocido")
        confidence = tracker.latest_message.get("intent", {}).get("confidence", 0.0)

        print("\n--- NUEVA CONSULTA ---")
        print(f"Texto usuario: {question}")
        print(f"Intent detectado: {intent}")
        print(f"Confianza: {confidence:.4f}")

        answer = ask_rag(question)

        debug_msg = f"[Intent detectado: {intent}]"

        dispatcher.utter_message(text=f"{debug_msg}\n{answer}")

        return []