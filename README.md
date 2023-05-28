# Let's Quiz



This is an quiz application making for python project. YIS

[![GitHub release](https://img.shields.io/github/release/akashgiricse/lets-quiz.svg)](https://img.shields.io/bower/vpre/bootstrap.svg)
[![GitHub issues](https://img.shields.io/github/issues/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/issues)
[![GitHub forks](https://img.shields.io/github/forks/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/network)
[![GitHub stars](https://img.shields.io/github/stars/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/stargazers)
[![GitHub license](https://img.shields.io/github/license/akashgiricse/lets-quiz.svg)](https://github.com/akashgiricse/lets-quiz/blob/master/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Current Features

### Site access features:

- User must be logged in to access the Quiz.
- For signup user is required to give _username_, _first name_, _last name_, _e-mail address_ and _password_.
- For login the user will be required to enter _username_ and _password_ only.

### Features of the quiz:

- All questions are multiple choice question.
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect.

### Leaderboard features:

- Leaderboard is a shorted list according to the score obtained by the users.
- If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.
- Leaderboard is open to all. No login required.

### Administrative features:

- Only admin can add questions.
- Admin can add questions and modify them until they are not marked as _Has been published?_
- Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
- Admin can search questions by question text or choice text.
- Admin can filter questions based on whether the questions have been published or not.

## Getting started with development

Dependencies:

- Python 3.6.x
