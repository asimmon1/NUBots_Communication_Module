from NLUModule import NLUAnalyser
from ASRModule import ASRModuleV1
import OutputModule

# Load the ASR module
print("Loading communication software.")
speech_recogniser = ASRModuleV1

# Load the NlU module
print("Loading the Natural Language processor...")
language_analyser = NLUAnalyser


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


def process(text):
    print("Proccessing input..." + text)

    # pre process before sendning to be analysed
    # Send to NLU for processing
    model_output = language_analyser.analyse(text)

    print("Intention found: ")
    print(model_output["intent"]["name"])

    print("Instruction set generated: ")
    model_out_copy = model_output.copy()

    print(OutputModule.process(model_out_copy))
    OutputModule.verbally_respond(model_output)

    # Send to Output


main()
