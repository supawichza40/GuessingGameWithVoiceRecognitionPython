import speech_recognition as sr
import random as rd


print("This is a number guessing game!1-100, You have 10 lives, and you need to find out the number I am thinking of, if you guess correct, you can move to the next round.")
print("Generating a random number and that will be the number I am thinking of.")
answer = rd.randint(0,100)
lives = 5
user_input = 0

recogniser_inst = sr.Recognizer() # create a recogniser instance.

#List all the available speaker and microphone with index
for count,microphone in enumerate(sr.Microphone.list_microphone_names()):
    print(count,microphone)

while True:
    try:
        index = int(input("What is the microphone index from the list?"))
        microphone = sr.Microphone(device_index = index)
        while(lives>=0):
            try:
                with microphone as source:
                    print("Guess the number! Speak it out!")
                    audio_output = recogniser_inst.listen(source,phrase_time_limit = 3)
                    recogniser_inst.adjust_for_ambient_noise(source,duration=0.5)
                    user_input= int(recogniser_inst.recognize_google(audio_output))
                    print("You guess number {0}".format(user_input))
                    #Game logic for guessing
                    if user_input>=0 and user_input<=100:
                        if user_input == answer:
                            print("That is the correct answer! You have won with {0} lives left".format(lives))
                            break
                        elif(user_input<answer):
                            print("The answer is higher")
                            lives-=1

                        else:
                            print("The answer is lower")
                            lives-=1

                    else:
                        print("Invalid number input, please try again.")
            except :
                print("Invalid input or speech, please try again.")

        if lives<0:
            print("You are dead! GAME OVER !")
            break



    except :
        print("Invalid Index Please try again.")
