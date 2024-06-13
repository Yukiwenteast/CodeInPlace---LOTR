import os
from PIL import Image

# Define the directory where images are stored
image_directory = "Pics"

print("Welcome to Realm of the Lord Of The Rings")
print("")
print("Now we enter the Fellowship of the Ring - verse")
print("")
print("Press Enter if you are ready...")


# Define the quiz questions and answers
# Round 1
Fellowship_quiz = [
    {
        "question": "What part of the Shire does Frodo live in before Gandalf gives him the ring?",
        "choices": ["A. Bag End", "B. Minas Tirith", "C. Brandybuck", "D. Mirkwood"],
        "answer": "A"
    },
    {
        "question": "Who stabbed Frodo?",
        "choices": ["A. Aragorn", "B. The Witch King of Angmar", "C. I did!!", "D. Gollum"],
        "answer": "B"
    },
    {
        "question": "Who saved Frodo and the hobbits from the ringwraiths?",
        "choices": ["A. Elrond", "B. Gandalf", "C. Aragorn", "D. Of course, us!"],
        "answer": "C"
    },
    {
        "question": "What last name does Frodo use at the Prancing Pony Inn?",
        "choices": ["A. Baggins", "B. Rohirrim", "C. Underhill", "D. Sauron"],
        "answer": "C"
    },
    {
        "question": "Where is Legolas' father king?",
        "choices": ["A. Rohan", "B. Mordor", "C. Mirkwood", "D. Anywhere, but here!"],
        "answer": "C"
    }
]

#Round 2
TwoTowers_quiz = [
    {
        "question": "What are Saruman's warriors called?",
        "choices": ["A. Uruk-Hai", "B. Orcs", "C. Ushbak-Nazki", "D. Mazca-lirda"],
        "answer": "A"
    },
    {
        "question": "Who do the Fellowship run into that help them to find Merry and Pippin?",
        "choices": ["A. The Rangers of Gondor", "B. Riders of Rohan", "C. The dwarves of Black Hill", "D. Me"],
        "answer": "B"
    },
    {
        "question": "What is the name of the orc that tries to eat Merry and Pippin in the forest?",
        "choices": ["A. Shelob", "B. Ringworm", "C. Grishnakh", "D. Theodred"],
        "answer": "C"
    },
    {
        "question": "Which creature helps Marry and Pippin?",
        "choices": ["A. An Elf", "B. An Orc", "C. An Ent", "D. James Bond"],
        "answer": "C"
    },
    {
        "question": "Through where does Gollum lead Frodo and Sam to avoid detection?",
        "choices": ["A. Misty Mountain", "B. Rohan", "C. The Dead Marshes", "D. Minas Tirith"],
        "answer": "C"
    }
]

# Round 3
ReturnKing_quiz = [
    {
        "question": "What is the name of Theoden's niece?",
        "choices": ["A. Eowyn", "B. Arwen", "C. Galadriel", "D. Beyonce"],
        "answer": "A"
    },
    {
        "question": "What is Frodo and Sam's final destination?",
        "choices": ["A. Rivendell", "B. Mount Doom", "C. Shire", "D. Moria"],
        "answer": "B"
    },
    {
        "question": "Where does Frodo go at the end of the book?",
        "choices": ["A. Middle Earth", "B. Mordor", "C. The Undying Lands", "D. Mirkwood"],
        "answer": "C"
    },
    {
        "question": "The title Return of the King refers to one of the main characters, who is he?",
        "choices": ["A. Thorin Oakenshield", "B. Legolas", "C. Aragorn", "D. Boromir"],
        "answer": "C"
    },
    {
        "question": "Who said the following quote:There never was much hope. Just a fool's hope.”",
        "choices": ["A. Saruman", "B. Aragorn", "C. Gandalf", "D. Not me, for sure!"],
        "answer": "C"
    }
]

# Initialize the score
score = 0

# Function to show the image
def show_image(image_path):
    img = Image.open(image_path)
    img.show()

# Function to run the quiz
def run_quiz(quiz):
    global score
    for i, q in enumerate(quiz):
        print(f"Question {i + 1}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    
# Run Round 1
print("Fellowship of the Ring-verse")
run_quiz(Fellowship_quiz)

# Determine if the user goes to Round 2
if score > 2:
    print(f"Your score is {score} out of {len(Fellowship_quiz)}. You qualify to enter the realm of The Two Towers!\n")
    #show_image(os.path.join(image_directory, "Pass.gif"))
    print("The Two Towers-verse")
    run_quiz(TwoTowers_quiz)


# Determine if the user goes to Round 3
if score > 5:  # Scoring criteria for Round 2
    print(f"Your score is {score} out of {len(Fellowship_quiz+TwoTowers_quiz)}. You qualify to enter the realm of Return Of The King!\n")
    print("Return of The King-verse")
    run_quiz(ReturnKing_quiz)

# Display final score and end message
print(f"Your final score is {score} out of {len(TwoTowers_quiz+Fellowship_quiz+ReturnKing_quiz)}.")
if score > 10:
    show_image(os.path.join(image_directory, "Pass.gif"))
    print("You bow to NO ONE")
else:
    show_image(os.path.join(image_directory, "Youshallnotpass.jpeg"))
    print("YOU SHALL NOT PASS")


#test
