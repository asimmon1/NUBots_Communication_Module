import pandas as pd

from os import path
from pydub import AudioSegment
from difflib import SequenceMatcher
import string
import os
import datetime

from ASRModule.ASRModuleV1 import analyseFile

# Testing parameters
result_path = 'D:/ASRVoiceData/Results'
testing_number = 500
result_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'_'+str(testing_number)+'_Model1.txt'


# Formatting Method - From mp3 to wav file at 16000
def format_to_wav(row):
    # Current Path is D:/ASRVoiceData/clips/
    clip_folder = path + 'clips/'
    clip_name = row.path

    # Pathing for files
    mp3_path = clip_name + '.mp3'
    os.chdir(clip_folder)
    target = path + clip_name+'.wav'

    # Exporting to wav
    sound = AudioSegment.from_mp3(mp3_path).export(target, format="wav")
    return target


# Tests a given row of the data frame
def test(row):
    # test the row with the ASR module and returns true or false
    print('Testing row: ')
    print(row)
    # Useful
    row_id = row.client_id
    target = format_to_wav(row)

    # Analyse file calls the speech recognition model
    print(target)
    print("analysed and found: " + analyseFile(target))
    write_results(row, analyseFile(target))
    os.remove(target)

# writes the results of the testing to the report file
def write_results(row, found_sentence):
    print("Storing....")
    os.chdir(result_path)
    f = open(result_name, "a")
    f.write('\n'+str(row))

    actual_data = row.sentence.lower()
    actual_data = actual_data[:-1]
    actual_data = actual_data.translate(str.maketrans('', '', string.punctuation))

    f.write('\nActual(converted): '+actual_data)
    f.write('\nFound: ' + found_sentence)
    result = ""
    if actual_data == found_sentence:
        result = 'CORRECT'
    else:
        result= 'FALSE'
    f.write('\n'+result)
    similarity = str(SequenceMatcher(None,  actual_data, found_sentence).ratio())
    f.write('\nSimilarity: '+str(SequenceMatcher(None,  actual_data, found_sentence).ratio())+'\n')
    benchmark_data.append([(str(row)),(result), (similarity)])
    f.close()

def get_clip(clip_path):
    # gets the clip from a given path

    print('getting clip form: ' + path)


# Conversion tool - Used for permanent batch conversions
def convert_to_wav(data_frame):

    #  for loop going through df converting all to wav files
    # Make sure to include percentages
    os.chdir('D:/ASRVoiceData/')


    for index, row in data_frame.iterrows():

        if index%10==0:
            print("Percentage: "+str(index/data_frame.size*100))

        clip_name = row.path
        mp3_path = 'clips/'+clip_name + '.mp3'
        target = 'Converted/'+clip_name + '.wav'
        sound = AudioSegment.from_mp3(mp3_path).export(target, format="wav")

    print("Finished")


# Extracting data frame
path = 'D:/ASRVoiceData/'

print(path + 'validated')
workbook = pd.read_table(path + 'validated.tsv')
workbook.head()
print(workbook['accent'])

AusDF = workbook[workbook['accent'] == 'australia']
AusDF.head()
print(AusDF)

# conversion_df = AusDF[1000:1100]
# convert_to_wav(conversion_df)

# Actual testing loop and logic
os.chdir(result_path)
benchmark_data = []
f = open(result_name, "a")
f.write('Batch '+str(datetime.datetime.now())+': \n')
f.close()


# for full loop use len(AusDF)
for i in range(testing_number):
    print('Testing: '+str(i) +' of ' + str(testing_number))
    test(AusDF.iloc[i])

correct = 0
similarity = 0.0
for i in range(len(benchmark_data)):

    if benchmark_data[i][1] == "CORRECT":
        correct+=1

    similarity+= float(benchmark_data[i][2])

    print(benchmark_data[i][1])
    print(benchmark_data[i][2])

similarity = similarity/len(benchmark_data)

f = open(result_name, "a")
f.write('\n\n '+str(correct)+' attempts were correct out of '+ str(len(benchmark_data)))
percentage_correct = (correct/len(benchmark_data))*100
f.write('\n\n Percentage Correct: '+ str(percentage_correct))
f.write('\n Average Similarity: '+str(similarity))
f.close()
print("Finished.")


