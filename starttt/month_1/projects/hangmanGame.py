import random

stages = [
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]


words = [
    "apple", "ball", "cat", "dog", "fish", "tree", "milk", "book", "star", "chair",
    "planet", "guitar", "butter", "camera", "banana", "window", "castle", "jungle", "pirate", "rocket",
    "elephant", "psychology", "dinosaur", "umbrella", "submarine", "laboratory", "microscope", "zookeeper", "volcano", "aviation",
    "python", "function", "variable", "compile", "algorithm", "database", "network", "boolean", "syntax", "iterator"
]
word=random.choice(words)

lives=6
placeholder=""
for position in range(len(word)):
    placeholder += "_"

over=False
correct_let=[]
while not over:
    guess=input("guess a letter:").lower()

    display=""
    for letter in word:
      if letter==guess:
        display += letter
        correct_let.append(guess)
      elif letter in correct_let:
         display += letter
         
      else:
       display += "_"
    print(display)

    if guess not in word:
       lives=lives-1
       print(f"oops! you lost a life,  {lives}  lives left")
       if lives==0:
          over=True
          print("you lost:(")
    if "_" not in display:
      print("You won! :)")
      over=True
    print(stages[lives])