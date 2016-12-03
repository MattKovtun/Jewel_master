# Jewel Monster

Jewel Bot has been created!
Bot which opens link in web broweser (http://www.miniclip.com/games/bejeweled/en/)
with the Bejeweled game and plays it. 

## Getting Started

Download all files from repository and unzip to some folder.

```
cd .../jewel-monster/main
python3 monster_test.py
```

### Prerequisites

There is 'setup.py' in repository, but still.

1. Numpy
2. Sklearn
3. Selenium

Beside those you also need:

1.Opencv
2.Firefox version <= 46

## Running the bot

Go to directory with the bot and then to main 

```
cd .../jewel-monster/main
```

*where ... stands for directories on your PC

Run the bot 

```
python3 monster_test.py
```

### Break down into end to end tests

Firefox broweser will be opened with link (http://www.miniclip.com/games/bejeweled/en/).
After the page is loaded you will see debug massage saying 'The page has been loaded.'
While server of the miniclip is loading the game you will see debug message 'The game is loading, please wait...'
When game is loaded debug message will say 'Loading is completed!'
Then bot will choose the game mode and start new game, debug message will say 'click'
After that greedy algorithm will play the game, and it will print whole matrix of diamonds he recognised.
where first letter is color of the diamond for example 'w_' mean white, 'b_' means blue, and sometimes he will recognise special 
effects like 'gs' - means shining green gem, and will be treated like regular white, of 'gf' - flamming green gem.

```
o_ o_ y_ p_ p_ b_ g_ p_
b_ y_ r_ p_ r_ p_ o_ r_
b_ b_ w_ g_ g_ o_ w_ g_
r_ o_ p_ w_ p_ r_ g_ y_
p_ b_ y_ r_ gf w_ y_ w_
r_ y_ p_ w_ r_ b_ r_ y_
g_ b_ g_ p_ o_ r_ y_ p_
o_ o_ g_ w_ r_ y_ p_ o_

```

## Authors

* **Matt Kovtun** - *Initial work* - [MattKovtun](https://github.com/MattKovtun)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.



