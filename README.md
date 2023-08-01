# EA Graphics Manager
Program for parsing FSH, SSH, XSH, PSH, GSH and MSH files from EA games.

Technologies used: Python 3.11, tkinter

This program **<ins>is not finished yet</ins>**.
It may not support all image types.

<img src="src\data\img\usage_v0.14.1.gif">

More info about EA Image file format can be found on [Xentax Wiki](http://wiki.xentax.com/index.php/EA_SSH_FSH_Image).


# Dependencies

* **[ReverseBox](https://github.com/bartlomiejduda/ReverseBox)**


# Building on Windows

1. Install  **[Python 3.11.0](https://www.python.org/downloads/release/python-3110/)**
2. Install **[PyCharm 2023 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)**
3. Create virtualenv and activate it
   - python3 -m venv \path\to\new\virtual\environment
   - .\venv\Scripts\activate.bat
4. Install all libraries from requirements.txt
   - pip3 install -r requirements.txt
5. Run the src\main.py file

# Building on Linux/MacOS

// TODO

# Image formats support table

| Image format                | Preview support     | Export support     | Import support     |
|-----------------------------|---------------------|--------------------|--------------------|
| <center>1 / 0x01</center>   | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>2 / 0x02</center>   | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>3 / 0x03</center>   | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>4 / 0x04</center>   | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>5 / 0x04</center>   | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>65 / 0x41</center>  | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>66 / 0x42</center>  | <center>✔️</center> | <center>❌</center> | <center>❌</center> |
| <center>125 / 0x7D</center> | <center>✔️</center> | <center>❌</center> | <center>❌</center> |

# EA-Graph-Man Noesis Script

In the src\scripts directory there is an script
which can be used for viewing EA graphics in Noesis.
To use script with Noesis, please follow below steps:

1. Go to \src\scripts\ directory
2. Copy script to \noesis\plugins\python\ directory
3. Open any EA Image in Noesis

# Badges
![GitHub](https://img.shields.io/github/license/bartlomiejduda/EA-Graphics-Manager?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/bartlomiejduda/EA-Graphics-Manager?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/bartlomiejduda/EA-Graphics-Manager/total)
![GitHub last commit](https://img.shields.io/github/last-commit/bartlomiejduda/EA-Graphics-Manager?style=plastic)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/bartlomiejduda/EA-Graphics-Manager?style=plastic)
