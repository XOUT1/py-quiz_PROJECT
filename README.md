# GUI Quiz Application using Tkinter and Open Trivia DB



This is an quiz application using tkinter and with the help of trivia DB. The task is to ask multiple-choice questions, collect user answers and finally display the results.

# DATABASE

The Open Trivia Database provides a completely free JSON API for use in programming projects. Use of this API does not require an API Key.

# Libraries and Tools Required

We'll use the following modules and concepts in this project:

• Tkinter is a standard GUI library for Python using which we can build desktop apps. This is the base of our project and we'll use it to create the User Interface of the application.

• Random module implements pseudo-random number generators for various distributions. This module will help us shuffle the options for the questions.

• Requests library allows us to send HTTP/1.1 requests extremely easily. We'll need the library to fetch questions from the Open Trivia DB.

• Python Classes are a blueprint for creating objects. Objects are real-world entities. During the entire project development, we'll be separating our different functionalities into different classes and methods.


[![GitHub release](https://img.shields.io/github/release/akashgiricse/lets-quiz.svg)](https://img.shields.io/bower/vpre/bootstrap.svg)
[![GitHub license](https://img.shields.io/github/license/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/blob/master/LICENSE)

## Current Features


### Features of the quiz:

- All questions are multiple choice question.
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect.


### Administrative features:

- Only admin can add questions.
- Admin can add questions and modify them until they are not marked as _Has been published?_
- Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
- Admin can search questions by question text or choice text.
- Admin can filter questions based on whether the questions have been published or not.

## Getting started with development

Dependencies:

- Python 3.6.x
