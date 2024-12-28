import matplotlib.pyplot as plt

def hipótesis_1(data)
depressed_students = df[df['Depression'] == 1]
gender_counts = depressed_students['Gender'].value_counts()
total_gender_counts = df['Gender'].value_counts()
gender_percentages = (gender_counts / total_gender_counts) * 100
ax = gender_percentages.plot(kind='bar', color=['blue', 'pink'], alpha=0.7)
plt.title('Porcentaje de Estudiantes Deprimidos por Género')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Género')
plt.xticks(rotation=0)
for i, percentage in enumerate(gender_percentages):
    plt.text(i, percentage + 0.5, f'{percentage:.2f}%', ha='center', fontsize=10)
plt.show()