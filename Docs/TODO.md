TODO (for contributors)
=======================

Comment here on github or e-mail TheWitchAgatha@gmail.com if you want to take a task.	

1. Add error checking (try/catch, etc) to methods

2. Add docstrings / comments

3. Improve CLI (help text, configurability with yaml, packaging)

4. Improve engine.py
	- This one is pretty complex. Contact me if you are up for a challenge.

5. Add CSV parsing and upload for default engine
	- The addContent and editContent modules should be the starting point
	- Ideally the program will tell users the right column/row format based on the engine

6. Add batch operations
	- Changes to a game engine should propegate in the game content
	- Ex. Removing 'durability' from weapons template
	- All weapons should then be updated and have that field removed

7. Flask App
	- This will live in another repo, however I may do a proof of concept on a branch here
	- Any contributors with Flask experience can take this ticket or contact me about it.

This TODO does not cover 'Engine Builder' goals. Those will be added here once the above priorities are complete.
