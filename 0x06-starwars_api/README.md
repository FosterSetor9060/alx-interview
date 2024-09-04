0x06. Star Wars API
Algorithm Specialization
Overview
The “0x06. Star Wars API” project involves interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you’ll need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

Concepts Needed
HTTP Requests in JavaScript:
Understand how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
A Complete Guide to Making HTTP Requests in Node.js
Working with APIs:
Understand the basics of RESTful APIs and how to interact with them.
Know how to parse JSON data returned by APIs.
Working with APIs in JavaScript
Asynchronous Programming:
Manage asynchronous operations with callbacks, promises, and async/await syntax.
Handle API response data asynchronously.
Asynchronous Programming in JavaScript
Command Line Arguments in Node.js:
Use the process.argv array to access command-line arguments passed to a Node.js script.
How to Parse Command Line Arguments in Node.js
Array Manipulation and Iteration:
Iterate over arrays and manipulate data structures to format and display character names.
JavaScript Array Methods
By familiarizing yourself with these concepts and resources, you’ll be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API. This project demonstrates your ability to work with external APIs and manage asynchronous code in JavaScript.

Requirements
General:
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS using Node (version 10.14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file at the root of the project folder is mandatory
Your code should be semistandard compliant (Rules of Standard + semicolons on top). Also, as a reference: AirBnB style
All your files must be executable
Task
0. Star Wars Characters
Write a script that prints all characters of a Star Wars movie:
The first positional argument passed is the Movie ID (example: 3 = “Return of the Jedi”).
Display one character name per line in the same order as the “characters” list in the /films/ endpoint.
You must use the Star Wars API.
You must use the request module.
Example Usage
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
