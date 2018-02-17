import random

s_nouns = ["a dude", "my mom", "the king", "some guy", "a cat with rabies", "a sloth", "your homie", "this cool guy my gardener met yesterday", "superman"]
p_nouns = ["these dudes", "both of my moms", "all the kings of the world", "some guys", "all of a cattery's cats", "the multitude of sloths living under your bed", "your homies", "like, these, like, all these people", "supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]
ends = ['.', '?', '!']

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''

    text1 = ' '.join([random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns) ])
    text2 = ' '.join([random.choice(p_nouns), random.choice(infinitives)])
    finall = text1 or text2
    return(''.join([finall.capitalize(), random.choice(ends)]))

def text_gen(n=1):
    return ' '.join([sing_sen_maker() for i in range(n)])