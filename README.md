# Mini Learning Coach

## 🌐 Live Demo

**Website URL:** [Mini Learning Coach — Live Demo](https://mini-learning-coach-abtobt9gnfgw3szmhuhshx.streamlit.app/)

## 📖 Project Overview

Mini Learning Coach is an interactive learning application built with Python and Streamlit. It helps learners explore topics, follow a study plan based on their selected difficulty level, practise multiple-choice questions, and review their results.

This project was developed as a prototype for an **AI Native Mentor internship build sprint**, with a focus on interactive learning, structured practice, and feedback.

## ✨ Features

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
- Study plans tailored to the selected topic and difficulty level

## 🛠️ Technology Stack

- **Python** — Application logic
- **Streamlit** — Interactive web interface
- **Google Colab** — Development environment

## ⏱️ Six-Hour Development Timeline

The project follows a six-hour build-sprint structure, progressing from application planning and content design to quiz functionality, testing, and deployment.

| Time | Development Phase | Activities |
|---|---|---|
| Hour 1 | Project Setup and Planning | Set up the Python and Streamlit project, establish the application structure, and define the main learning workflow. |
| Hour 2 | Learning Content Design | Organise the three learning topics and prepare study plans for Beginner, Intermediate, and Advanced levels. |
| Hour 3 | Quiz Development | Implement topic-specific and difficulty-specific multiple-choice questions, answer options, and correct-answer definitions. |
| Hour 4 | Scoring and Feedback | Add answer submission, automatic score calculation, explanations, feedback, and quiz retry functionality. |
| Hour 5 | Interface Integration and Testing | Connect the topic selector, difficulty selector, study plans, and quiz interface; review the main learner workflow. |
| Hour 6 | Final Review and Deployment | Review the application behaviour, refine the user experience, and prepare or verify the deployed Streamlit application. |

### Sprint Deliverables

- An interactive learning application accessible through a web browser.
- Three learning topics and three difficulty levels.
- Structured study plans for selected topics and levels.
- Five-question multiple-choice quizzes.
- Automatic scoring and answer explanations.
- A quiz retry option for additional practice.
- A deployed live demonstration.

*The timeline is a suggested six-hour sprint breakdown based on the application's features. Adjust the activities to reflect the work actually completed during your sprint.*

## 🔄 How It Works

1. Select a learning topic.
2. Choose a difficulty level.
3. Review the suggested study plan.
4. Answer the quiz questions.
5. Submit your answers to view your score and explanations.
6. Retry the quiz to practise again.

## 🤖 AI Transparency

The current prototype uses predefined study plans, quiz questions, correct answers, and explanations. It does not generate new questions through a live AI model or call a paid AI API.

AI assistance may be used during development. The project should be presented transparently, distinguishing development assistance from AI capabilities implemented in the application itself.

## 🚀 Run Locally

### 1. Install Python

Install a compatible Python version on your computer.

### 2. Clone or download the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the placeholders with your actual GitHub username and repository name.

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open at the local URL displayed in the terminal.

## ⚠️ Project Limitations

- Learning content and quiz questions are predefined.
- Learner progress is not permanently stored.
- Personalised AI-generated tutoring is not currently implemented.
- The quality of feedback depends on the predefined explanations and questions.

## 🔮 Future Improvements

- Add more learning topics and questions.
- Save learner progress across sessions.
- Integrate an AI model for personalised explanations and learning recommendations.
- Generate adaptive quizzes based on learner performance.
- Add progress tracking and topic-wise performance summaries.

## 🎓 Internship Sprint Demonstration

The project demonstration should cover:

1. **Live application walkthrough:** Demonstrate topic selection, difficulty selection, the study plan, quiz submission, scoring, explanations, and retry functionality.
2. **Design decision:** Explain one important design decision, such as using predefined content to make the prototype reliable and functional within the sprint duration.
3. **AI mistake and correction:** Describe one AI-related mistake that actually occurred during development, explain how it was identified, and show how it was corrected. Do not invent a mistake or claim a correction that did not happen.

## 📌 Disclaimer

Mini Learning Coach is an educational prototype intended to support structured practice and self-directed learning. Its content and feedback are limited to the features implemented in the current version.

---

**Live Demo:** [https://mini-learning-coach-abtobt9gnfgw3szmhuhshx.streamlit.app/](https://mini-learning-coach-abtobt9gnfgw3szmhuhshx.streamlit.app/)
