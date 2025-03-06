# Snowman

## Goal

Build a guess-the-word game that builds a snowman.

## One-Time Project Setup

Follow these directions once, at the beginning of your project:


1. Navigate to the folder where you would like to store your projects.

While this can be anywhere on your system, Ada recommends creating a `Developer` folder in your home directory and placing your `projects` folder there. The remaining instructions will assume you are using this setup.

```bash
$ cd ~/Developer/projects
```

1. In Github click on the "Fork" button in github and fork the repository to your Github account.  This will make a copy of the project in your github account. 

2. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `snowman`, and then puts the project into this new folder.  Make sure you are cloning from your copy of the project and not the Ada version (ada-cXX).

```bash
$ git clone ...
```

Do not actually type `...`.  Instead, go to the Github page for your fork of the project and click on the green "Code" button.  Copy the URL that appears in the box.  It should look something like `https://github.com/your_user_name/snowman.git`.  Paste this URL in place of the `...` in the command above.

Use `ls` to confirm there's a new project folder

4. Move your location into this project folder

```bash
$ cd snowman
```

5. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

6. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:
- [x] Fork the project respository
- [x] `cd` into your `projects` folder
- [x] Clone the project onto your machine
- [x] `cd` into the `snowman` folder
- [x] Create the virtual environment `venv`
- [x] Activate the virtual environment `venv`
- [x] Install the dependencies with `pip`

# Running the Project

To run the project, you must be in the virtual environment.  If you are not in the virtual environment, activate it with:

```bash
$ source venv/bin/activate
```

To run the project, use the command:

```bash
$ python main.py
```

You will be prompted to enter "p" to play the game, or "t" to run the tests.

When you start, all of the tests will fail, and playing the game will exit the program immediately. Your goal is to make the tests pass and the game work!

To do this, you will need to complete the implementation of the `snowman` function in the file `game.py`. There are a number of other functions that we developed in the Precourse materials that are also included in that file for you to use.
