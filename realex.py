#### This is Male's Single
#### We are going to do all Male singles in here
#### We hope to do some import too?
#### Sure, cus the others like 35.py, cheatad.py and the latest failure cheatcrack.py
#### I guess you know the story
#### But Dawn is a real warrior! And Real Warriors never quit!


from sys import exit
from random import randint

class Game(object):

	def __init__(self, start):
		self.quips = [
			"Not so good to hear. Sorry though, gotta leave you alone",
			"And now I guess you've to tour the Island alone ",
			"And now, you've got to learn how to be a better person. Sorry though ve to leave you :(",
			"Ooops, did I just say your residence is ready? Well I guess its a typographical error."
		]
		self.start = start

	def play(self):
		next = self.start

		while True:
			print """
-------------------------------------------------------------------------------		
\n---------                        ----    ----    ----   ----    ---- ---   ----
----    ---                   -------    ----    ----   ----    ---- ---   ----
----     ---                ---- ----    ----    ----   ----    ----  ---  ----
----       ---            ----   ----    ----    ----   ----    ----   --- ----
----       ---          ----  -- ----    ----    ----   ----    ----    -------
----      ---         ----    -- ----    ----    ----   ----    ----     ------
----    ---         ----         ----    -------------------    ----      -----
----------        ----           ----    -------------------    ----       ----

-------------------- ----------------------------------------------------------
			"""
			room = getattr(self, next)
			next = room()

	def death(self):
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)

	def bye(self):
		print "No problem, lets get going :)"
		print "Elm...just maybe I'm been to inquisitive though..."
		print "\nAre you Single or Married?"

		mar = raw_input(">>> ")

		if mar == "Single":
			print "Well thats kul."
			print "Would hope to get your invitation soon :)"
			return 'single_axe'

		elif mar == "Married":
			print "Wow, you know what I mean."
			print "High 5."
			return 'mar'

		else:
			print "I got no idea what that means please"
			print "Let's roll it back shall we?"
			return 'bye'



######################################################################
	def single_axe(self):
		print "So if ever you got married, would you ever kiss the opposite sex or so?"

		sin = raw_input(">>> ")

		if sin == "Yes": #a
			print "Well, what about phone sex?"
			return 'yesin'
		elif sin == "No": #b
			print "I see"
			return 'nosin'
		else:
			print "I got no idea what that means."
			print "Let's roll it back shall we?"
			return 'single'

	def nosin(self): #b1
		print "Tell me about it."
		print "What about phone sex?"

		nosin = raw_input(">>> ")

		if nosin == "Yes": #a1
			print "Ok, the last question actually."
			print "What about a secret date on the agender?"
			return 'final_sin'

		elif nosin == "No":#b
			print "Well I see"
			print "What about a secret date on the agender?"
			return 'no_sin_finale'

		else:
			print "I got no idea what that means."
			print "Lets roll it back shall we?"
			return 'nosin'

	def no_sin_finale(self):
		print "Anything secret shared with your lover other than your other darling?"

		no_sin_finale = raw_input(">>> ")

		if no_sin_finale == "Yes":
			print "Incredible"
			return 'nosin_end'
		elif no_sin_finale == "No":
			print "Seriously?"
			return 'nosin_end'
		else:
			print "I got no idea what that means."
			return 'no_sin_finale'

	def finale_sin(self):
		print "Would you ever have a secret date on the list"

		finale_sin = raw_input(">>> ")

		if finale_sin == "Yes":
			print "Well, I thought so"
			return 'end_sin'

		elif finale_sin == "No":
			print "Hm, thumbs up."
			return 'nosin_end'

		else:
			print "I got no idea what you saying"
			return 'finale_sin'

	def nosin_end(self):#b3
		print "Well, well, well."
		print "My good friend is not a cheat after all."
		print "And now we're at Governor Dawn's Palace."
		print "Don't worry, he will be with us in a moment."
		print "Hi Tech building you know :)"

		print "\nWants to know what Dawn got for you?"
		print "\nWell, that would be a different Chapter."
		print "\nAre you ready?"
		exit (0)


	def yesin(self):#a2
		print "Tell me about it."
		print "Would you my old friend?"

		yesin = raw_input(">>> ")

		if yesin == "Yes":
			print "Ok, the last question actually."
			print "What about a date on the agender?"
			return 'yes_in_finale' #### Cross check here again

		elif yesin == "No": ##### Re order here too
			print "Not the least friend."
			return 'finale_sin'

		else:
			print "I got no idea what that means pls"
			return 'yesin'

	def yes_in_finale(self):
		print "Huh?"

		yes_in_finale = raw_input(">>> ")

		if yes_in_finale == "Yes":
			print "Hm"
			return 'end_sin'
		elif yes_in_finale == "No":
			print "Ooops"
			return 'end_sin'
		else:
			print "I got no idea what that means"
			return 'yes_in_finale'

	def end_sin(self):
		print "So you're a cheat after all."
		print "Huh? Even before getting married."
		print "There is no way you're staying in our Honorable Dawn's Island"
		print "Get your stuffs and start packing out"
		exit(0)

	def end_sin_axe(self):
		print "Bye, Bye, Bye!"
		exit(0)
######################################################################
######################################################################

	def mar(self):
		print "So as you're married, would you ever kiss the opposite sex or so?"

		mar = raw_input(">>> ")

		if mar == "Yes": #a
			print "Well, what about phone sex?"
			return 'maryes'
		elif mar == "No": #b
			print "I see"
			return 'mar_no'
		else:
			print "I got no idea what that means."
			print "Lets roll it back shall we?"
			return 'mar'

	def mar_no(self): #b1
		print "Tell me about it."
		print "What about phone sex?"

		mar_no = raw_input(">>> ")

		if mar_no == "Yes": #a1
			print "Ok, the last question actually."
			print "What about a secret date on the agender?"
			return 'mar_finale'

		elif mar_no == "No":#b
			print "Well I see"
			return 'mar_finale'

		else:
			print "I got no idea what that means."
			print "Lets roll it back shall we?"
			return 'mar_no'

	def no_mar_finale(self):
		print "Anything secret shared with your lover other than your other darling?"

		no_mar_finale = raw_input(">>> ")

		if no_mar_finale == "Yes":
			print "Incredible"
			return 'mar_yes_end'
		elif no_mar_finale == "No":
			print "Seriously?"
			return 'mar_yes_end'
		else:
			print "I got no idea what that means."
			return 'no_mar_finale'

	def mar_finale(self): ##########################
		print "Yeah, the last question I think."

		mar_finale = raw_input(">>> ")

		if mar_finale == "Yes":
			print "Well, I thought so"
			return 'mar_end_axe'

		elif mar_finale == "No":
			print "Hm, thumbs up."
			return 'mar_yes_end'

		else:
			print "I got no idea what you saying"
			return 'mar_finale'

	def mar_yes_end(self):#b3
		print "Well, well, well."
		print "My good friend is not a cheat after all."
		print "And now we're at Governor Dawn's Palace."
		print "Don't worry, he will be with us in a moment."
		print "Hi Tech building you know :)"
		exit (0)


	def maryes(self):#a2
		print "Tell me about it."
		print "Would you my old friend?"

		maryes = raw_input(">>> ")

		if maryes == "Yes":
			print "Ok, the last question actually."
			print "What about a secret date on the agender?"
			return 'yes_in_finale_mar' #### Cross check here again

		elif yesin == "No": ##### Re order here too
			print "What about a secret date on the agender?"
			return 'mar_finale'

		else:
			print "I got no idea what that means pls"
			return 'maryes'

	def yes_in_finale_mar(self):
		print "Huh?"

		yes_in_finale_mar= raw_input(">>> ")

		if yes_in_finale_mar == "Yes":
			print "Hm"
			return 'mar_end_axe'
		elif yes_in_finale_mar == "No":
			print "Ooops"
			return 'mar_end_axe'
		else:
			print "I got no idea what that means"
			return 'yes_in_finale_mar'

	def mar_end_axe(self):
		print "So you're a cheat after all."
		print "Huh? Even while married."
		print "There is no way you're staying in our Honorable Dawn's Island"
		print "Get your stuffs and start packing out"
		exit (0)

	def mar_end(self):
		print "Bye, Bye, Bye!"
		exit(0)

#######################################################################
#######################################################################


	def help(self):
		print """
\t Possible Words
        -----------------
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
		exit(0)

	def single(self):
		print "HELLO AND WELCCOME TO DAWN'S ISLAND."
		print "I am Phillipine your country girl"
		print "\nPlease, what do I call you?"

		user = raw_input(">>> ")

		print "Welcome %s once again to Dawn's Island" % user
		print "We love exposing Cheaters."
		print "And this Island is no exception."
		print "And because you're our new citizen, I would love to show you around."
		print "Before then some few questions please."
		print "Need Help? Just ask. Nevertheless, we would've to start all over again."
		print "\nYou see a beautiful Princess with a shiny crown."
		print "She gives you a wink."
		print "\nWhat do you do in return?"

		flirt_it = raw_input(">>> ")

		if flirt_it == "wink back":
			print "Oh yeah? I said it. I knew you would be a cheat."
			print "Uh uh, on your first day of seeing her?"
			print "No way, you gotta be out."
			return 'death'

		elif flirt_it == "smile":
			print "Hm, I can see you're good."
			print "I guess by now your residence is ready."
			return 'in_house'

		elif flirt_it == "frown":
			print "Oops, you seems not be friendly."
			print "I hope you change though."
			return 'death'

		elif flirt_it == "Help":
			print "Ok, so you need help."
			return 'help'
		else:
			print "%s the Princess looks at you confused." % user
			print "Well lets start all over again shall we?"
			return 'single'

	def in_house(self):
		print "Its cold in the evening hours."
		print "And the Princess is lying on a bed obviously shivering from the cold weather."
		print "\nWhat would you do?"

		house = raw_input(">>> ")

		if house == "get a blanket":
			print "Well that's a good news. Thumbs up."
			print "I ve always thought of you been a good persona."
			print "I knew you would said that."
			return 'on_bed'

		elif house == "talk to her":
			print "No way, I just said she is feeling cold."
			print "I guess you dont care about her."
			return 'death'


		elif house == "have sex":
			print "And now you just confirmed your exit status."
			print "She will not need that."
			print "And well she is married too."
			return 'death'

		elif house == "Help":
			print "Ok, so you need help."
			return 'help'

		else:
			print "The Princess keeps staring at you my friend. Puzzled." 
			return 'in_house'

	def on_bed(self):
		print "You cover her with the blanket."
		print "She says 'Thank you' and smiles at you."
		print "\nWhat comes to mind?"

		on_bed = raw_input(">>> ")

		if on_bed == "smile and walk away":
			print "You're a good man after all."
			print "\nWelcome to Dawn's Island :)"
			return 'island'

		elif on_bed == "sit down":
			print "Hm, and the Husband comes in to catch you."
			print "You are not lucky after all."
			return 'death'

		elif on_bed == "Help":
			print "Ok, so you need help"
			return 'help'

		else:
			print "She is smiling at you my friend. And all you do is stare at her?" 
			print "Seriously?"
			return 'on_bed'


	def island(self):
		print "My new found friend wants to explore the Island more" 
		print "And well, I am glad to follow suite :)"
		print "I hope you will enjoy this place though"
		print "\nHave an old friend you want to bring along please?"

		ans = raw_input(">>> ")

		if ans == "Yes":
			print "Thank you my friend."
			return 'single'
		elif ans == "No":
			print "Awww, hope they come by one day though."
			return 'bye'
		else:
			print "I got no idea what that means please :("
			print "Thinking of help, sorry my friend. None here"
			return 'island'


a_game = Game("single")
a_game.play()
