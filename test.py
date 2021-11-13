import streamlit as st
st.title("Math marks clculator")

main_val={
"A":74.5,
"B":64.5,
"C":54.5,
"D":44.5,
"E":84.5,
"O":95,
}

sem1 = st.selectbox(
        "First Semester", ("A", "B","C","D","E","O")
    )
   
sem2 = st.selectbox(
        "Second Semester", ("A", "B","C","D","E","O")
    )

sem3 = st.selectbox(
        "Third Semester", ("A", "B","C","D","E","O")
    )

sem4 = st.selectbox(
        "Fourth Semester", ("A", "B","C","D","E","O")
    )


if st.button("Calculate"):
    total_val=main_val[sem1]+main_val[sem2]+main_val[sem3]+main_val[sem4]
    avg=float(total_val/4)
    st.write("Your total marks is:",avg)
