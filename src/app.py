import streamlit as st

st.image("./data/neurona.jpg")
st.title("¡Hola Neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    w0 = st.slider("Peso W")
    x0 = st.number_input("Entrada X")

    if st.button("Calcular la salida",key="btn_0"):
        y = w0 * x0
        st.write(f"La salida de la neurona es de {y}")


with tab2:
    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso W", key="w0_t2")
        x0 = st.number_input("Entrada X", key="x0_t2")

    with col2:
        w1 = st.slider("Peso W", key="w1_t2")
        x1 = st.number_input("Entrada X", key="x1_t2")

    if st.button("Calcular la salida",key="btn_1"):
        y = (x0 * w0) + (x1 * w1)
        st.write(f"La salida de la neurona es de {y}")

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso W", key="w0_t3")
        x0 = st.number_input("Entrada X", key="x0_t3")

    with col2:
        w1 = st.slider("Peso W", key="w1_t3")
        x1 = st.number_input("Entrada X", key="x1_t3")

    with col3:
        w2 = st.slider("Peso W",key="w3_t3")
        x2 = st.number_input("Entrada X",key="x3_t3")

    b = st.number_input("Introduzca el valor del sesgo")

    if st.button("Calcular la salida",key="btn_2"):
        y = (x0 * w0) + (x1 * w1) + (x2 * w2) + b
        st.write(f"La salida de la neurona es de {y}")