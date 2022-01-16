# A game where the user answers certain questions and gets a point if answered correctly and no points otherwise

print("Hi welcome to my mini program called 'Quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's get started!")


def my_quiz():
    score = 0

    answer = input(
        "Question 1: Julia is born in 1998, how old is she now in the year of 2022 (considering she already had her birthday this year)? ").lower()
    if answer == "24":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input("Question 2: Julia graduated from the Technical University Munich. Is that correct? ").lower()
    if answer == "yes":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input("Question 3: Julia can speak 4 languages. Is this correct? ").lower()
    if answer == "no":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input(
        "Question 4: Julia can speak English, German, Chinese, French, Japanese and Korean. Which language does not belong in this sentence? ").lower()
    if answer == "japanese":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input(
        "Question 5: Julia went abroad and went to the well-known Zhejiang University in Hangzhou. Right or wrong? ").lower()
    if answer == "right":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input("Question 6: Does Julia like to cook? ")
    if answer.lower() == "yes":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input("Question 7: Does Julia play the guitar? ").lower()
    if answer == "yes":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    answer = input("Question 8: Does Julia eat meat? ").lower()
    if answer == "no":
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print("You finished this quiz with " + str(score) + " points! This means you answered " + str(
        (score / 8) * 100) + "% correctly!")
    if score >= 6:
        print("Congratulations! You seem to know Julia pretty well!")
    else:
        print("Hmm...seems like you do not know Julia that much yet. There is still room for improvement!")
        repeat = input("Would you like to play again? ").lower()
        if repeat == "yes":
            my_quiz()
        else:
            quit()


my_quiz()
