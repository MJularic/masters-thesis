# Code of my master thesis from Faculty of Electrical Engineering and Computing in Zagreb

## Thesis title: Generation and classification of passwords using Markov models

Passwords are nowadays the main way to restrict access to online content.
When choosing a password, computer users rarely think about the level of security
they provide. Commercial password classification tools will often force the user
to create a password that is hard to remember or in most cases a weak password.
Such tools do classification based on the idea that an attacker will perform a brute
force attack, although there are much more sophisticated methods for cracking
passwords. The goal of this paper is to create a solution that will allow the user
to create a secure and easy to remember password. A classification system will be
proposed to determine the likelihood of an attacker guessing a password if using
a statistical attack based on Markov models.


The original paper of the master's thesis is included in the folder **/paper**. It is important to note that it is written in Croatian.

To install the needed dependencies run the provided install.sh script from the terminal.

You will need **sudo** privileges to run the installation.

```./install.sh ```


After installing the necessary dependecies. One must run the **main.py** python file. 

**Note that this has been tested on Ubuntu 18.04 and was written for python3**

The GUI is just a prototype for testing out the functionalities.


