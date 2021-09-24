import yaml

def test():
    with open('Intention_Instructions.yml') as file:
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)

        print(fruits_list["Intention_name"]["Instruction_set"])
        x = 0
        for instruction in fruits_list["Intention_name2"]["Instruction_set"]:
            print(str(x)+": "+instruction)
            x+=1


test()