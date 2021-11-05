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
                                          {'id': -2663835504377684674,
                                           'name': 'find_them_in_place+guide_them_to_the_room',
                                           'confidence': 2.778235057121492e-06},
                                          {'id': 2385680674734148750, 'name': 'follow_them',
                                           'confidence': 1.174748717858165e-06}]}

    exitTest = {'text': 'go to the exit',
                'intent': {'id': -342517517105506541, 'name': 'go_to_place', 'confidence': 0.937962532043457},
                'entities': [{'entity': '"place"', 'start': 10, 'end': 14, 'confidence_entity': 0.9998570680618286,
                              'value': 'exit', 'extractor': 'DIETClassifier'}],
                'intent_ranking': [{'id': -342517517105506541, 'name': 'go_to_place', 'confidence': 0.937962532043457},
                                   {'id': 4441591611196869807, 'name': 'guide_them_to_the_place',
                                    'confidence': 0.028497472405433655}, {'id': 5810392035782171967,
                                                                          'name': 'find_gesture_person_in_room+guide_them_to_the_place',
                                                                          'confidence': 0.015368894673883915},
                                   {'id': 8444298590883430388, 'name': 'go_to_place+find_name_in_place+answer_question',
                                    'confidence': 0.012510501779615879},
                                   {'id': -1442478780025599394, 'name': 'find_them_in_place+guide_them_to_the_place',
                                    'confidence': 0.0029830976855009794},
                                   {'id': 1129510507926405128, 'name': 'go_to_place+take_the_object+place_on_placement',
                                    'confidence': 0.0013247570022940636}, {'id': 1568124161981792560,
                                                                           'name': 'take_object_from_the_placement+go_to_place+deliver_to_name',
                                                                           'confidence': 0.0012383329449221492},
                                   {'id': 7366034151374702332, 'name': 'go_to_place+take_the_object+deliver_it_to_me',
                                    'confidence': 6.378402758855373e-05}, {'id': 2636638795059586739,
                                                                           'name': 'go_to_place+take_object_from_the_placement+deliver_it_to_me',
                                                                           'confidence': 4.266676478437148e-05},
                                   {'id': 6592226560023567322, 'name': 'guide_name_from_place_to_place',
                                    'confidence': 7.989295227162074e-06}]}

    gesture_test = {'text': 'find the waving person in the office',
                    'intent': {'id': 5408910607561581179, 'name': 'find_gesture_person_in_room',
                               'confidence': 0.974810004234314}, 'entities': [
            {'entity': '"gesture"', 'start': 9, 'end': 15, 'confidence_entity': 0.9924208521842957, 'value': 'waving',
             'extractor': 'DIETClassifier'},
            {'entity': '"room"', 'start': 30, 'end': 36, 'confidence_entity': 0.9998169541358948, 'value': 'office',
             'extractor': 'DIETClassifier'}], 'intent_ranking': [
            {'id': 5408910607561581179, 'name': 'find_gesture_person_in_room', 'confidence': 0.974810004234314},
            {'id': -2242864693134451462, 'name': 'find_gesture_person_in_room+guide_them_to_the_room',
             'confidence': 0.015774453058838844},
            {'id': -3963107886035029103, 'name': 'find_gesture_person_in_room+follow_them',
             'confidence': 0.006587074603885412},
            {'id': 3032025282161081089, 'name': 'find_object_in_room+deliver_it_to_name_in_place',
             'confidence': 0.0014575000386685133},
            {'id': -8542670576459889394, 'name': 'place_object_in_placement+find_name_in_room+answer_question',
             'confidence': 0.0008161742007359862},
            {'id': 7329906019618066440, 'name': 'follow_name_who_is_at_place', 'confidence': 0.0003407879266887903},
            {'id': 5277198158193671727, 'name': 'find_name_in_room+answer_question',
             'confidence': 0.00013386608043219894},
            {'id': -8531829408034531145, 'name': 'find_name_in_room', 'confidence': 6.0526283050421625e-05},
            {'id': 990665670384614109, 'name': 'deliver_it_to_name_in_place', 'confidence': 9.912355380947702e-06},
            {'id': 3235750508281550860, 'name': 'find_gesture_person_in_room+guide_them_to_the_place',
             'confidence': 9.628389307181351e-06}]}

    largeTest = {'text': 'take the beer from the shelf deliver it to Anna in the bed guide them to the kitchen',
                 'intent': {'id': 5726968576518644682,
                            'name': 'take_object_from_the_placement+deliver_it_to_name_in_place+guide_them_to_the_room',
                            'confidence': 0.9988498091697693}, 'entities': [
            {'entity': '"object"', 'start': 9, 'end': 13, 'confidence_entity': 0.999957799911499, 'value': 'beer',
             'extractor': 'DIETClassifier'},
            {'entity': '"place"', 'start': 23, 'end': 28, 'confidence_entity': 0.9156861305236816, 'value': 'shelf',
             'extractor': 'DIETClassifier'},
            {'entity': '"name"', 'start': 43, 'end': 47, 'confidence_entity': 0.9995750784873962, 'value': 'Anna',
             'extractor': 'DIETClassifier'},
            {'entity': '"place"', 'start': 55, 'end': 58, 'confidence_entity': 0.9997746348381042, 'value': 'bed',
             'extractor': 'DIETClassifier'},
            {'entity': '"room"', 'start': 77, 'end': 84, 'confidence_entity': 0.9995773434638977, 'value': 'kitchen',
             'extractor': 'DIETClassifier'}], 'intent_ranking': [{'id': 5726968576518644682,
                                                                  'name': 'take_object_from_the_placement+deliver_it_to_name_in_place+guide_them_to_the_room',
                                                                  'confidence': 0.9988498091697693},
                                                                 {'id': -4831856364644485819,
                                                                  'name': 'guide_them_to_the_room',
                                                                  'confidence': 0.0007421826012432575},
                                                                 {'id': 8434024480973770168,
                                                                  'name': 'find_them_in_place+guide_them_to_the_room',
                                                                  'confidence': 0.00012973313278052956},
                                                                 {'id': -5539228037583004059,
                                                                  'name': 'take_object_from_the_placement+deliver_it_to_name_in_place+follow_them',
                                                                  'confidence': 0.00010855415894184262},
                                                                 {'id': 5381658183275763630,
                                                                  'name': 'take_object_from_the_placement+deliver_it_to_name_in_place+guide_them_to_the_place',
                                                                  'confidence': 9.960833267541602e-05},
                                                                 {'id': 5645945950853826864,
                                                                  'name': 'go_to_place+take_object_from_the_placement+deliver_it_to_me',
                                                                  'confidence': 3.388205004739575e-05},
                                                                 {'id': 5377396954018051025,
                                                                  'name': 'take_object_from_the_placement+deliver_it_to_me',
                                                                  'confidence': 1.122498815675499e-05},
                                                                 {'id': 8224003839746441706,
                                                                  'name': 'take_object_from_the_placement+deliver_it_to_me+answer_question',
                                                                  'confidence': 1.0831852705450729e-05},
                                                                 {'id': 5195620129910661595,
                                                                  'name': 'take_object_from_the_placement+go_to_place+deliver_to_name',
                                                                  'confidence': 9.211839824274648e-06},
                                                                 {'id': 6875940516572779771,
                                                                  'name': 'find_gesture_person_in_room+guide_them_to_the_room',
                                                                  'confidence': 4.936021014145808e-06}]}

    triple_intenttest = {'text': 'go to the desk get the pen and give it to me',
                         'intent': {'id': 1247555141514203622, 'name': 'go_to_place+take_the_object+deliver_it_to_me',
                                    'confidence': 0.9974803328514099}, 'entities': [
            {'entity': '"place"', 'start': 10, 'end': 14, 'confidence_entity': 0.9995324611663818, 'value': 'desk',
             'extractor': 'DIETClassifier'},
            {'entity': '"object"', 'start': 23, 'end': 26, 'confidence_entity': 0.9996356964111328, 'value': 'pen',
             'extractor': 'DIETClassifier'}], 'intent_ranking': [
            {'id': 1247555141514203622, 'name': 'go_to_place+take_the_object+deliver_it_to_me',
             'confidence': 0.9974803328514099},
            {'id': -131025305581450117, 'name': 'go_to_place+take_object_from_the_placement+deliver_it_to_me',
             'confidence': 0.002053638454526663},
            {'id': 7983402689062998467, 'name': 'deliver_it_to_me', 'confidence': 0.000395552342524752},
            {'id': -951149383615934795, 'name': 'take_object_from_the_placement+deliver_it_to_me',
             'confidence': 2.497189234418329e-05},
            {'id': -3241437192423548967, 'name': 'go_to_place+take_the_object+deliver_it_to_name_in_place',
             'confidence': 1.507909928477602e-05},
            {'id': 3980589582878353777, 'name': 'go_to_place+take_the_object+place_on_placement',
             'confidence': 1.391457499266835e-05},
            {'id': 7299257785345437299, 'name': 'take_object_from_the_placement+deliver_it_to_me+answer_question',
             'confidence': 7.488382379960967e-06},
            {'id': -5450126815976994537, 'name': 'take_object_from_the_placement+go_to_place+deliver_to_name',
             'confidence': 7.261554401338799e-06},
            {'id': -448273666104916340, 'name': 'deliver_to_name', 'confidence': 1.3986557405587519e-06},
            {'id': 2459133192810904900, 'name': 'guide_them_to_the_room', 'confidence': 3.540594093465188e-07}]}
    # print(format_Instructions(intention_list["take_object_from_the_placement"]["Instruction_set"], testEntities2))
    # print(fruits_list["Intention_name"]["Instruction_set"])
    # x = 0
    # for instruction in fruits_list["Intention_name2"]["Instruction_set"]:
    #     print(str(x)+": "+instruction)
    #     x+=1

    print(process(triple_intenttest))
    verbally_respond(triple_intenttest)


# Processes the NLU module output
def process(model_output):
    # Extract intention from instruction set
    intention = model_output["intent"]["name"]
    intentions = intention.split("+")
    entities = model_output["entities"]
    instruction_list = []
    current_entity = 0
    for intent in intentions:

        # get the expected entities
        entities_string = intention_list[intent]["Expected_Entities"]
        matched_entities = []
        if "null" not in entities_string:
            expected_entities = format_entity_list(entities_string)
            # match to next availble

            if len(entities) > 0:
                for entity in expected_entities:
                    if current_entity < len(entities):
                        if entity == entities[current_entity]["entity"].strip("\""):
                            matched_entities.append(entities[current_entity])
                            current_entity += 1

        # trim entity list=

        instruction_set = format_Instructions(intention_list[intent]["Instruction_set"], matched_entities)
        instruction_list += instruction_set
    return instruction_list


# Loads the verbal response for an intention
def verbally_respond(model_output):
    intention = model_output["intent"]["name"]
    intentions = intention.split("+")
    entities = model_output["entities"]
    current_entity = 0
    for intent in intentions:

        response = intention_list[intent]["verbal_response"]

        # get the expected entities
        entities_string = intention_list[intent]["Expected_Entities"]
        expected_entities = format_entity_list(entities_string)
        # match to next available
        matched_entities = []

        if len(entities) >0:
            for entity in expected_entities:
                if current_entity < len(entities):
                    if entity == entities[current_entity]["entity"].strip("\""):
                        matched_entities.append(entities[current_entity])
                        current_entity += 1

        response = ' '.join(fill_entity(response, matched_entities))

        print("Verbal response: " + response)
        engine = pyttsx3.init()
        engine.say(str(response))
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

