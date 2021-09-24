import yaml
import pyttsx3


def tester():
    with open('Intention_Instructions.yml') as file:
        intention_list = yaml.load(file, Loader=yaml.FullLoader)
        verbally_respond(intention_list, "find_name_in_place")
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

def fill_entity(string, entities):
    print("this is where the enittyts will be fille din with what was said")

def extract_instructions(heading):
    print("this will extract the instructions for the intention under the heading")

tester()