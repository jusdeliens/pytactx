# PyTactX
Learn Python by playing with an Ova bot in a virtual Arena ⚔️ 

## ⚙️ Setup

1. Clone this repo
2. pip install all deps in [the requirement list](requirements.txt)
```
pip install paho-mqtt requests python-dotenv pytz pillow
```
3. Add a .env file in the root project directory, containing the following credentials. If you don't have any credentials, feel free [to contact us](https://jusdeliens.com/contact) to join the adventure 🚀
```.env
# The name of your player or your robot ID
ROBOTID         = ...
# The name of the arena to join
ARENA           = ...
# The broker user name provided by a Jusdeliens administrator
USERNAME        = ...
# The broker user password as str
PASSWORD        = ...
# The broker ip address or dns
BROKERADDRESS   = ...
# The border port as int 
BROKERPORT      = ...
# Verbosity level as int from 0:no log, to 4: full debug logs)
VERBOSITY       = ... 
```

4. Then run the main.py with python interpretor (⚠️ at least version 3.9)
```
python main.py
```

## 🤔 How to play ?

Fetch all instructions to program your robot 👉 [on our tutorial here](https://tutos.jusdeliens.com/index.php/2020/01/14/pytactx-prise-en-main/)

To see the public arenas in your web browser 🎮, go to 👉 [IDEAL Viewer online](https://play.jusdeliens.com/)

You can also get yourself a real Ova bot to have much more fun and join the next robot challenge with passionate developers all around the world [by clicking here](https://jusdeliens.com/ova).

## 🧑‍💻 Author
Designed with 💖 by [Jusdeliens Inc.](https://jusdeliens.com)

## ⚖️ License
Under CC BY-NC-ND 3.0 licence 
👉 https://creativecommons.org/licenses/by-nc-nd/3.0/ 

