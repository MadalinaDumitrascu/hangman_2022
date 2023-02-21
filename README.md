<a href="https://github.com/MadalinaDumitrascu" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://linkedin.com/in/MadalinaDumitrascu" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>  
  



### The Hangman  
Hangman game
Implement a basic hangman game flow. You can use any (even a constant) word to guess, focus on the guessing logic and the termination of the game.

The game requires the user to guess all the letters belonging to a word.

The initial game state is displayed as _ _ _ _ _ _ _ _ (one underscore for each letter in word).

The game state is displayed as _ o d _ _ o o _ if letters 'd' and 'o' are revealed.

It is possible to make guesses, and letters that occur in the word are revealed.

When a guessed letter does not occur in word, the player loses one life.

When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens.

When a guess is wrong (either a new or a repeated letter), the previous wrong letters are shown to the user.

The player wins when all letters in word are revealed.

The player loses when the number of wrong guesses is higher than the initial value of lives parameter (not counting repeated guesses).

When the player types 'quit' as input, the program says good-bye and terminates.
Case sensitivity
The gameplay is case insensitive, the word display is case sensitive.

Both uppercase and lowercase letters are considered valid input.

Uppercase and lowercase letter guesses reveal the same letters (e.g. both c and C guesses reveal all the cs in the word, regardless of their case).

Letters of different cases behave as if they were the same when checking repetitions (e.g. entering c after a C would count as a repetition).

On the displaying side, however, letters are revealed as they originally appear in word (e.g. successfully guessing c shows C _ _ _ c _ _ _ for Codecool).
Graphics
Add ASCII art to visualize lives left.

The game state display is accompanied by an ASCII art depending on the number of lives left.

The art sequence is adapted to the starting value of the lives parameter (at least between 3 and 7) – this means that the game over art is always the same.

Load words
The game uses a random word from a pre-defined word collection.

The game randomly picks a word at each run.

The game randomly picks a country from countries-and-capitals.txt.
Different levels
The program allows the user to play on different levels.

The game asks the user to pick a difficulty before starting

The word-pool and the number of lives depend on the chosen level.

  
  

<br/>  



## Languages and Tools  
<div align="center">  
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="25" /></a>  
</div>  

<br/>  


## Github Stats  
<table><tr><td valign="top" width="50%">

<img src="https://github-readme-stats.vercel.app/api?username=madalinadumitrascu&show_icons=true&count_private=true&hide_border=true" align="left" style="width: 100%" />

</td><td valign="top" width="50%">

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=madalinadumitrascu&hide_border=true&layout=compact" align="left" style="width: 100%" />

</td></tr></table>  

<br/>  

  

<br/>  

  

<br/>  


<br />

----
<div align="center">Generated using <a href="https://profilinator.rishav.dev/" target="_blank">Github Profilinator</a></div>
