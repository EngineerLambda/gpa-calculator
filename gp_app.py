import streamlit as st
import time


with st.container():
    st.write("""
    ### GPA/CGPA CALCULATOR
    ### This is a GPA calculator based on both 4.0 and 5.0 system
    """)


with st.expander("How to use?"):
    st.write("""
    1. Check the side bar on the left to select your GPA system, it is set to 5.0 system by default
    2. Fill in the number of courses you want to use in the calculation of your GPA, in the provided field
    3. select the unit and grade in the approproiate selection box provided
    4. Don't worry if you are not sure yet, you can always add a new field by clicking on the plus sign on the input field
    5. If you make any mistake while selecting either the unit or the grade, you can edit it 
       without losing the information previously provided for other courses, 
       makes it easy for you to do try and error with expected grades even before your results are out
    """)
    


with st.sidebar:
    system = st.radio("What is your preferred GPA system? ", options=["5.0", "4.0"])

if system == "5.0":
    grade_dict = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
    grades_array = ["A", "B", "C", "D", "E", "F"]
else:
    grade_dict = {"A":4, "B":3, "C":2, "D":1, "F":0}
    grades_array = ["A", "B", "C", "D", "F"]
n_courses = st.number_input("Enter the number of courses you offered", step=1, min_value=1, format="%i")


def positions(num):
    num_str = str(num)
    if len(num_str) >= 2 and num_str[-2] == "1":
        return str(num) + "th"
    else: 
        if num_str[-1] == "1":
            num_str += "st"
        elif num_str[-1] == "2":
            num_str += "nd"
        elif num_str[-1] == "3":
            num_str += "rd"
        else:
            num_str += "th"
        return num_str 
        


total_points = 0
total_unit = 0
for i in range(1, 1+int(n_courses)):
    col1, col2 = st.columns(spec=2, gap="medium")
    with col1:
        unit = st.selectbox(f"Select the unit of the {positions(i)} course", range(1,7))
    with col2:
        grades = st.selectbox("Select your grade", grades_array, key=i)
        grade_val = grade_dict[grades]
    point = unit*grade_val
    total_points += point
    total_unit += unit

    

def get_class_5(val):
    if 4.5 <= val <= 5.0:
        st.balloons()
        return st.success("FIRST CLASS, KEEP IT UP", icon="🚀")
    elif 3.5 <= val <= 4.5:
        return st.success("SECOND CLASS (UPPER), KEEP IT UP", icon="🔥")
    elif 2.4 <= val <= 3.5:
        return st.warning("SECOND CLASS (LOWER), YOU CAN DO MORE",icon="💪")
    else:
        return st.error("KEEP ON GROWING, YOU WILL GET THERE SOON",icon="💪")
    

def get_class_4(val):
    if 3.5 <= val <= 4.0:
        st.balloons()
        return st.success("FIRST CLASS, KEEP IT UP", icon="🚀")
    elif 3.0 <= val <= 3.5:
        return st.success("SECOND CLASS (UPPER), KEEP IT UP", icon="🔥")
    elif 2.0 <= val <= 3.0:
        return st.warning("SECOND CLASS (LOWER), YOU CAN DO MORE",icon="💪")
    else:
        return st.error("KEEP ON GROWING, YOU WILL GET THERE SOON",icon="💪")


if st.button("CALCULATE"):
    with st.spinner("Crunching numbers ..."):
        time.sleep(2)
        gp = total_points/total_unit
        st.write(f"Your GPA is {gp:.2f}")
        if system == "5.0":
            get_class_5(gp)
        else:
            get_class_4(gp)



