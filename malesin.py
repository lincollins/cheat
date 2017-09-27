#### This is Male's Single
#### We are going to do all Male singles in here
#### We hope to do some import too?
#### Sure, cus the others like 35.py, cheatad.py and the latest failure cheatcrack.py
#### I guess you know the story
#### But Dawn is a real warrior! And Real Warriors never quit!


from sys import exit
from random import randint


class Game(object):
    """ Game Class. """

    def __init__(self, start, user_name):
        self.quips = [
            "Not so good to hear. Sorry though, gotta leave you alone",
            "And now I guess you've to tour the Island alone ",
            "And now, you've got to learn to be a good man. Sorry though ve to leave you :(",
            "Ooops, did I just say your residence is ready? Well I guess its a typographical error."
        ]
        self.start = start
        self.user_name = user_name

    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit()

    def bye(self):
        print "No problem, lets get going :)"
        exit()

    def help(self):
        print """
\t Possible Words
   --------------------
\n\t 'wink back'
\n\t 'smile'
\n\t 'frown'
\n\t 'get a blanket'
\n\t 'talk to her'
\n\t 'have sex'
\n\t 'smile and walk away'
\n\t 'sit down'
    -------------------
        """

    def single(self):
        print "Welcome %s once again to Dawn's Island" % self.user_name
        print "We love exposing Cheaters."
        print "And this Island is no exception."
        print "And because you're our new citizen, I would love to show you around."
        print "Before then some few questions please"
        print "Need Help? Just ask. Nevertheless, we would've to start all over again."
        print "\nYou see a beautiful Princess with a shiny crown."
        print "She gives you a wink"
        print "\nWhat do you do in return?"

        flirt_it = raw_input(">>> ").lower()

        if flirt_it == "wink back":
            print "Oh yeah? I said it. I knew you would be a cheat"
            print "Uh uh, on your first day of seeing her?"
            print "No way, you gotta be out"
            return self.death()

        elif flirt_it == "smile":
            print "Hm, I can see you a good man"
            print "I guess by now your residence is ready"
            return self.in_house()

        elif flirt_it == "frown":
            print "Oops, you seems not be friendly"
            print "I hope you change though"
            return self.death()

        elif flirt_it == "help":
            print "Ok, so you need help"
            return self.help()
        else:
            print "%s the Princess looks at you confused" % user
            print "Well lets start all over again shall we?"
            return self.single()

    def in_house(self):
        print "Its cold in the evening hours"
        print "And the Princess is lying on a bed obviously shivering from the cold weather"
        print "\nWhat would you do?"

        house = raw_input(">>> ").lower()

        if house == "get a blanket":
            print "Well that's a good news. Thumbs up."
            print "I ve always thought of you been a good persona."
            print "I knew you would said that."
            return self.on_bed()

        elif house == "talk to her":
            print "No way, I just said she is feeling cold"
            print "I guess you dont care about her"
            return self.death()

        elif house == "have sex":
            print "And now you just confirmed your exit status"
            print "She will not need that"
            print "And well she is married too"
            return self.death()

        elif house == "help":
            print "Ok, so you need help"
            return self.help()

        else:
            print "The Princess keeps staring at you friend. Puzzled"
            return self.in_house()

    def on_bed(self):
        print "You cover her with the blanket"
        print "She says 'Thank you' and smiles at you\n"
        print "What comes to mind?"

        on_bed = raw_input(">>> ").lower()

        if on_bed == "smile and walk away":
            print "You're a good man after all"
            print "\nWelcome to Dawn's Island :)"
            return self.island()

        elif on_bed == "sit down":
            print "Hm, and the Husband comes in to catch you"
            print "You are not lucky after all"
            return self.death()

        elif on_bed == "help":
            print "Ok, so you need help"
            return self.help()

        else:
            print "She is smiling at you my friend. And all you do is stare at her?"
            print "Seriously?"
            return self.on_bed()


    def island(self):
        print "My new found friend wants to explore the Island more"
        print "And well, I am glad to follow suite :)"
        print "I hope you will enjoy this place though"
        print "\nHave an old friend you want to bring along please?"

        ans = raw_input(">>> ").lower()

        if ans == "yes":
            print "Thank you my friend."
            return self.single()
        elif ans == "no":
            print "Awww, hope they come by one day though."
            return self.bye()
        else:
            print "I got no idea what that means please :("
            print "Thinking of help, sorry my friend. None here"
            return self.island()


print "HELLO AND WELCCOME TO DAWN'S ISLAND."
print "I am Phillipine your country girl.\n"
print "Please, what do I call you?"

user_name = raw_input(">>> ")
a_game = Game("single", user_name)

while True:
    print """
-------------------------------------------------------------------------------
-------------------- ------------------------------------ ---------------------
------------------     --------------------------------     -------------------
----------------         ----------------------------         -----------------
--------------             ------------------------             ---------------
------------                 --------------------                 -------------
---------                      ----    ----    ----   ----    ---- ---   ----
----     --                   -------    ----    ----   ----    ---- ---   ----
----      --                ---- ----    ----    ----   ----    ----  ---  ----
----        --            ----   ----    ----    ----   ----    ----   --- ----
----        --          ----  -- ----    ----    ----   ----    ----    -------
----       ---        ----    -- ----    ----    ----   ----    ----     ------
----      --        ----         ----    -------------------    ----      -----
----------        ----           ----    -------------------    ----       ----

     """

    a_game.single()
