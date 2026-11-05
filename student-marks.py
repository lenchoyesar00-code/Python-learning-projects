import pandas as pd

students = {
    "Name": ["Ali", "Sara", "Abdi", "Hana", "Omar", "Lensa"],
    "Mark": [85, 98, 70, 95, 60, 88]
}

df = pd.DataFrame(students)

average = df["Mark"].mean()

top_student = df.loc[df["Mark"].idxmax()]

print("Student Marks:")
print(df)

print("Average:", average)

print("Top Student:")
print(top_student)

df.to_csv("student_marks.csv", index=False)

print("File saved successfully!")
