import random
def TellJoke():
    #JOKECOUNT=JOKECOUNT+1 #TODO We need to increment the joke counter so that we know we have already told the joke today
    #JOKETIME              #TODO We keep track of the joke time so that we know when we have told the joke.
    JOKE=[["Where do you find a dog with no legs?","Where you left him"],
               ["How do you a man with one arm out of a tree?","You wave to him"],
               ["What do you call a dear with no eyes?","no eyes deer"],
               ["What do you call man with no arms and no legs swiming in the ocean?","Bob"],
               ["What has six legs, is green and brown and if it fell from a tree it would kill you?","A pool table"]]
    JOKELENGTH=len(JOKE)
    joke=random.randint(1,JOKELENGTH-1)
    C=JOKE[joke]
    Q=C[0]
    A=C[1]
    print(Q)
    print(A)
TellJoke()
