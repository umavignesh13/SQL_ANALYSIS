import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "/content/performance.csv"
df = pd.read_csv(file_path)

# Convert 'Resigned' column from True/False to 1/0
def convert_resigned(value):
    if str(value).strip().lower() == 'true':
        return 1
    else:
        return 0

df['Resigned_Flag'] = df['Resigned'].map(convert_resigned)

# 1. Barplot - Top 10 Job Titles by Resignation Rate
resignation_rate = df.groupby('Job_Title')['Resigned_Flag'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=resignation_rate.values, y=resignation_rate.index, palette='Reds_r')
plt.title('Top 10 Job Titles by Resignation Rate')
plt.xlabel('Resignation Rate')
plt.ylabel('Job Title')
plt.tight_layout()
plt.show()

# 2. Stacked Bar Chart - Gender Distribution by Department
gender_dept = df.groupby(['Department', 'Gender']).size().unstack().fillna(0)
gender_dept.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
plt.title("Gender Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

# 3. Pie Chart - Age Group Distribution
def get_age_group(age):
    if age < 30:
        return "<30"
    elif 30 <= age <= 45:
        return "30-45"
    else:
        return ">45"

df['Age_Group'] = df['Age'].apply(get_age_group)
age_dist = df['Age_Group'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(age_dist, labels=age_dist.index, autopct='%1.1f%%', startangle=140, colors=['#FFD700', '#87CEFA', '#FFB6C1'])
plt.title("Age Group Distribution")
plt.tight_layout()
plt.show()

# 4. Line Plot - Satisfaction Score vs Performance
avg_satis = df.groupby('Performance_Score')['Employee_Satisfaction_Score'].mean().reset_index()
plt.plot(avg_satis['Performance_Score'], avg_satis['Employee_Satisfaction_Score'], marker='o', color='purple')
plt.title("Satisfaction Score vs Performance")
plt.xlabel("Performance Score")
plt.ylabel("Average Satisfaction")
plt.grid(True)
plt.tight_layout()
plt.show()

# Re-import CSV (not required if already done)
df = pd.read_csv("performance.csv")

#  5. Horizontal Bar Plot - Average Projects Handled by Department
avg_proj = df.groupby('Department')['Projects_Handled'].mean().sort_values()
avg_proj.plot(kind='barh', figsize=(10, 6), color='orange')
plt.title("Average Projects Handled by Department")
plt.xlabel("Projects")
plt.ylabel("Department")
plt.tight_layout()
plt.show()

# 6. Horizontal Bar Plot - Average Overtime Hours by Department
avg_ot = df.groupby('Department')['Overtime_Hours'].mean().sort_values()
avg_ot.plot(kind='barh', figsize=(10, 6), color='red')
plt.title("Average Overtime Hours by Department")
plt.xlabel("Overtime Hours")
plt.ylabel("Department")
plt.tight_layout()
plt.show()

# 7. Box Plot - Work Hours per Week by Job Title
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Work_Hours_Per_Week', y='Job_Title', orient='h', palette='coolwarm')
plt.title("Work Hours per Week by Job Title")
plt.xlabel("Hours/Week")
plt.ylabel("Job Title")
plt.tight_layout()
plt.show()

# 8. Bar Plot - Average Monthly Salary by Department
avg_salary = df.groupby('Department')['Monthly_Salary'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
avg_salary.plot(kind='bar', color='skyblue')
plt.title("Average Monthly Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Bar Plot - Resignation Rate by Department
df['Resigned_Flag'] = df['Resigned'].map(convert_resigned)
resign_rate_dept = df.groupby('Department')['Resigned_Flag'].mean().sort_values(ascending=False)
resign_rate_dept.plot(kind='bar', figsize=(10, 6), color='crimson')
plt.title("Resignation Rate by Department")
plt.ylabel("Resignation Rate")
plt.xlabel("Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. Bar Plot - Average Team Size by Department
avg_team = df.groupby('Department')['Team_Size'].mean().sort_values(ascending=False)
avg_team.plot(kind='bar', figsize=(10, 6), color='darkgreen')
plt.title("Average Team Size by Department")
plt.ylabel("Team Size")
plt.xlabel("Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
