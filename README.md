# Mini Learning Coach
🌐 Live Demo

Website URL: https://mini-learning-coach-abtobt9gnfgw3szmhuhshx.streamlit.app/

## Project Overview

Mini Learning Coach is an interactive learning application built with Python and Streamlit. It helps learners explore topics, follow a study plan based on their selected difficulty level, practise multiple-choice questions, and review their results.

This project was developed as a prototype for an AI Native Mentor internship build sprint.

## Features

- Three learning topics:
  - Python Functions
  - Machine Learning
  - Artificial Intelligence
- Three difficulty levels: Beginner, Intermediate, and Advanced
- Topic-specific and difficulty-specific quiz questions
- Five multiple-choice questions per quiz
- Automatic score calculation
- Answer explanations and feedback
- Option to retry a quiz
- Study plans tailored to the selected topic and level

## Technology Stack

- Python
- Streamlit
- Google Colab for development

## How It Works

1. Select a learning topic.
2. Choose a difficulty level.
3. Review the suggested study plan.
4. Answer the quiz questions.
5. Submit your answers to view your score and explanations.
6. Retry the quiz to practise again.

## AI Transparency

The current prototype uses predefined study plans, quiz questions, correct answers, and explanations. It does not generate new questions through a live AI model or call a paid AI API.

AI assistance may be used during development, and the project should be presented honestly with its current capabilities and limitations.

## Run Locally

1. Install Python.
2. Download or clone this repository.
3. Install the dependencies:

   pip install -r requirements.txt

4. Run the application:

   streamlit run app.py

## Project Limitations

- Learning content and quiz questions are predefined.
- Learner progress is not permanently stored.
- Personalised AI-generated tutoring is not currently implemented.

## Future Improvements

- Add more learning topics and questions.
- Save learner progress.
- Integrate an AI model for personalised explanations and learning recommendations.

## Internship Sprint Demonstration

The project demonstration should show the running application, explain one important design decision, and describe one AI mistake encountered during development and how it was corrected. Only describe mistakes and fixes that actually occurred.
