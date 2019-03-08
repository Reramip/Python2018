import random

class Contestant:
    def __init__(self, name = "", score = 0):
        self._name = name
        self._score = score

    def getName(self):
        return self._name

    def getChoice(self):
        return self._choice

    def addScore(self):
        self._score += 1

    def getScore(self):
        return self._score

class Human(Contestant):
    def choose(self, choice):
        self._choice = choice

class Computer(Contestant):
    def choose(self):
        self._choice = random.choice(["rock", "scissors", "paper"])

def main():
    rsp = ["rock", "scissors", "paper"]
    human = Human(input("Enter name of human: "))
    computer = Computer(input("Enter name of computer: "))
    for i in range(3):
        human.choose(input(human.getName() + ", enter your choice: "))
        computer.choose()
        print(computer.getName(), "chooses", computer.getChoice())
        if human.getChoice() == rsp[0]:
            if computer.getChoice() == rsp[1]:
                human.addScore()
            elif computer.getChoice() == rsp[2]:
                computer.addScore()
        elif human.getChoice() == rsp[1]:
            if computer.getChoice() == rsp[2]:
                human.addScore()
            elif computer.getChoice() == rsp[0]:
                computer.addScore()
        elif human.getChoice() == rsp[2]:
            if computer.getChoice() == rsp[0]:
                human.addScore()
            elif computer.getChoice() == rsp[1]:
                computer.addScore()
        print('\n' + human.getName()+':', human.getScore(), ' ', computer.getName()+':', computer.getScore())
    if human.getScore() > computer.getScore():
        print("\n" + human.getName().upper(), "WINS")
    elif human.getScore() == computer.getScore():
        print("\nDRAW GAME")
    else:
        print('\n' + computer.getName().upper(), "WINS")

main()