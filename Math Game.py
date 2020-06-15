#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculateAnswer(lhs,rhs,operator):
    if(operator == "-"):
        return lhs - rhs
    if(operator == "+"):
        return lhs + rhs
    if(operator == "*"):
        return lhs * rhs
    if(operator == "/"):
        return lhs / rhs
    if(operator == "**"):
        return lhs ** rhs
    raise Exception("Unknown Operator")


def isAccurateEnoughAnswer(givenAnswer, correctAnswer, tolerance = 0.01):
    difference = abs(float(givenAnswer) - float(correctAnswer))
    return difference <= tolerance


from random import randint
def generateQuestion():
    ops = "**/-+*"
    opIndex = randint(0,len(ops)-1)
    operator = ops[opIndex]
    lhs = randint(-10,10)
    rhs = randint(-10,10)
    while(operator == "/"):
        rhs = 2
    return lhs, rhs, operator

totalQuestions = 10
correct = 0
for i in range(totalQuestions):
    question = generateQuestion()
    correctAnswer = calculateAnswer(question[0],question[1],question[2])
    playerAnswer = input("{0} {2} {1} = " .format(question[0],question[1],question[2]))
    if(str(correctAnswer) == playerAnswer):
        print("Correct!")
        correct += 1
    else:
        print("Wrong. Correct answer = " + str(correctAnswer))       
print("You got {0} correct out of {1}, or {2}% correct".format(correct, totalQuestions, correct/totalQuestions*100))




# %%
