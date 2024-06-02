**Question:**

In Sri Lanka, the National Identity Card (NIC) number contains useful information about the individual's date of birth (DOB) and gender. The old NIC format consists of nine digits followed by a letter (e.g., 123456789V), while the new format consists of twelve digits (e.g., 200012345678). Write a Python program that extracts the DOB, gender, and any other useful information from a given NIC number. 

Your program should include the following features:

1. A function to extract and return the date of birth in the format `YYYY-MM-DD`.
2. A function to determine and return the gender based on the NIC number.
3. Handle both old and new NIC formats.
4. Include error handling for invalid NIC numbers.

Use the following NIC numbers to test your program:
- Old Format: `861234567V`
- New Format: `200012345678`

**Detailed Requirements:**

1. **Date of Birth Extraction:**
    - For the old NIC format, the first two digits represent the year of birth.
    - For the new NIC format, the first four digits represent the year of birth.
    - The next three digits represent the day of the year the person was born (001-366). If the value is greater than 500, subtract 500 to determine the actual day and use this to infer the gender.

2. **Gender Determination:**
    - If the day value is greater than 500, the person is female; otherwise, the person is male.

3. **Example:**
    - For `861234567V`, the year is 1986, and the day value is 123. The person is male, and the DOB is 1986-05-03.
    - For `200012345678`, the year is 2000, and the day value is 123. The person is male, and the DOB is 2000-05-02.

Write a Python program that fulfills the above requirements and demonstrates its functionality using the provided NIC numbers.

**Sample Output:**

For NIC `861234567V`:
- Date of Birth: `1986-05-03`
- Gender: `Male`

For NIC `200012345678`:
- Date of Birth: `2000-05-02`
- Gender: `Male`

**Marks Distribution:**
- Correct extraction of the date of birth (10 marks)
- Correct determination of gender (10 marks)
- Handling both NIC formats correctly (10 marks)
- Appropriate error handling (10 marks)