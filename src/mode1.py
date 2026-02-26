import random
colours = ["red", "blue", "green", "yellow", "orange", "purple"]

def generate_code():
    code = []
    for i in range(4):
        code.append(random.choice(colours))
    return code

# create a function to check if the user input is any one of the random coulours in  the list code
def check_input(user_input, code):
    if user_input in code:
        return True
    else:
        return False
    
# create a function to check if the user input is in the correct position in the list code
def check_position(user_input, code):
    if user_input in code:
        index = code.index(user_input)
        if index == 0:
            return "red"
        elif index == 1:
            return "blue"
        elif index == 2:
            return "green"
        elif index == 3:
            return "yellow"
    else:
        return False
        
