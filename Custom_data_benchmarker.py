from ASRModuleV1 import analyseFile
from difflib import SequenceMatcher
import string
path = 'D:/self_testing_data/'

data = ["Robot please locate William in the living table",
        "Could you please locate paprika in the dining room",
        "Please guide Jacob from the TV stand to the corridor",
        "escort her to the dining table",
        "Could you look for Liam in the living table",
        "Grasp the tea from the drawer",
        "answer a question",
        "Grasp the beer from the sideshelf",
        "follow Angel who is at the sink",
        "Could you please look for Ethan in the dining room",
        "Pick up the soap from the cabinet",
        "Say the time",
        "Put soap on the sideshelf",
        "Could you please locate Daniel in the dining room",
        "bring it to Daniel in the tv stand",
        "Say something about yourself",
        "grasp the chips from the living shelf",
        "Navigate to the dining table",
        "Pick up the soap from the bar",
        "locate the pointing right person in the dining room",
        "look for beer in the kitchen",
        "Navigate to the drawer",
        "Find Daniel",
        "Take the soap from the cupboard",
        "follow Charlotte who is at the cabinet",
        "Could you find Emily in the Kitchen",
        "Robot please find Liam in the bedroom",
        "Locate Noah in the cabinet",
        "follow Emily who is at the sink",
        "Get the soap",
        ]

i = 0
correct =0
average_similarity =0.0
while (i < 30):
    found_sentence =analyseFile(path + str(i) + '.wav')
    print("analysed and found: " + str(i) + ": " + found_sentence)
    similarity = str(SequenceMatcher(None, data[i], found_sentence).ratio())
    average_similarity+= float(similarity)
    actual_data = found_sentence.lower()
    actual_data = actual_data.translate(str.maketrans('', '', string.punctuation))
    print("actual data=" + actual_data)
    print("similairty =" + similarity)
    if actual_data == found_sentence:
        correct +=1

    i += 1

average_similarity = average_similarity/30
print("Average similairty ="+  str(average_similarity))
print("correct"+str(correct))


