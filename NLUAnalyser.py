from rasa.nlu.model import Interpreter
import json
import pyttsx3
rasa_model_path = "models/Cat_1_2_trainedmodel/nlu"

interpreter = Interpreter.load(rasa_model_path)



def rasa_output(text):
    print(text)
    message = str(text).strip()
    #print("message: " + str(text) + " stripped: " + message)
    result = interpreter.parse(message)


    return result


def manual_input_loop():
    user_input = input(">>")
    while not (user_input.lower() in ("q") ):
        model_output = rasa_output(user_input)
        print(model_output)
        print("====================================================\n")
        respond(model_output)
        user_input = input(">>")

def analyse(text):

    model_output = rasa_output(text)
    return model_output


def respond(model_output):
    engine = pyttsx3.init()



    intent = model_output["intent"]["name"]
    intent = intent.replace("_", " ", len(intent))
    intent = intent.replace("+", " ", len(intent))
    entities = "";
    print(model_output["entities"])
    for i in model_output["entities"]:
        entities += " Found entity " +i["entity"] +" which is "+i["value"]

    print(intent+entities)

    engine.say("Initiating sequence" + intent+entities)
    engine.runAndWait()


manual_input_loop()