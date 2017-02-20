import pandas as pd

# Read csv file
df = pd.read_csv("../intern/training_data.csv")
# df = pd.read_csv("../intern/evaluation_data.csv")


# Delete months
df['term'] = df['term'].str.extract('([0-9]+)').astype(int)

# Delete %
df['int_rate'] = df['int_rate'].str.extract('([0.0-9]+)').astype(float)
df['revol_util'] = df['revol_util'].str.extract('([0.0-9]+)').astype(float)

# Replace data
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '10+ years', '10')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '< 1 year', '0')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == 'n/a', '0')
df['emp_length'] = df['emp_length'].str.extract('([0-9]+)').astype(int)

# Quantification grade
grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
df['grade'] = df['grade'].map(lambda x: grades.index(x))
for i in range(len(grades)):
    for j in range(5):
        df['sub_grade'] = df['sub_grade'].mask(df['sub_grade'] == (grades[i] + str(j + 1)), (str(i) + '.' + str(j)))
df['sub_grade'] = df['sub_grade'].str.extract('([0.0-9]+)').astype(float)

# if ... del elements
'''
del df['sub_grade']
'''

# Output csv
df.to_csv("output.csv", index=None)