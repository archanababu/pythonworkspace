#-----------------------------
# Multiple choice quiz
#-----------------------------

from question import Question

questionPrompts = [
    "What is the color of an apple? \n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What is the color of a banana? \n(a) Red\n(b) Purple\n(c) Yellow\n\n",
    "What is the color of a strawberry? \n(a) Red\n(b) Purple\n(c) Orange\n\n"
]

questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "a")
]

def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

runTest(questions)
