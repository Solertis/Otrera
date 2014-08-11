Otrera API Doc
===============

***This document is a work in progress***

== Overview

Otrera is an open source Python library for making table top games. It is optimized around traditional pen & paper role-playing game systems, but can be used to described almost any sort of game system.

== Basic Structure

Otrera describes games in a single JSON file. This engine.json file has a set of root keys known as Constructs. Constructs are abstractions like 'Equipment' or 'Performance'. Users select which apply to their game engine and select Schemes - instantiations of Constructs. A Scheme for the Equipment construct would be something like "Weapons" or "Gold", any sort of physical thing a character might carry.

Constructs and Schemes serve as the templates for game content. Game content lives in a separate content.json file in a subdirectory of an engine. Games depend upon engines to work. 'Content' can be thought of as an instantiation of a Scheme. Thus the full hierarchy is as follows:

Construct -> Scheme -> Content

Some examples:

Ability -> Magic -> Fire Bolt +
Character -> NPC -> Inquisitor Larry +
Performance -> Attribute -> Dexterity +

The engine.json file does not only contain Constructs it Schemes, it also defines relationships between these systems with special keywords. Users can have character attributes depend upon class, usable weapons depend on race, level progression depend on skills, etc. etc.

== Games and Engines

An engine is a set of rules and relationships. A game is defined by its content. It is possible to create an engine with zero content and keep it purely as a framework for other games. It is also possible to lock engines to particular games for users who do not wish to create general purpose engines.

It is also possible to build new games on top of old games. Users can allow others to edit the content in a content.json file or add new pieces and rename others. This allows for multiple levels of game development complexity and scope based on what the user wishes to do. A basic hierarchy of the complexity:

Most: Creating a new engine from scratch with at least one game +
Moderate: Creating an original game on top of an existing engine. +
Lowest: Altering the content of an existing game and renaming it as a new game or campaign. +

This is a very rough hierarchy in that the difficulty in creating a game is a function of the volume of content and complexity of the game engine. In theory, a person might be able to create a new engine in a matter of minutes, while devising all of the spells, equipment, classes, and characters for a new game (or addon campaign) may take weeks.

In practice the content.json file that defines a game is much larger than the engine.json file that describes the game system. Consider that games like Pathfinder have hundreds of spells. Any singe piece of content is comparable in size to the scheme that sets its template.
