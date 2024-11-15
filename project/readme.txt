JavaScript Keylogger
Created by Osareme Davis and Mika Shiffman

Project Deliverables:
- Demo vulnerable website
- JavaScript Keylogger Program
- Documentation on testing environment
- Keylogger Attack Writeup

Instructions for Replicating:

Website setup:
On one machine, run the server2.py file with your ip address and the port number 8000

Attacker server setup:
Be in the directory with all the attacker files.
On another machine, run the php server with the command php -S IP:port

Orchestrate the Attack:
Attacker:
On the attacker server, go to the website (http://ip:port).
Paste the JavaScript code into discussion box. Hit enter.

Victim:
On a browser, go to the webite (http://ip:port).
Enter username and password as normal. Hit enter.

Attacker:
Open up test.txt. 
Check that the victim's username and password have been sent using a PHP request and put into the file.

To run the secure version of the website, swap index.html with secure.html in server2.py
