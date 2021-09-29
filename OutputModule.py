import yaml
import pyttsx3

with open('Intention_Instructions.yml') as file:
    intention_list = yaml.load(file, Loader=yaml.FullLoader)


# Just for testing purposes
def tester():
    # verbally_respond(intention_list, "find_name_in_place")

    testEntities = [
        {'entity': '"name"', 'start': 5, 'end': 10, 'confidence_entity': 0.8220005035400391, 'value': 'Julia',
         'extractor': 'DIETClassifier'},
        {'entity': '"place"', 'start': 18, 'end': 23, 'confidence_entity': 0.8015493750572205, 'value': 'bench',
         'extractor': 'DIETClassifier'}]

    testEntities2 = [
        {'entity': '"object"', 'start': 8, 'end': 12, 'confidence_entity': 0.9999829530715942, 'value': 'beer',
         'extractor': 'DIETClassifier'},
        {'entity': '"room"', 'start': 22, 'end': 28, 'confidence_entity': 0.8432316184043884, 'value': 'office',
         'extractor': 'DIETClassifier'}]
    print(format_Instructions(intention_list["take_object_from_the_placement"]["Instruction_set"], testEntities2))
    # print(fruits_list["Intention_name"]["Instruction_set"])
    # x = 0
    # for instruction in fruits_list["Intention_name2"]["Instruction_set"]:
    #     print(str(x)+": "+instruction)
    #     x+=1


# Processes the NLU module output
def process(model_output):
    # Extract intention from instruction set

    intent = model_output["intent"]["name"]
    instruction_set = format_Instructions(intention_list[intent]["Instruction_set"], model_output["entities"])

    return instruction_set


# Loads the verbal response for an intention
def verbally_respond(model_output):
    # if + is found recursivly call for the split string

    engine = pyttsx3.init()
    intent = model_output["intent"]["name"]
    engine.say(str(intention_list[intent]["verbal_response"]))
    engine.runAndWait()


# Formats the instructions by filling in the entities and ordering
def format_Instructions(intructions_set, entities):
    single_instructions = intructions_set.split(" -")
    single_instructions[0] = single_instructions[0].replace("-", "")
    new_instruction_list = []
    for i in range(len(single_instructions)):
        single_instructions[i] = fill_entity(single_instructions[i], entities)
        formatted_instruction = str(i + 1) + ": "
        for string in single_instructions[i]:
            formatted_instruction += string + " "

        new_instruction_list += [formatted_instruction]

    return new_instruction_list


# Fills the entity in an instruction string
def fill_entity(string, entities):
    words = string.split(" ")
    for i in range(len(words)):
        if "[" in words[i]:
            words[i] = words[i].strip("[")
            words[i] = words[i].strip("]")
            for entity in entities:
                if entity["entity"].lower().strip("\"") == words[i]:
                    words[i] = entity["value"]

    return words


tester()
