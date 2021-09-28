import yaml
import pyttsx3


def tester():
    with open('Intention_Instructions.yml') as file:
        intention_list = yaml.load(file, Loader=yaml.FullLoader)
        # verbally_respond(intention_list, "find_name_in_place")

        testEntities =[{'entity': '"name"', 'start': 5, 'end': 10, 'confidence_entity': 0.8220005035400391, 'value': 'Julia', 'extractor': 'DIETClassifier'}, {'entity': '"place"', 'start': 18, 'end': 23, 'confidence_entity': 0.8015493750572205, 'value': 'bench', 'extractor': 'DIETClassifier'}]
        print(format_Instructions(intention_list["find_name_in_place"]["Instruction_set"], testEntities))
        # print(fruits_list["Intention_name"]["Instruction_set"])
        # x = 0
        # for instruction in fruits_list["Intention_name2"]["Instruction_set"]:
        #     print(str(x)+": "+instruction)
        #     x+=1



def verbally_respond(list, intention):
    #if + is found recursivly call for the split string

    engine = pyttsx3.init()

    engine.say(str(list[intention]["verbal_response"]))
    engine.runAndWait()

def format_Instructions(intructions_set, entities):

    single_instructions = intructions_set.split(" -")
    single_instructions[0] = single_instructions[0].replace("-", "")
    new_instruction_list = []
    for i in range(len(single_instructions)):
        single_instructions[i] = fill_entity(single_instructions[i], entities)
        formatted_instruction = str(i+1)+": "
        for string in single_instructions[i]:
            formatted_instruction += string+" "

        new_instruction_list += [formatted_instruction]

    return new_instruction_list
def fill_entity(string, entities):

    words = string.split(" ")
    for i in range(len(words)):
        if "[" in words[i]:
            words[i] = words[i].strip("[")
            words[i] = words[i].strip("]")
            for entity in entities:
                if entity["entity"].lower().strip("\"") == words[i]:
                    words[i] = entity["value"]


    return(words)

def extract_instructions(heading):
    print("this will extract the instructions for the intention under the heading")

tester()