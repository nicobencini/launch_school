import json
import random

PATH = "/home/nicbencini/launch_school/python_helper/python_helper_db.json"

def helper_reader(keyword):
    with open(PATH, 'r') as f:
        info_dictionary = json.load(f)

    try:
        description = info_dictionary[keyword]
    except:
        description = f"==> '{keyword}' not found!!"

    return (description)

def helper_search(keyword):
    with open(PATH, 'r') as f:
        info_dictionary = json.load(f)

    keys = info_dictionary.keys()
    
    count = 0

    for key in keys:
        if keyword in key:
            print(f'\n{key}:\n' + '-'*20)
            print(info_dictionary[key])
            print('-'*20 + '\n')
            count += 1
    
    if count == 0:
        print ('==> No iformation found')

def helper_writer(keyword, description):
    
    data_entry = {keyword : description}
    with open(PATH, 'r') as f:
        info_dictionary = json.load(f)

    if keyword not in info_dictionary.keys():
        info_dictionary.update(data_entry)   
    
        with open(PATH, 'w') as f:
            json.dump(info_dictionary, f)


def print_keywords():
    with open(PATH, 'r') as f:
        info_dictionary = json.load(f)
    
    sorted_key_list = sorted(info_dictionary.keys())

    print('-'*20)
    for key in sorted_key_list:
        print('==> ' + key)
    print('-'*20)

print('*' *100 )
print('*' *100 )
print('Welcome to Python Helper!\n')
print("Input 'r- + keyword' to retrieve the informaiton on that keyword.")
print("Input 's- + keyword' to search the database for all entries containing the keyword and print results.")
print("Input 'keys' to get a list of the current keywords.")
print("Input 'study' to go into study mode.")
print("Input 'q' to exit.")
print('*' *100 + '\n')

while True:
    user_input = input('==> What can I help you with?')

    if (user_input == 'keys'):
        print_keywords()
    elif(user_input[0:2] == 'r-'):
        keyword = user_input[2::]
        print(f'\n{keyword}:\n' + '-'*20)
        print(helper_reader(keyword))
        print('-'*20 + '\n')
    elif(user_input[0:2] == 's-'):
        keyword = user_input[2::]
        helper_search(keyword)
    elif(user_input == 'q'):
        print('==> Goodbye!')
        break
    elif(user_input == 'study'):
        with open(PATH, 'r') as f:
            info_dictionary = json.load(f)

        keys = list(info_dictionary.keys())

        while True:
            key = random.choice(keys)
            print('-'*20)
            print(key)
            user_input = input("==>Press enter for answer or 'q' to quit.\n\n")
            if user_input == 'q':
                break
            print (info_dictionary[key])
            print('-'*20)

    else:
        print('==> Invalid input. Please re-entre.')


