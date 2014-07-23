PROJECT MILESTONES
==================

1. Complete character builder -- COMPLETE 7/21/2014

	Users can create characters on top of the default engine and customize their
	attributes, equipment, skills, class, and level, and see the resulting stats.

2. Complete game publisher -- GOAL 7/27/2014

	Users can create complete games as JSON blobs. When the user selects a game
	(for character builder or content editor) the Python modules just take in
	a game name to get the correct path to the proper JSON directory.

3. Flask frontend for character builder -- GOAL 8/10/2014

	Users should be able to do all of the character builder, content editing,
	and game publishing functions through a webapp. Ideally this milestone
	will include auth/login and some way to accept payments. The website is the
	main paid service, the code will remain free.

4. Analytics -- GOAL 8/31/2014

	Users can get efficacy ratings for different character builds. Otrera should
	be able to gauge how balanced a game is based on its classes, skills, and
	equipment. While I have some ideas on how to do this, I know it will require
	a lot of testing and some basic data science knowledge that may be beyond me.
	Will definitely need help here.

5. Full RPG Engine Builder -- 9/30/2014

	This is the Holy Grail here - giving users the ability to start from nothing
	and build their own engine. It is a level of abstraction higher than I intended
	to go, but after talking with a lot of RPG players and developers, it seems that
	this is perhaps the most important feature.
	
	In order for people to feel like a game they developed is really 100% 'theirs',
	they need to be able to start from nothing. Otrera can allow that if we can
	get users to properly describe the attributes they want and how they should
	effect various stats. It's actually not an insanely hard problem and I have ideas
	on how to do it. For one, players need analytical tools, and the ability to save
	their work. They should then be able to name their original creations, patent them
	if they want, and host any games or content they create on our site (for a price)
	or on their own sites.

The final version of the open source Otrera project should include the following:

	- A fully functioning RPG combat and level progression system
	- A rich variety of sample content including character classes, skills, and equipment
	- A basic suite of analytics services to gauge game balance
	- The ability to quickly generate and test new skills, classes, and complete games
	- The ability to create an original engine from scratch.
	- High quality, tested code with complete documentation

The Otrera WebApp, which will include paid features, should do the following:

	Users can change attribute and stat names
	Users can define their own classes
	Users can define weapons, armor, equipment
	Users can get statistics on combat efficacy for balancing
	Users can define enemies
	Users can build an engine from the ground up
	Users can print out character sheets and game manuals
	Users can host games and scenarios for private use / kickstarter / whatever

SHORT-TERM PRIORITIES
=====================
	
TODO

1. Add more sample data to JSON files -- IN PROGRESS

2. Create content editor program (JSON tweaker)

3. Batch creation of content from CSVs

4. Add ability to publish character objects as named JSON files. This will also handle enemy objects.

5. Add ability to publish complete games as directories with JSON files

6. Create tests for your code (Debugging is slow and shitty now)

7. Cleanup code, add comments, error-handling, etc. -- Will do after game publishing milestone

8. Improve your documentation!

LONG-TERM PRIORITIES
====================

1. Analytics! Find a way to quantify a character's combat efficacy

2. Make a random and class-based character generator

3. Create methods for generating teams of characters with a team combat efficacy

4. Rebalance attributes and stats after analyzing thousands of characters

5. Formalize the analytics piece and do some play testing.

6. Flask frontend --> This can begin BEFORE the analytics stuff. Need help from web developers here

7. Make a nice website. Host somewhere (owned domains: otrera.org, otreragames.com)

8. Setup secure login, merchent features, hosting service for people's games

9. Engine builder!

The repo and source code will always remain free (as in freedom) and open.
