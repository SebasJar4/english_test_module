import streamlit as st
import json

from models.question import Question
from models.quiz import Quiz
from models.result import QuestionResult
from services.timer import QuestionTimer
from services.feedback import errors_by_topic
from services.storage import save_attempt


with open("data/questions.json", encoding="utf-8") as f:
    raw_data = json.load(f)

quiz_title = raw_data.get("title", "English Practice")

raw_questions = raw_data["questions"]

questions = [
    Question(
        q_id=q["id"],
        q=q["q"],
        options=q["options"],
        answer=q["a"],
        topic=q["topic"]
    )
    for q in raw_questions
]

st.set_page_config("English B1/B2 Practice", layout="centered")
st.title(f"🇬🇧 {quiz_title}")

if "quiz" not in st.session_state:
    st.session_state.quiz = Quiz(questions)
    st.session_state.current = 0
    st.session_state.timer = QuestionTimer()

quiz = st.session_state.quiz
idx = st.session_state.current

if idx < len(questions):
    q = questions[idx]
    st.subheader(f"Question {idx + 1}/{len(questions)}")

    answer = st.radio(q.q, q.options, key=idx)

    if st.button("Next"):
        time_spent = st.session_state.timer.stop()
        result = QuestionResult(q, answer, time_spent)

        quiz.add_result(result)

        st.session_state.current += 1
        st.session_state.timer = QuestionTimer()
        st.rerun()

else:
    errors = errors_by_topic(quiz.results)

    report = {
        "title": quiz_title,
		"summary": {
		    "title": quiz_title,
		    "total_questions": len(quiz.results),
		    "correct": quiz.score(),
		    "percentage": quiz.percentage(),
		    "total_time_seconds": quiz.total_time()
		},
		"questions": [
		    {
		        "question_id": r.question.id,
		        "question": r.question.q,
		        "topic": r.question.topic,
		        "options": r.question.options,
		        "user_answer": r.user_answer,
		        "correct_answer": r.question.answer,
		        "is_correct": r.is_correct,
		        "time_spent_seconds": r.time_spent
		    }
		    for r in quiz.results
		],
        "weak_topics": errors,
        "quiz": raw_data 
    }

    path = save_attempt(report)

    st.success("Test completed")
    st.metric("Score", f"{quiz.percentage()}%")
    st.write("### 📌 Weak topics")
    st.json(errors)

    st.write("### 🤖 AI / Human readable report")
    st.json(report)

    st.caption(f"Saved at: {path}")

