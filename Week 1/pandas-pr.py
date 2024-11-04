import pandas as pd
# Creating a simple Series
scores = pd.Series([10, 20, 15, 30])
print(scores)

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 90, 78, 88],
    'Age': [14, 15, 14, 16]
}

data_frame = pd.DataFrame(data)
print(data_frame)

# Sorting by Score
sorted_df = data_frame.sort_values(by='Score', ascending=True)
print(sorted_df)

#  Filling Missing data
new_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, None, 78, 88],
    'Age': [14, 15, None, 16]
}

new_df = pd.DataFrame(new_data)
new_df['Score'] = new_df['Score'].fillna(new_df['Score'].mean())
new_df['Age'] = new_df['Age'].fillna(new_df['Age'].mean())
print(new_df)