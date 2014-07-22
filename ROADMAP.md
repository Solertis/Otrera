The final version of the open source Otrera project should include the following:

	- A fully functioning RPG combat and level progression system
	- A rich variety of sample content including character classes, skills, and equipment
	- A basic suite of analytics services to gauge game balance
	- The ability to quickly generate and test new skills, classes, and complete games
	- High quality, tested code with complete documentation

The Otrera WebApp, which will include paid features, should do the following:

	Users can change attribute and stat names
	Users can define their own classes
	Users can define weapons, armor, equipment
	Users can get statistics on combat efficacy for balancing
	Users can define enemies
	Users can print out character sheets and game manuals
	Users can host games and scenarios for private use / kickstarter / whatever

HIGH-LEVEL NOTES

	Otrera needs the ability to publish full games. Each game directory should
	have its own data directory with files for skills, gear (everything.json)
	as well as scenario and characters. Essentially a game built from the
	Otrera engine should just be a set of JSON files utilized by the Python
	modules.

	The degree to which non-developers will be able to change the engine is
	unclear at this point. While anyone who knows Python can easily fork and
	tweak the code to their heart's content, there is only so much users of
	the web GUI will be able to do without the ability to alter the source code.

	I would be satisfied if users were at least able to change attribute and
	stat names. The ability to remove class skills, class attribute bonuses,
	or classes altogether, would also be cool I think, and probably not overly
	complex. Letting users change attribute --> stat mappings however is where
	things get hairy. Not only would that screw with game balance (do we want
	to let users make unbalanced games?) but it would require substantial
	refactoring of code, as those mappings are currently in a Python module.
	
	There is no reason why attribute --> stat mappings cannot be encoded in
	JSON and made editable. Nevertheless, this is not an immediate priority.

SPECIFIC TODO's
=======
	
TODO

1. Add more sample data to JSON files -- NEXT PRIORITY

2. Create content editor program (JSON tweaker)

3. Create tests for your code (Debugging is slow and shitty now)

4. Cleanup code, add comments, error-handling, etc. -- Will do after game publishing milestone

5. Improve your documentation!

6. Make complete character builder print well-designed character sheets

7. Find a way to quantify a character's combat efficacy

8. Make a random and class-based character generator

9. Create methods for generating teams of characters with a team combat efficacy

10. Rebalance attributes and stats after analyzing thousands of characters

11. Add concept of enemies (Tagged character objects? New object?)

12. Make a simple frontend for the different builder programs

13. Create game builder

14. Host everything somewhere. Improve GUI / website design. Monetize "point and click" services.

The repo and source code will always remain free (as in freedom) and open.
The 'Daughters of Ares' game (among other projects) will remain a proprietary fork.
