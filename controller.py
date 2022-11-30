from PyQt5 import QtCore, QtGui, QtWidgets
from view import *
from PyQt5.QtWidgets import *
import pymsgbox, time, sys, pymsgbox, string_utils,pygame
from gtts import gTTS
from os.path import exists
from pygame.locals import *
import enchant


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
class SCRAMBLE:
    all_words=[]  # Class Variable
    def __init__(self,spelling_words):
        """
        Initial function to create mp3 from spelling list if it does not already exist
        :param spelling_words:  spelling list        
        """
        self.spelling_words = spelling_words
        for word in self.spelling_words:
            if exists(f'{word}.mp3')==True:
                pass
            else:
                try:
                    if exists('AnsRight.mp3') == False:
                        tts = gTTS(text="That's right", lang='en')
                        tts.save('AnsRight.mp3')
                except:
                    pass
                try:
                    if exists('wrong.mp3') == False:
                        tts = gTTS(text="That's wrong", lang='en')
                        tts.save('wrong.mp3')
                except:
                    pass
                try:                      
                    tts = gTTS(text=word, lang='en')
                    tts.save(f'{word}.mp3')
                    if exists(f'{word}.mp3') == True: # For some reason the code will not perform correctly without this line
                        pass
                except Exception as e:
                    pass
   
    def play_mp3(word) -> None:
        """
        Function to play the saved mp3 file that matches the word
        :param word: the word that wants to be played
        """
        try:
            if word != "":
                pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(f'{word}.mp3')
                pygame.mixer.music.play()
                return
        except:
            pymsgbox.alert("Could not play mp3")   
            return 
    
    def scramble(spelling_words) -> tuple:
        """
        Function to scramble each word in the spelling list.
        :param spelling_words: spelling list
        :return: return the correct word and the scramble word        
        """
        for word in spelling_words:    
            if word == "":
                pass  
            if word in SCRAMBLE.all_words:
                pass
            else:
                random_word=(string_utils.shuffle(word))
                SCRAMBLE.all_words.append(word)
            return word,random_word

class Controller(QMainWindow, Ui_MainWindow):
    #####   Class Variables #####
    spelling_list=[]
    correct_word=""
    entries=[]
    label_entries=[]
    temp_list=[]
    x=-1
    ###############################
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.btn_speak.clicked.connect(lambda: SCRAMBLE.play_mp3(Controller.correct_word))
        self.btn_validate.clicked.connect(lambda: self.validate(Controller.correct_word))
        self.edit_words = EditWordsWindow()
        self.add_words()
        
    def finish_gui(self) -> None:
        '''
        Function finishes the setup process. Adds words to the list and creates stacked widgets for errors. Calls next word to begin scrammble game.
        :param edit_words: provides instance of pop up window 
        '''   
        if len(Controller.temp_list) > 0:
            self.show()
            for word in Controller.temp_list:
                if word == "":
                    Controller.temp_list.remove(word)
                else:
                    Controller.spelling_list.append(word)
            SCRAMBLE(Controller.temp_list)
            self.create_stacked()
            Controller.temp_list.clear()
            self.edit_words.hide()
            self.next_word()
        else:
            pymsgbox.alert("Please enter a word to begin")
        
    def add_words(self) -> None:
        '''
        Function to show the pop up window at the correct stacked widget index. provides functionality for the add and done buttons.
        '''
        self.edit_words.show()
        self.edit_words.stackedWidget.setCurrentIndex(0)
        self.edit_words.btn_add.clicked.connect(lambda: self.retrieve_new_words())
        self.edit_words.btn_done.clicked.connect(lambda: self.finish_gui())
            
    def retrieve_new_words(self) -> None:
        """
        Function to get new spelling words
        :return: returns spelling word(s)
        """
        d = enchant.Dict("en_US")
        new_word = self.edit_words.lineEdit_addWord.text().lower()
        if d.check(new_word):
            Controller.temp_list.append(new_word)
        else:
            pymsgbox.alert("Not a valid word")
        self.edit_words.lineEdit_addWord.setText("")
        
    def exit_program(self) -> None:
        '''
        Function to end the program. Asks for confirmation
        '''
        answer = pymsgbox.confirm("Are you sure?")
        if answer == 'OK':
            sys.exit()        
                
    def create_stacked(self) -> None:
        """
        Function to create stacked widgets in the range of the length of the spelling list
        """
        if len(Controller.temp_list) > 0:
            for i,word in enumerate(Controller.temp_list):
                e = QtWidgets.QWidget()
                e.setObjectName(word)
                e.setLayout(QtWidgets.QHBoxLayout())
                self.stackedWidget.addWidget(e)
                Controller.entries.append(e)
                
                all_labels=[]
                for letter in word:
                    label = QtWidgets.QLabel()
                    label.setObjectName(letter)
                    label.setFont(QtGui.QFont('Arial', 18))
                    Controller.entries[i].layout().addWidget(label)
                    all_labels.append(label)
                Controller.label_entries.append(all_labels)
                    
    def reset_labels(self) -> None:
        '''
        Function to reset the labels to default
        '''
        for x,entry in enumerate(Controller.spelling_list):
            correct_word = entry
            for i,letter in enumerate(correct_word):
                label = Controller.label_entries[x][i]
                label.setText("")
                label.setStyleSheet("")
                
    def validate(self,correct_word) -> None:
        """
        Function to validate the users response. It takes the users phrase and creates color coded labels for correct/wrong letters
        :param correct_word: correct word to validate with
        :return: return None if errors
        """
        if correct_word != "":
            phrase = self.lineEdit_scramble.text()  # users response
            
            ########## Exception Handling  ###############
            if phrase == "":
                alert = pymsgbox.alert("Enter a word!!!")
                return
            if len(phrase) < len(correct_word) :
                alert = pymsgbox.alert("Not enough letters!")
                return
            if len(phrase) > len(correct_word):
                alert = pymsgbox.alert("Too many letters!")
                return
            ##############################################
            
            if phrase == correct_word:  # correct response      
                SCRAMBLE.play_mp3("AnsRight")
                time.sleep(3)
                Controller.spelling_list.pop(0)
                self.next_word()
            else:                       # Incorrect response
                for i,letter in enumerate(correct_word):
                    if letter == phrase[i]:  # colors letters green if correct
                        label = Controller.label_entries[Controller.x][i]
                        label.setText(phrase[i])
                        label.setStyleSheet("background-color: lightgreen")
                        
                    else:                     # colors letters pink if incorrect
                        label = Controller.label_entries[Controller.x][i]
                        label.setText(phrase[i])
                        label.setStyleSheet("background-color: pink")
                SCRAMBLE.play_mp3("wrong") 
        else:
            pymsgbox.alert("Please add spelling words!")
    
    def next_word(self) -> None:
        """
        Function used to go to the next word
        uses stacked widgets
        
        """
        self.lineEdit_scramble.setText("")  # clear user text
        Controller.x += 1  # set index value
        self.stackedWidget.setCurrentIndex(Controller.x)
        try:
            if len(Controller.spelling_list) > 0:
                Controller.correct_word,scrambled_word = SCRAMBLE.scramble(Controller.spelling_list)
        except Exception as e:
            pass
        if len(Controller.spelling_list) == 0:
            Controller.spelling_list=SCRAMBLE.all_words
            SCRAMBLE.all_words=[]
            ans=pymsgbox.confirm("Do you want to start over? ")
            if ans=='OK':
                Controller.correct_word,scrambled_word = SCRAMBLE.scramble(Controller.spelling_list)
                self.lineEdit_scramble.setText("")
                Controller.x = 0
                self.stackedWidget.setCurrentIndex(Controller.x)
                self.reset_labels()
            else:
                sys.exit()
        try:
            self.label_scramble.setText(scrambled_word)
        except:
            pass