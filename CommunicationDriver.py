print("Loading the Natural Language processor...")
from NLUModule import NLUAnalyser

print("Loading communication software...")
from ASRModule import ASRModuleV1
import OutputModule
from difflib import SequenceMatcher

# Load the ASR module
speech_recogniser = ASRModuleV1

# Load the NlU module
language_analyser = NLUAnalyser


# the main driver class - continously listens for commands
def main():
    # Initiate the output module
    output = OutputModule

    # Start the ASR module
    print("Starting the speech recognition system")
    listen()

    # Continuous listening loop
    # Listen for input from microphone
    # If value is found send to proccessing method


def listen():
    while (True):
        value = speech_recogniser.listen()
        if value != "Null":
            process(value)


def test():
    found_value = speech_recogniser.analyseFile(test_file)
    similarity = str(SequenceMatcher(None, actual_data, found_value).ratio())
    print(similarity)
    process(found_value)


def process(text):
    # print("Proccessing input..." + text)

    # pre process before sendning to be analysed
    # Send to NLU for processing
    model_output = language_analyser.analyse(text)

    print("Intention found: ")
    print(model_output["intent"]["name"])

    print("Instruction set generated: ")
    model_out_copy = model_output.copy()

    print(OutputModule.process(model_out_copy))
    OutputModule.verbally_respond(model_output)
    instruction_set = OutputModule.process(model_output)
    # Send to Output


main()
