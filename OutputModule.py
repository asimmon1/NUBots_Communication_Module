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


    multiIntentTest = {'text': 'go to the kitchen get me a beer from the shelf and give it to me',
                        'intent': {'id': 5030101474768177391,
                                   'name': 'go_to_place+take_object_from_the_placement+deliver_it_to_me',
                                   'confidence': 0.6125522255897522}, 'entities': [
            {'entity': '"place"', 'start': 10, 'end': 17, 'confidence_entity': 0.9834251999855042, 'value': 'kitchen',
             'extractor': 'DIETClassifier'},
            {'entity': '"object"', 'start': 27, 'end': 31, 'confidence_entity': 0.9995878338813782, 'value': 'beer',
             'extractor': 'DIETClassifier'},
            {'entity': '"place"', 'start': 41, 'end': 46, 'confidence_entity': 0.9282556176185608, 'value': 'shelf',
             'extractor': 'DIETClassifier'}],
                        'intent_ranking': [{'id': 5030101474768177391,
                                            'name': 'go_to_place+take_object_from_the_placement+deliver_it_to_me',
                                            'confidence': 0.6125522255897522},
                                           {'id': -4828206238987585652,
                                            'name': 'take_object_from_the_placement+deliver_it_to_me+answer_question',
                                            'confidence': 0.36412540078163147},
                                           {'id': -2557781306983401135,
                                            'name': 'go_to_place+take_the_object+deliver_it_to_me',
                                            'confidence': 0.01651490479707718},
                                           {'id': 7162758957566710485, 'name': 'find_object_in_room+deliver_it_to_me',
                                            'confidence': 0.0033488734625279903},
                                           {'id': 5851309784761359836,
                                            'name': 'take_object_from_the_placement+deliver_it_to_me',
                                            'confidence': 0.0029760627076029778},
                                           {'id': 7545006386555068802,
                                            'name': 'take_object_from_the_placement+go_to_place+deliver_to_name',
                                            'confidence': 0.0002346885303268209},
                                           {'id': 6031051345724166511, 'name': 'deliver_it_to_me',
                                            'confidence': 0.00020100524125155061},
                                           {'id': -488819467365087494, 'name': 'guide_them_to_the_room',
                                            'confidence': 4.294080281397328e-05},
                                           {'id': -2663835504377684674, 'name': 'find_them_in_place+guide_them_to_the_room',
                                            'confidence': 2.778235057121492e-06},
                                           {'id': 2385680674734148750, 'name': 'follow_them',
                                            'confidence': 1.174748717858165e-06}]}
    # print(format_Instructions(intention_list["take_object_from_the_placement"]["Instruction_set"], testEntities2))
    # print(fruits_list["Intention_name"]["Instruction_set"])
    # x = 0
    # for instruction in fruits_list["Intention_name2"]["Instruction_set"]:
    #     print(str(x)+": "+instruction)
    #     x+=1

    print(process(multiIntentTest))


# Processes the NLU module output
def process(model_output):
    # Extract intention from instruction set
    intention = model_output["intent"]["name"]
    intentions = intention.split("+")
    entities = model_output["entities"]
    instruction_list = []

    for intent in intentions:

        #get the expected entities
        entities_string = intention_list[intent]["Expected_Entities"]
        expected_entities = format_entity_list(entities_string)
        #match to next availble
        matched_entities = []
        if len(entities) >0 :
            for entity in expected_entities:
                if entity == entities[0]["entity"].strip("\""):
                    matched_entities.append(entities[0])
                    entities.remove(entities[0])

        #trim entity list=

        instruction_set = format_Instructions(intention_list[intent]["Instruction_set"], matched_entities)
        instruction_list += instruction_set
    return instruction_list




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


def format_entity_list(string):
    list = string.split(" -")
    for i in range(len(list)):
        list[i] = list[i].strip("-")
        list[i] = list[i].strip("[")
        list[i] = list[i].strip("]")
    return list


# finds index of a character in string
def find_idx(str, ch):
    yield [i for i, c in enumerate(str) if c == ch]
tester()