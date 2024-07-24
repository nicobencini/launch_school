import json

PATH = "/home/nicbencini/launch_school/python_helper/python_helper_db.json"

def helper_reader(keyword):
    with open(PATH, 'r') as f:
        info_dictionary = json.load(f)

    try:
        description = info_dictionary[keyword]
    except:
        description = f"==> '{keyword}' not found!!"

    return (description)

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
print("Input 'w- + keyword' to write a new entry.")
print("Input 'keys' to get a list of the current keywords.")
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
    elif(user_input[0:2] == 'w-'):
        print('==> Functionality removed. Edit JSON file directly.')
        #keyword = user_input[2::]
        #description = input('==> Please enter information to store:')
        #helper_writer(keyword, description)
        #print(f"==> '{keyword}' entry has now been stored.")

    elif(user_input == 'q'):
        print('==> Goodbye!')
        break
    else:
        print('==> Invalid input. Please re-entre.')


