**Question:**

Write a Python program that processes a CSV file containing information about students and their marks in different subjects. The program should calculate the following:

1. The average mark for each student across all subjects.
2. The average mark for each subject across all students.
3. Identify the student with the highest average mark and the subject with the highest average mark.
4. Save the results in a new CSV file with the following columns: `Student Name`, `Average Mark`, `Highest Mark Student`, `Subject Name`, `Subject Average Mark`, `Highest Mark Subject`.

Use the following sample data to test your program:

```csv
Student Name,Mathematics,Science,English
Alice,85,78,92
Bob,89,94,85
Charlie,78,85,88
David,92,91,85
Eva,76,83,91
```

**Detailed Requirements:**

1. **Average Mark for Each Student:**
    - Calculate the average mark for each student and add it to the new CSV file under `Average Mark`.

2. **Average Mark for Each Subject:**
    - Calculate the average mark for each subject and add it to the new CSV file under `Subject Average Mark`.

3. **Highest Average Mark Student:**
    - Identify the student with the highest average mark and add their name to the new CSV file under `Highest Mark Student`.

4. **Highest Average Mark Subject:**
    - Identify the subject with the highest average mark and add it to the new CSV file under `Highest Mark Subject`.

**Marks Distribution:**
- Correct calculation of average marks for each student (10 marks)
- Correct calculation of average marks for each subject (10 marks)
- Correct identification of the student with the highest average mark (10 marks)
- Correct identification of the subject with the highest average mark (10 marks)
- Proper formatting and saving of results in a new CSV file (10 marks)

**Sample Output:**

For the given data, the output CSV should look like this:

```csv
Student Name,Average Mark,Highest Mark Student,Subject Name,Subject Average Mark,Highest Mark Subject
Alice,85.0,Alice,Mathematics,84.0,Science
Bob,89.33,Alice,Science,86.2,Science
Charlie,83.67,Alice,English,88.2,Science
David,89.33,Alice,,,
Eva,83.33,Alice,,,
```

**Note:** The columns `Subject Name`, `Subject Average Mark`, and `Highest Mark Subject` only need to be filled for the first row.