from spy_detail import spy_name,spy_age,spy_rating,spy_salutation
from spy import

def start_chat(spy_name , spy_age , spy_rating):
    print spy_name
    print spy_age
    print spy_rating
    return "the chat has started for"

spy_name = "najma"
spy_age = 19
spy_rating =5.0
spy_status = None
STATUS_MESSAGE =  ["What's up doc? ",  "Busy", "Available"]
#we create add status function due to this function we add new status
def add_status(current_status_message):
    if current_status_message != None:
        print "your current status message is" + current_status_message
    else:
        print "you dont have any status message from before"
    default = raw_input("Do you want to select from the older status (y/n)?")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGE.append(updated_status_message)
            print STATUS_MESSAGE
    if default.upper() =="Y":
        print  "What status do you want to choose?"
        item_position = 1
        for e in STATUS_MESSAGE :
            print str(item_position) +"." + e
            item_position = item_position + 1

        status_choice = raw_input("what status do you want to set")

        if int(status_choice) > len(STATUS_MESSAGE):
            print "BUZZZZZZZZZ"
        if len(STATUS_MESSAGE) >=int(status_choice):
            updated_status_message = STATUS_MESSAGE[ int (status_choice)- 1 ]
            print  "your status message is : %s" %(updated_status_message)

        return updated_status_message



b = add_status(spy_status)
print b

friend_names = []
friend_ages = []
friends_rating = []
friend_is_online = []

def add_friend():
    new_name = raw_input("Please add your friends's name:")
    new_salutation = raw_input("Are they Mr or Ms ?:")
    new_name = new_salutation + " " + new_name
    new_age = raw_input("age")
    new_rating = raw_input("Spy rating?")

    if len(new_name) > 0 and new_age > 20 and new_rating >= spy_rating:

        friend_names.append(new_name)
        friend_ages.append(new_age)
        friends_rating.append(new_rating)
        friend_is_online.append(True)


    else:
        print "Sorry we cant add you"

add_friend()

print friend_names
print friend_ages
print friends_rating





question = "continuous as %s %s(Y/N)" %(spy_salutation ,spy_name)
existing = raw_input(question)



if (existing == "Y"):
  #Continue with the default user/details imported from the helper file.
    print "continuous as usual"

else:
  spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
  if len(spy_name) > 0:
    spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")

    spy_age = raw_input("What is your age?")
    spy_age = int(spy_age)

    spy_rating = raw_input("What is your spy rating?")
    spy_rating = float(spy_rating)

    spy_is_online = True
