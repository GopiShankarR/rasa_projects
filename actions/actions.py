# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher

# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []

# class ActionStoreName(Action):
#     def name(self) -> Text:
#         return "action_store_name"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract the name entity from the latest user message associated with the provide_name intent
#         name = next(tracker.get_latest_entity_values("name_field"), None)
        
#         print(tracker.latest_message)
#         # print("Name entity:", name)
#         # print("bleh", [SlotSet("name", name)])
        
#         # If name entity is found, store it in the name slot
#         if name:
#             return [SlotSet("name_field", name)]
#         else:
#             # If no name entity is found, return an empty list
#             return []