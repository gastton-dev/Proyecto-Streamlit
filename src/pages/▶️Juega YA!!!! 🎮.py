import streamlit as st
import random
from utility import questions


def main():
    # Configuración de la aplicación
    st.set_page_config(
        page_title="Quiz de Meteorología ", page_icon="🌦️", layout="centered"
    )

    # Título de la aplicación
    st.title("Quiz de Meteorología 🌦️")

    st.logo(
        "images\logo_USS_35.png",
        link="https://www.uss.cl/",
        icon_image="images\logo_USS.png",
    )

    st.write(
        "Responde las siguientes preguntas y mide tus conocimientos sobre meteorología."
    )

    # Inicializar el estado de las respuestas si no existe
    if "selected_questions" not in st.session_state:
        st.session_state.selected_questions = random.sample(questions, 5)
        st.session_state.user_answers = [None] * len(
            st.session_state.selected_questions
        )
    correct_answers = 0

    # Imprimir las preguntas seleccionadas
    for i, q in enumerate(st.session_state.selected_questions):
        st.subheader(f"Pregunta {i + 1}: {q['question']}")
        user_answer = st.radio(
            "Selecciona tu respuesta:",
            q["options"],
            key=f"question_{i}",  # Asignar una clave única para cada pregunta
        )

        # Almacenar la respuesta del usuario en el estado
        if user_answer is not None:
            st.session_state.user_answers[i] = user_answer
            if q["options"].index(user_answer) == q["answer"]:
                correct_answers += 1

    # Resultado final
    if st.button("Ver resultados"):
        st.write(
            f"Tu puntaje final es: {correct_answers}/{len(st.session_state.selected_questions)}"
        )
        if correct_answers == len(st.session_state.selected_questions):
            st.balloons()
            st.success("¡Excelente! Eres un experto en meteorología.")
        elif correct_answers >= len(st.session_state.selected_questions) // 2:
            st.info("¡Buen trabajo! Pero puedes mejorar.")
        else:
            st.warning("Sigue practicando, ¡la meteorología es fascinante!")


if __name__ == "__main__":
    main()
