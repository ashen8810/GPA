import streamlit as st 
import csv,os

st.title("GPA Calculator")
credit = {"CS104":1,"CS101":3,"ST101":3,"ST103":1,"MT103":2,"MT104":3,"CS100":2,"BL100":2} 
grading_scale = {"A+" : 4, "A" : 4, "A-" : 3.7, "B+" : 3.3, "B" : 3.0, "B-" : 2.7, "C+" : 2.3, "C" : 2.0, "C-" : 1.7, "D" : 1.3, "D-" : 1.0, "E" : 0 }
grades = []
courses = []
for i in credit:
    courses.append(i)
for j in grading_scale:
    grades.append(j)

with st.form("form"):
    c1 = st.selectbox("Course",courses)
    c1g = st.selectbox("Grade",grades)
    submit = st.form_submit_button("Submit")
    if submit == True:

        with open("gpa.csv","a",newline = "") as f:
            writer = csv.writer(f)
            writer.writerow([c1,c1g])
        with open("gpa.csv","r") as f:
                reader = csv.reader(f)
                for row in reader:
                    marks = row[0]+"\t----->"+ row[1]
                    st.markdown(marks)
clear = st.button("Clear")
if clear == True:
    try:
        os.remove("gpa.csv")
        st.success("Done")
    except:
        st.write("Done")

f = st.button("Calculate GPA")         
if f == True:
    try:
        with open("gpa.csv","r") as f:
                reader = csv.reader(f)
                i = 0
                csum = 0
                gpsum = 0
                for row in reader:
                    marks = row[0]+"\t-"+ row[1]

                    gp = float(credit[row[0]])*float(grading_scale[row[1]])
                    
                    csum = csum+float(credit[row[0]])
                    
                    gpsum = gpsum+float(gp)

                
                    st.write(marks)
                    i=i+1
        gpa = "Your GPA is : "+str(gpsum/csum)
        st.header(gpa)
        st.balloons()
        os.remove("gpa.csv")
        
    except FileNotFoundError:    
        
        st.warning("Please Fill the data")
   
    except:
        os.remove("gpa.csv")

