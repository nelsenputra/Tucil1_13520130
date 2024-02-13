# Tucil Stima 1 by Nelsen Putra
> Cyberpunk 2077 breach protocol solver written in Python. Based on the concept of Brute Force algorithm.


## Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Library](#library)
* [Contact](#contact)


## Introduction
Hello, everyone! Welcome to my GitHub Repository!

This project was created by:
| Name | Student ID | Class |
| :---: | :---: | :---: |
| Nelsen Putra | 13520130 | IF2211-02


## General Information
Cyberpunk 2077 Breach Protocol is a hacking minigame in the Cyberpunk 2077 video game. This minigame is a simulation of hacking a local network from ICE (Intrusion Countermeasures Electronics) in Cyberpunk 2077. Components in this game include:
1. Token – consists of two alphanumeric characters such as E9, BD, and 55.
2. Matrix – consists of tokens that will be selected to arrange the code sequence.
3. Sequence – a sequence of tokens (two or more) that must be matched.
4. Buffer – the maximum number of tokens that can be arranged sequentially.

The program is a solution to the breach protocol game where it is supposed to be an optimum solver for each combination of matrix, sequence, and buffer size. This program was written in Python language, implementing the Brute Force algorithm. It accepts input in the form of a `.txt` file containing the information of buffer size, followed by matrix width and height, the matrix itself, number of sequences, and the whole sequences and its reward. As an alternative form, it can also generate a random input for the program. After reading the input, the program will begin to find the best solution using the method applied by the writer of this program. At the end of the program, user can save the final solution into a .txt file.


## Technologies Used
The whole program was written in Python.


## Features
- [x] Can be compiled successfully
- [x] Can be run and executed well
- [x] Receive an external file as an input
- [x] Generate random input
- [x] Solve the breach protocol and generate an optimal output
- [x] Save the solution into a .txt file
- [ ] Graphical User Interface


## Setup
### Installation
- Download and install [python](https://www.python.org/downloads/)
- Install the whole modules and [libraries](#library) used in the source code
- Download the whole folders and files in this repository or do clone the repository

### Execution
1. Clone this repository in your own local directory

    `git clone https://github.com/nelsenputra/Tucil1-13520130.git`

2. Open the command line and change the directory to 'src' folder

    `cd Tucil1-13520130/src`
    
3. Run `python3 main.py` on the command line or use the code runner extension

### Requirement
A `.txt` file used as an input should follow the pattern:
```
buffer_size
matrix_width matrix_height
matrix
number_of_sequences
sequences_1
sequences_1_reward
sequences_2
sequences_2_reward
...
sequences_n sequences_n_reward
```
or you can directly use randomizer for an automatic input.


## Project Status
Project is: _complete_

All the specifications were implemented.


## Room for Improvement
- A faster or more efficient algorithm to make the program run quicker
- A better interface development to improve user satisfaction


## Acknowledgements
- This project was based on [Spesifikasi Tugas Kecil 1 IF2211 Strategi Algoritma](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2023-2024/Tucil1-2024.pdf)
- Thanks to God
- Thanks to Mrs. Masayu Leylia Khodra, Mrs. Nur Ulfa Maulidevi, and Mr. Rinaldi as our lecturers
- Thanks to academic assistants
- This project was created to fulfill our Small Project for IF2211 Algorithm Strategies


## Library
- [time](https://www.tutorialspoint.com/c_standard_library/time_h.htm)
- [os](https://docs.python.org/3/library/os.html)
- [pyfiglet](https://pypi.org/project/pyfiglet/)
- [colorama](https://pypi.org/project/colorama/)
- [random](https://www.w3schools.com/python/module_random.asp)


## Contact
Created by Nelsen Putra. 2024 All Rights Reserved.
