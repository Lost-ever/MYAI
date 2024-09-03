import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser as wb
import os , sys
import cv2
import random as r
import pickle as pk
import csv 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate' , 160)
random = r.Random()
random.seed(1)
quitlist = ["shut down" , "quit" , "quit program" , "shutdown program" , "shutdown" , "qutie" , "exit"]
message = {"hello":["hello sir" , "welcome sir" , "hy sir"] , 
           "hello jarvis":["hello sir" , "welcome sir" , "hy sir"] , 
           "hy":["hello sir" , "welcome sir" , "hy sir"] , 
           "hy jarvis":["hello sir" , "welcome sir" , "hy sir"] , 
           "hi jarvis":["hello sir" , "welcome sir" , "hy sir"] ,
           "hi":["hello sir" , "welcome sir" , "hy sir"]}
fileextansion = {"text":"txt","python":"py"}
path = os.getcwd()
def  speak(audio):
                engine.say(audio)
                engine.runAndWait()

def keyfind(command , message):
        for i in message:
                if i == command:
                        return r.Random.choice( random , message[i])

def check_word(wordlist , data):
        found = True
        data = str(data).rstrip("?")
        datalist = str(data).split()
        for i in datalist:
                if i in wordlist:
                        found = True
                        continue
                else:
                        found = False
                        break
        if found == True:
                return True
        else:
                return False
        
def jokes():
        file = open(f'{path}\\jokes.csv' , "r")
        randomcount = r.randint(1,38269)
        jokes = csv.reader(file)
        jokeslist = list(jokes) 
        joke = jokeslist[randomcount]   
        file.close()
        return joke[0] , joke[1]
                
def click_picture(open = True):
        if open == True:
            win = cv2.VideoCapture()
            while True:
                ret,img = win.read()
                if ret == True:
                        key = cv2.waitKey()
                        if key == 32:
                                cv2.imshow(win,img)
                                
def checkdata(question):
        file  = open(f"{path}\\QAp.csv" , "r")
        reader = list(csv.reader(file))
        file.close() 
        for data in reader:
                found = check_word(question , data[0].lower())
                if found == True:
                        return data[1]
        else:
                return "none"
                                                                             
def question_data(command):
        try:
            file1 = open(f"{path}\\question.txt" , "r")
            question_number = len(file1.readlines())
        except Exception:
                question_number = 1
        with open(f"{path}\\question.txt" , "a") as file:
                file.write(f"{question_number}.'{command}'\n")
        if question_number != 1:
                file1.close()
def take_command():
                r = sr.Recognizer()
                while True:
                    try:
                        with sr.Microphone() as source :
                                print("listening.....")
                                r.energy_threshold = 600
                                audio = r.listen(source , timeout=4)
                        try:
                            print("recognising.....")
                            query = r.recognize_google(audio , language="en-IN")
                            #query1 = r.recognize_bing(audio1 , language="en-IN")
                            #print(query1)
                            print(query)
                        except sr.RequestError:
                            speak("you want connect with network or check your network connectivity")
                            return "none"
                        except sr.UnknownValueError:
                            speak("i can't understand you command , please say again and correct")
                            return "none"
                    except sr.exceptions.WaitTimeoutError:
                        print("waittimeouterror")
                        continue
                    except OSError:
                            return "none"
                    except Exception as e:
                            retrun "none"
                    return query

def mainprogram():
    command = take_command()
    if command == "none":  
       command = input("give me command:")
    command = command.lower()
    if command != "none":
        if command == "open youtube":
            speak("opening youtube")
            open_youtube()

        elif "+" in command or "-" in command and  "*" in command or "/" in command and "equal" in command:
                for i in command.split():
                        pass
                
        elif command == "open google":
            speak("opening google")
            open_google()
        
        elif "say" in command and "jokes" in command or "tell" in command and "jokes" in command or "speak" in command and "jokes" in command:
                question , answer = jokes()
                print(question)
                speak(question)
                if input("Answer:"):
                        speak("give me answer")
                        print(answer)
                        speak(answer)

        elif "youtube" in command:
            web = command.split("in youtube")
            speak(f"opening {web} on youtube")
            string = ""
            web.pop()
            for i in web:
                if len(web) == 1:
                    string += i
                else:
                    if  web.index(i) != -1:
                        string += i + "+"
                    else:
                        string += i
            open_youtube(string)

        elif "google" in command:
            web = command.split(' in google')
            speak(f"opening {web} on google")
            string = ""
            web.pop()
            for i in web:
                if len(web) == 1:
                    string += i
                else:
                    if  web.index(i) != -1:
                        string += i + "+"
                    else:
                        string += i
            open_google(string)
        
        elif "file" in command and "make" in command:
                for i in fileextansion:
                        if i in command:
                                speak("give me a file name")
                                filename = input("give me a file name:")
                                speak(f"{filename} is making")
                                open(f"{path}\\{filename}.{fileextansion[i]}" , "+a")
                                break
                else:
                    speak("i can't make this file")
                
        elif command in message:
                message1 = keyfind(command , message)
                speak(message1)

        elif command in quitlist:
            speak("thank you for using me , Good bye sir")
            sys.exit()
        
        elif "computer" in command and "shutdown" in command:
                speak("i am going to shutdown your pc , do you agree")
                #agree = take_command().lower()
                agree = input("yes/no:").lower()
                if agree == "yes":
                    os.system("shutdown -p")

        else:
            command = command.rstrip("?")
            command1 = command.split()
            answer = str(checkdata(command1))
            if answer != "none":
                    print(answer)
                    speak(answer)
            else:
                speak("i have not information about that")
                question_data(command)

def wishme():
                hr = datetime.datetime.now().hour
                if hr>=4 and hr<12 :
                                speak("Good Morning sir")
                elif hr>=12 and hr<16:
                                speak("Good Afternoon sir")
                elif hr>=16 and hr<19:
                                speak("Good Evening sir")
                elif hr>=19 and hr<4:
                                speak("Good Night sir")
                speak("how may i help you")
                
def open_youtube(web = "none"):
                if web == "none":
                                wb.open("https://www.youtube.com/")
                else:
                                wb.open(f"https://www.youtube.com/results?search_query={web}")

def open_google(web = "none"):
                if web == "none":
                                wb.open("https://www.google.com/")
                else:
                                wb.open(f"https://www.google.com/search?q={web}&oq={web}&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQLhiABDIJCAIQABhDGIoFMg8IAxAuGAoYxwEY0QMYgAQyDQgEEC4YrwEYxwEYgAQyBwgFEAAYgAQyBwgGEC4YgAQyBwgHEAAYgAQyDQgIEC4YrwEYxwEYgAQyBwgJEAAYjwLSAQg1MjYyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
if __name__ == "__main__":
                wishme()
                while True:
                                mainprogram()
                
