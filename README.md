# Turn-based Role Playing Game Battle (Text-based game)
* A Python script that presents a turn-based, text-based battle system that is inspired by old school Role Playing video games (RPG).

* This program is complete with health counters for the player and boss, different attacks that have different damage outputs/chances to hit or miss, and a colored text interface.

* It presents a fun challenge where the player must do battle with a futuristic robot boss enemy. The game ends when either that player or boss reaches 0 health.

## What does the program do exactly?
1) Sets up the in-game variables, including health, attacks, a turn counter, chances to hit or miss through random number generator, and a switch for the gameplay loop.

2) Introduces the fight, and uses colored text to present the turn number, player health, and boss health in an aesthetically pleasing way.

3) Prompts the player to input one of two different attack options ("laser" or "big blast").

4) Once an attack is selected, the player will have a chance to hit or miss the attack.

5) After the players attempt to attack, the boss will use a randomly selected attack ("punch" or "shock") with a chance to hit or miss.

6) After both parties have attempted to attack, the next turn is display with updated player and boss health counters.

7) Once either party reaches 0 health, the game is over.


## About the program
* This is a basic Python script, and uses only two libraries ("random" and "termcolor").

* Future updates may include other libraries, such as "pygame". Future updates may also include adjusted variables for balance.

