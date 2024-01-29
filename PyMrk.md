## About
PyTerm is an engine to run scripts dynamically. The name PyTerm means Python and Terminal.
I created this around December or November 2023 after learning about the python builtin function `input()`

## Installation
To install run `sudo apt install python3 -y && git clone https://github.com/uthmn/pyterm && cd pyterm && python3 main.py` This will install python 3, and clone the repository to your current working directory.

Currently there aren't any executable files but I am open to contributors creating some (note, these will be tested for the safety of other users)

## Creating commands
To create commands, simply create a file with no extension in `PyMrk/Snippets` and put the desired python code that will be ran inside. The name of the file is the command that will be called.

## Deleting commands
To delete a command, delete the file with the name of the command inside of `PyMrk/Snippets`.
I don't have anything else to say here.

## Creating Man pages
Create a file named after your respective command inside of `PyMrk/Man` and write the information inside. Markdown support is coming soon.

## Deleting Man pages
To delete a command, delete the file with the name of the man page inside of `PyMrk/Man`.
I don't have anything else to say here either.

## State of project
I don't plan on ending this project and currently it has no contributors. Any help would be appreciated. This project is what taught me python and motivated me to start learning other languages. I am planning on adding a web page for my project and making on organisation account if this project grows more.

## Safety: malicious scripts
Always make sure to check your scripts before installing it, I am working on a program to automate this process but that doesn't mean you should ignore the scripts safety.

## Safety: chance of program crashing or freezing
The chance of this is low from scripts as it uses pythons `exec()` function so a script will either crash alone or rarely will crash the entire program.

So far I have never encountered a crash (excluding errors e.g. a incorrect function etc)
but I am using older hardware (>10 years manufacturing date)

## Folders
I am planning on adding folder support in `PyMrk/Snippets` but so far, we have `PyMrk/Man`, `PyMrk/Snippets` and `PyMrk/Data`

`PyMrk/Snippets` is where commands are stored e.g. clear, exit, etc

`PyMrk/Man` contains the manual pages for each command, saying the commands developer of the command or a contributor made a man page for it.

`PyMrk/Data` stores json files with data that needs to be kept across multiple sessions in a json format. E.g autorun, etc
