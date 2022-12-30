import time
import emoji
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
if int(time.strftime('%H')) < 12:
    print("Good Morning",emoji.emojize(":sun:"))   
elif int(time.strftime('%H')) < 16:
    print("Good Afternoon",emoji.emojize(":grinning_face:"))
elif int(time.strftime('%H')) <= 18:
    print("Good Evening",emoji.emojize(":sunset:"))
    
else:
    print("Good Night",emoji.emojize(":sleeping_face:"))

#code to print minutes and seconds
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
