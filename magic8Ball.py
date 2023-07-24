#Magic8Ball program

import random

#write answers
ans1="Go for it!"
ans2="No way, Jose!"
ans3="I'm not sure. Ask me again."
ans4="Fear of unknown is what imprisons us."
ans5="It'd be madness to do that!"
ans6="Only you can save mankind!"
ans7="Makes no difference to me, do or don't - whatever."
ans8="Yes, I think on balance that is the right choice."

print("welcome to magic8Ball")

# get the user question
question = input ("Ask me for advice then press ENTER to shake me.\n")
print ("shaking ...\n" *4)

# use the randint() function to select the correct answer
choice=random.randint(1,8)
if choice == 1:
    answer=ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer= ans5
elif choice == 6:
    answer= ans6
elif choice == 7:
    answer= ans7
else:
    answer = ans8
#print the answer to the screen
print (answer)
input ("\n\nPress the RETUN key to finish!")
