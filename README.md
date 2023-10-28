# GUI Quiz Application using Tkinter and Open Trivia DB

[![GitHub release](https://img.shields.io/github/release/akashgiricse/lets-quiz.svg)](https://img.shields.io/bower/vpre/bootstrap.svg)
[![GitHub license](https://img.shields.io/github/license/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/blob/master/LICENSE)

This is an quiz application using tkinter and with the help of trivia DB. The task is to ask multiple-choice questions, collect user answers and finally display the results.

# DATABASE

The Open Trivia Database provides a completely free JSON API for use in programming projects. Use of this API does not require an API Key.

# Libraries and Tools Required

We'll use the following modules and concepts in this project:

• Tkinter is a standard GUI library for Python using which we can build desktop apps. This is the base of our project and we'll use it to create the User Interface of the application.

• Random module implements pseudo-random number generators for various distributions. This module will help us shuffle the options for the questions.

• Requests library allows us to send HTTP/1.1 requests extremely easily. We'll need the library to fetch questions from the Open Trivia DB.

• Python Classes are a blueprint for creating objects. Objects are real-world entities. During the entire project development, we'll be separating our different functionalities into different classes and methods.

## Workflow of the Project

 1.We'll fetch questions from the Open Trivia DB API.

 2.For each fetched question, we'll create a different object using a Question class. All these Question objects will be appended to a `question_bank` list.

 3.This `question_bank` will be passed to the brain of the application, QuizBrainand a `quiz` object will be created.This class will be responsible for checking if there are more questions, for getting the next question, calculating the score, and so on.

 4.Finally, this `quiz` object will be passed to the QuizInterface class, and the user will be able to interact with it.

## Fetching Questions

As we discussed above, we’ll be using the Open Trivia DB API to get the questions. Head over to [their API](https://opentdb.com/api/_config.php), select the number of questions, category, and difficulty. The question type should be Multiple Choice and the encoding should be Default Encoding. Click on Generate API URL and you’ll get an API URL.

Sample API URL: `<https://opentdb.com/api.php?amount=10&type=multiple>`


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
