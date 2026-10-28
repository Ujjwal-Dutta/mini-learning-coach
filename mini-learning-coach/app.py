import streamlit as st

st.set_page_config(
    page_title="Mini Learning Coach",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Mini Learning Coach")
st.write(
    "Choose a topic and difficulty level, follow your learning plan, "
    "and test your knowledge with a personalized quiz."
)

# --------------------------------------------------
# 1. LEARNING PLANS
# --------------------------------------------------

PLANS = {
    "Python Functions": {
        "Beginner": [
            "Understand why functions are used in Python.",
            "Learn how to define functions using def.",
            "Practice function calls, parameters, and return values."
        ],
        "Intermediate": [
            "Work with positional, keyword, and default arguments.",
            "Understand local variables and function scope.",
            "Write reusable functions and test different inputs."
        ],
        "Advanced": [
            "Understand closures and higher-order functions.",
            "Explore decorators and function composition.",
            "Design reusable functions and reason about edge cases."
        ]
    },
    "Machine Learning": {
        "Beginner": [
            "Understand datasets, features, and labels.",
            "Learn the difference between classification and regression.",
            "Explore training data and test data."
        ],
        "Intermediate": [
            "Learn preprocessing and train-test splitting.",
            "Compare evaluation metrics and baseline models.",
            "Understand overfitting and validation."
        ],
        "Advanced": [
            "Explore cross-validation and hyperparameter tuning.",
            "Identify data leakage and generalization problems.",
            "Design reliable machine learning experiments."
        ]
    },
    "Artificial Intelligence": {
        "Beginner": [
            "Understand what artificial intelligence means.",
            "Explore AI examples such as chatbots and image recognition.",
            "Recognize limitations and risks of AI systems."
        ],
        "Intermediate": [
            "Compare AI, machine learning, and deep learning.",
            "Explore natural language processing and generative AI.",
            "Evaluate AI outputs for accuracy and potential bias."
        ],
        "Advanced": [
            "Analyze robustness, fairness, and model evaluation.",
            "Compare retrieval-based and generative approaches.",
            "Design AI solutions with testing and human oversight."
        ]
    }
}

# --------------------------------------------------
# 2. LEVEL-SPECIFIC QUIZ QUESTIONS
# Each topic and level has its own five questions.
# Correct answers are stored as zero-based indexes.
# --------------------------------------------------

def Q(question, options, answer, explanation):
    return {
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation
    }

QUIZZES = {
    "Python Functions": {
        "Beginner": [
            Q("Which keyword defines a Python function?",
              ["func", "def", "function", "make"],
              1, "Python uses def to define a function."),
            Q("How do you call a function named greet?",
              ["greet", "greet()", "call greet", "def greet"],
              1, "Parentheses are used to call a function."),
            Q("What does return do?",
              ["Repeats code", "Deletes a function",
               "Sends a result back to the caller", "Prints automatically"],
              2, "return sends a value back to the calling code."),
            Q("In def add(a, b):, what are a and b?",
              ["Modules", "Parameters", "Loops", "Classes"],
              1, "a and b are parameters in the function definition."),
            Q("If a function returns x * 2 and x is 4, what is returned?",
              ["2", "4", "6", "8"],
              3, "Four multiplied by two is eight.")
        ],
        "Intermediate": [
            Q("What is the output of def f(x=3): return x; print(f())?",
              ["None", "3", "0", "Error"],
              1, "The default argument is 3, so f() returns 3."),
            Q("What does print(add(b=2, a=5)) do if add returns a+b?",
              ["2", "5", "7", "Error"],
              2, "Keyword arguments match the named parameters; 2+5=7."),
            Q("A variable created inside a function is usually local to what?",
              ["The entire internet", "That function", "Every Python program",
               "The operating system"],
              1, "A local variable is normally available within its function."),
            Q("What does return None mean?",
              ["Return the number zero", "Return no meaningful value",
               "Repeat the function", "Raise every exception"],
              1, "None is Python's special value representing absence of a value."),
            Q("Why can a mutable default argument cause bugs?",
              ["It makes Python run backward",
               "The same object may be reused across calls",
               "It prevents all function calls",
               "It always converts values to strings"],
              1, "A default list, for example, can retain changes between calls.")
        ],
        "Advanced": [
            Q("What does a decorator commonly do?",
              ["Deletes a function", "Wraps a function to extend its behavior",
               "Converts Python into HTML", "Always returns an integer"],
              1, "A decorator wraps or modifies a callable's behavior."),
            Q("What does this return: (lambda x: x + 1)(4)?",
              ["4", "5", "1", "Error"],
              1, "The lambda adds one to four."),
            Q("A closure most commonly allows an inner function to do what?",
              ["Remember variables from its enclosing scope",
               "Access every computer file automatically",
               "Stop all outer functions permanently",
               "Remove all local variables"],
              0, "A closure retains access to relevant enclosing-scope bindings."),
            Q("What is a common purpose of functools.wraps in a decorator?",
              ["Preserve wrapped function metadata",
               "Make every function asynchronous",
               "Delete function arguments",
               "Convert a function to a class"],
              0, "wraps helps preserve metadata such as the name and docstring."),
            Q("A function accepts another function as an argument. It is an example of what?",
              ["Higher-order function", "Integer literal",
               "Syntax comment", "File handle"],
              0, "Higher-order functions accept or return other functions.")
        ]
    },
    "Machine Learning": {
        "Beginner": [
            Q("What is machine learning?",
              ["Learning patterns from data", "Building only web pages",
               "Replacing a keyboard", "Compressing every file"],
              0, "Machine learning uses data to learn patterns."),
            Q("Which is a classification task?",
              ["Predicting a house price", "Predicting tomorrow's temperature",
               "Classifying an email as spam or not spam", "Adding two numbers"],
              2, "Classification predicts categories or labels."),
            Q("What is a feature?",
              ["An input variable", "Always the final answer",
               "A programming error", "The computer's screen"],
              0, "Features are input variables used by a model."),
            Q("Why keep a test dataset?",
              ["To evaluate the model on held-out examples",
               "To make training take longer",
               "To guarantee perfect accuracy", "To delete the labels"],
              0, "Held-out test data helps evaluate performance on unseen examples."),
            Q("Which task is regression?",
              ["Detecting spam", "Predicting a numeric house price",
               "Recognizing a cat category", "Sorting emails into folders"],
              1, "Regression predicts numerical values.")
        ],
        "Intermediate": [
            Q("Why fit a scaler on training data only?",
              ["To avoid leaking test-set information",
               "To increase the number of labels",
               "To guarantee zero error", "To remove the target variable always"],
              0, "Fitting preprocessing on test data can leak information."),
            Q("A model performs well on training data but poorly on test data. This suggests what?",
              ["Overfitting", "Perfect generalization",
               "Underflow only", "Correct data labeling always"],
              0, "The model may have learned training-specific patterns."),
            Q("Which metric is commonly used for classification?",
              ["Accuracy", "Mean squared error only",
               "Image resolution", "File size"],
              0, "Accuracy measures the fraction of predictions that are correct."),
            Q("What is the main purpose of a validation set?",
              ["Tune choices during model development",
               "Replace every training example",
               "Guarantee fairness", "Store the program code"],
              0, "Validation data helps compare models and tune hyperparameters."),
            Q("A dataset has 1% positive cases. Why might accuracy be misleading?",
              ["Predicting only the majority class can still give high accuracy",
               "Accuracy cannot be calculated",
               "The dataset has too many columns",
               "All models become unsupervised"],
              0, "Imbalanced data often requires metrics such as recall, precision, or PR-AUC.")
        ],
        "Advanced": [
            Q("Why use nested cross-validation for model selection and evaluation?",
              ["To separate tuning from performance estimation",
               "To make the dataset completely balanced",
               "To avoid using any training data",
               "To guarantee a perfect model"],
              0, "Nested cross-validation reduces bias from tuning on evaluation folds."),
            Q("What is data leakage?",
              ["Information unavailable at prediction time influences training",
               "A computer loses battery power",
               "A model has too few parameters in every case",
               "A dataset uses CSV format"],
              0, "Leakage lets inappropriate information influence model training or selection."),
            Q("What does regularization generally aim to do?",
              ["Discourage overly complex models",
               "Increase every weight without limit",
               "Remove the need for evaluation",
               "Guarantee all features are useful"],
              0, "Regularization penalizes complexity to help control overfitting."),
            Q("When tuning hyperparameters, which data should guide the final unbiased evaluation?",
              ["A held-out test set not used for tuning",
               "The same training score only",
               "The test set after repeated manual tuning",
               "Any randomly selected label"],
              0, "Reserve test data for final evaluation after model selection."),
            Q("A model has high recall but low precision. What is a likely interpretation?",
              ["It finds many actual positives but also flags many negatives",
               "It misses every positive case",
               "It has no false positives",
               "It predicts only numeric values"],
              0, "High recall with low precision can indicate many false-positive predictions.")
        ]
    },
    "Artificial Intelligence": {
        "Beginner": [
            Q("What is artificial intelligence?",
              ["Technology for tasks associated with human intelligence",
               "A type of monitor", "A keyboard layout", "A file extension"],
              0, "AI systems perform tasks such as language processing or reasoning."),
            Q("Which is an example of natural language processing?",
              ["A chatbot processing a written question",
               "A battery charging", "A screen brightness setting",
               "A computer fan spinning"],
              0, "Natural language processing works with human language."),
            Q("What is generative AI designed to do?",
              ["Generate content such as text or images",
               "Only store files", "Only measure temperature",
               "Always provide verified facts"],
              0, "Generative AI creates new content based on learned patterns."),
            Q("Can AI systems make mistakes?",
              ["No, never", "Yes, outputs can be inaccurate",
               "Only when offline", "Only when used for math"],
              1, "AI can produce inaccurate or misleading outputs."),
            Q("What is one responsible way to use an AI answer?",
              ["Verify important claims", "Assume it is always true",
               "Share private data unnecessarily", "Ignore its limitations"],
              0, "Checking important claims helps catch errors.")
        ],
        "Intermediate": [
            Q("How does deep learning relate to machine learning?",
              ["It is a subfield using multi-layer neural networks",
               "It is unrelated to AI", "It only describes databases",
               "It is a type of computer monitor"],
              0, "Deep learning is a machine learning approach using multi-layer networks."),
            Q("What is a hallucination in a generative AI system?",
              ["A plausible-sounding but incorrect or unsupported output",
               "A guaranteed correct answer", "A hardware upgrade",
               "A file compression method"],
              0, "Hallucinations are outputs that are not grounded in reliable facts."),
            Q("Why evaluate an AI model on representative data?",
              ["To estimate how it may perform in its intended use",
               "To guarantee it never fails", "To avoid defining a task",
               "To make every output identical"],
              0, "Representative evaluation data helps reveal real-world strengths and limitations."),
            Q("What is one common use of embeddings?",
              ["Representing text or items as numerical vectors",
               "Charging a laptop", "Deleting model weights",
               "Changing the screen resolution"],
              0, "Embeddings encode items as vectors useful for similarity and other tasks."),
            Q("What is a potential risk of biased training data?",
              ["The system may produce unfair outcomes",
               "The model must become accurate", "The program cannot run",
               "The system will always be smaller"],
              0, "Patterns in biased data can contribute to biased predictions or outputs.")
        ],
        "Advanced": [
            Q("What is retrieval-augmented generation (RAG)?",
              ["Retrieving relevant information to help ground generated answers",
               "Training a model without any data",
               "A method for deleting prompts",
               "A hardware cooling technique"],
              0, "RAG combines retrieval with generation to provide relevant context."),
            Q("What does robustness testing examine?",
              ["How reliably a system behaves under varied or perturbed inputs",
               "Only the color of the interface", "The number of users' keyboards",
               "Whether a model has a short name"],
              0, "Robustness testing checks behavior under challenging or changing conditions."),
            Q("Why is human oversight important in high-impact AI decisions?",
              ["It enables review, accountability, and handling of difficult cases",
               "It guarantees that AI never errs", "It removes all data needs",
               "It makes evaluation unnecessary"],
              0, "Human oversight supports accountability and review of consequential decisions."),
            Q("What is a key challenge when evaluating generative AI?",
              ["Outputs can vary and quality may need multiple criteria",
               "Every output has only one possible correct wording",
               "It cannot generate text", "It never uses context"],
              0, "Generative outputs can require factuality, relevance, safety, and other checks."),
            Q("Why monitor an AI system after deployment?",
              ["Data and user behavior can change over time",
               "Models can never degrade", "Monitoring removes the need for testing",
               "Deployment guarantees perfect predictions"],
              0, "Monitoring helps detect drift, failures, and changing real-world performance.")
        ]
    }
}

# --------------------------------------------------
# 3. SIDEBAR SETTINGS
# --------------------------------------------------

with st.sidebar:
    st.header("Your learning settings")
    topic = st.selectbox(
        "Choose a topic",
        list(PLANS.keys()),
        key="selected_topic"
    )
    level = st.selectbox(
        "Choose your level",
        ["Beginner", "Intermediate", "Advanced"],
        key="selected_level"
    )
    st.divider()
    st.caption("Choose a level that matches your current knowledge.")

# --------------------------------------------------
# 4. RESET QUIZ WHEN TOPIC OR LEVEL CHANGES
# --------------------------------------------------

selection = (topic, level)

if "last_selection" not in st.session_state:
    st.session_state.last_selection = selection
    st.session_state.quiz_round = 0
    st.session_state.submitted = False
elif st.session_state.last_selection != selection:
    st.session_state.last_selection = selection
    st.session_state.quiz_round += 1
    st.session_state.submitted = False

round_id = st.session_state.quiz_round
questions = QUIZZES[topic][level]

# --------------------------------------------------
# 5. SHOW THE LEVEL-SPECIFIC STUDY PLAN
# --------------------------------------------------

st.subheader(f"📚 Study plan: {topic}")
st.write(f"**Difficulty level:** {level}")

for i, step in enumerate(PLANS[topic][level], start=1):
    st.markdown(f"**Step {i}.** {step}")

if level == "Beginner":
    st.info("Start with the fundamentals. Read each question carefully.")
elif level == "Intermediate":
    st.info("Apply what you know and look for the reasoning behind each answer.")
else:
    st.info("Challenge yourself with deeper concepts and practical decisions.")

st.divider()

# --------------------------------------------------
# 6. SHOW QUIZ
# --------------------------------------------------

st.subheader(f"📝 {level} quiz")
st.write(f"Topic: **{topic}** · 5 questions · 1 point each")

answers = {}

for i, question in enumerate(questions):
    st.markdown(f"**Question {i + 1}.** {question['question']}")

    answers[i] = st.radio(
        f"Answer for question {i + 1}",
        question["options"],
        index=None,
        key=f"answer_{round_id}_{i}",
        label_visibility="collapsed",
        disabled=st.session_state.submitted
    )

if not st.session_state.submitted:
    if st.button("Check my answers", type="primary", use_container_width=True):
        if any(value is None for value in answers.values()):
            st.warning("Please answer all five questions before submitting.")
        else:
            st.session_state.submitted = True
            st.rerun()

# --------------------------------------------------
# 7. SCORE AND EXPLANATIONS
# --------------------------------------------------

if st.session_state.submitted:
    score = sum(
        answers[i] == questions[i]["options"][questions[i]["answer"]]
        for i in range(len(questions))
    )

    st.divider()
    st.subheader("📊 Your results")
    st.metric("Your score", f"{score} / 5")

    if score == 5:
        st.success("Excellent! You answered every question correctly.")
    elif score >= 3:
        st.info("Good work! Review the explanations to strengthen your understanding.")
    else:
        st.warning("Keep practising! Review the explanations and try again.")

    for i, question in enumerate(questions):
        correct_answer = question["options"][question["answer"]]
        is_correct = answers[i] == correct_answer

        if is_correct:
            st.markdown(f"**Question {i + 1}: Correct ✅**")
        else:
            st.markdown(f"**Question {i + 1}: Incorrect ❌**")
            st.write(f"Correct answer: **{correct_answer}**")

        st.caption(question["explanation"])

    if st.button("Try this quiz again", use_container_width=True):
        st.session_state.quiz_round += 1
        st.session_state.submitted = False
        st.rerun()

st.divider()
st.caption("Mini Learning Coach | Learn, practise, and improve.")
