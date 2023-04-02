# GPA/CGPA CALCULATOR built with Python and Streamlit
This is based on both the 4.0 and 5.0 system

### Why this difference?
Some schools as we know use the 5-point system and others use the 4-point system

### How are they different?
In the 5-point system, there are six (6) grades; A, B, C, D, E and F.
While in the 4-point system there are only five (5) grades; A, B, C, D and F

### How does this affect our GPA/CGPA calculation?
#### In the 5-point system:
* A is 5 points
* B is 4 points
* C is 3 points
* D is 2 points
* E is 1 point
* F is 0 points

#### In the 4-point system:
* A is 4 points
* B is 3 points
* C is 2 points
* D is 1 points
* F is 0 points

### How is the GPA/ CGPA calulated?
This program makes use of the formula below:

$$ gpa = {\sum(unit \times\ value\text{ of }grade) \over \sum unit} $$

### What GPA range belongs to what class?
#### In the 5-point system:
| GPA Range | Classification  |
|-----------|-----------------|
| 5.0 - 4.5 | First Class     |
| 4.49 - 3.5 | Second Class (Upper)    |
| 3.49 - 2.4 | Second Class (Lower)|
| Less than 2.4 | Others|

#### In the 4-point system:

| GPA Range | Classification  |
|-----------|-----------------|
| 4.0 - 3.5 | First Class     |
| 3.49 - 3.0 | Second Class (Upper)    |
| 3.0 - 2.0 | Second Class (Lower)|
| Less than 2.0 | Others|

This web app takes all of the above into consideration for the calculation and classificaton of the GPA/CGPA 

[Link to web app](https://engineerlambda-gpa-calculator.streamlit.app/)