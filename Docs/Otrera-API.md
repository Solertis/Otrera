Otrera API Doc
===============

***This document is a work in progress***

== Overview

Otrera is an open source Python library for making table top games. It is optimized around traditional pen & paper role-playing game systems, but can be used to described almost any sort of game system.

Otrera describes games in a single JSON file. This engine.json file has a set of root keys known as Constructs. The only Construct that exists by default is that of CHARACTER. The user starts by describing the things that define a character - race, level, class, stats, attributes, etc. Each of these in turn become constructs that the user can describe with fields, number values, and dependency relationships.

The engine.py file then parses the engine.json file and creates characters based on the rules laid out in the game engine. Users can then use the content editing modules to add content (specific skills, characters, classes, etc.) and use the builder module to create characters.

The core output of Otrera is the JSON file that describes a game. This file may describe an abstract engine, a game that references another engine, or a game/engine combination for non-general purpose engines. This output file can then be ingested by other programs, such as the Otrera Analytics Service and the Otrera WebApp (both still in very early development phases).
