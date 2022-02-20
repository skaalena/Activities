# Activity 4- Python List
# Autumn Skaalen
# ISQA 3900 Web Application Developement
# February 20, 2022
# List duplicate remover

# activity 4a

def Remove(names):
    print("Initial List of Names\n ['mary','mary','bill','sam','maria','kahn','bill','barry','george','hank','belinda','maria','karthik']\n")

    print("List of unique names after running through the de-duplicator program")

    final_list = []
    for num in names:
        if num not in final_list:
            final_list.append(num)
            return final_list

            names = ['mary','mary','bill','sam','maria','kahn','bill','barry','george','hank','belinda','maria','karthik']

            print(Remove(names))
