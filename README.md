# Chat Spammer

# DISCLAIMER
You are 100% responsible for the way you use this program. This program does not have any limit so you could technically break your, or other people's devices by using this to the maximum. This is for educational purposes only.


# What is this about?
This is a program that spams/repeats a certain message through any chat application. This program allows you to set a custom message to send, it allows you to set the delay after each message has been sent (anything below 0.5s might break your pc), it allows you to set a timer for how long you want the spammer to be running and the amount of times you want the program to be sending the message.

# How to run the program?
To run this, make sure you have python 3+ installed and git installed on your PC. If not, here are the links: [(https://git-scm.com/)](https://git-scm.com/downloads), ([https://www.python.org/](https://www.python.org/downloads/)). Go to these links and go through the download process.

First, clone the git repo navigate to the folder by running:
```
git clone https://github.com/oDqnger/chat-spammer.git
cd chat-spammer
```

Then, create a virtual enviornment and activate it so you can install all the dependencies you need (you can also install them globally if you know what you're doing)
```
python -m venv .venv
.venv\Scripts\activate.bat
```

Then install all the dependencies you need for this project
```
pip install -r requirements.txt
```

Then run the main.py file
```
python main.py
```

If you have any issues with installing this, please search it up on google, there will most definately be an answer. If it's a problem with my code or with the steps written here, please create an issue or a pull request. Thanks for using my software :)

# NOTE:
This software does not have any limit, so you can break your PC or get in trouble by doing this. When the program asks you to input the delay after each message has been sent, I highly recommend that you enter a delay above 0.2.
If there are any problems with the code or if you're unable to run the code for whatever reason, you may open an issue for this repo. Or if you know how to fix it, you may as well open a pull request.
