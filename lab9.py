#7.	WAP to plot line graph using following instructions:
#a.	Define two lists: one for the days of the week (e.g., Monday, Tuesday, etc.) and another for the corresponding temperature data for each day.
#b.	Use Matplotlib to create a line graph where the x-axis represents the days of the week and the y-axis represents the temperature.
#c.	Customize the appearance of the line graph by adding labels to the x-axis and y-axis, adding a title, and adjusting the color and style of the line.

import matplotlib.pyplot as plt
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 21, 23, 25, 26, 27]
plt.plot(days_of_week, temperatures, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Weekly Temperature Data')
plt.grid(True)
plt.show()

#8.	WAP to plot scatter graph using following instructions:
#a.	Define two lists: one for the hours studied by each student and another for the corresponding exam scores.
#b.	Use Matplotlib to create a scatter graph where the x-axis represents the hours studied and the y-axis represents the exam scores.
#c.	Customize the appearance of the scatter graph by adding labels to the x-axis and y-axis, adding a title, and adjusting the marker style 
# and color.
hours_studied = [1, 2, 3, 7, 5, 6, 10]
exam_scores = [50, 55, 60, 45, 70, 75, 90]
plt.scatter(hours_studied, exam_scores, color='r', marker='x', s=100)
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Scatter Plot of Hours Studied vs Exam Scores')
plt.grid(True)
plt.show()

#9.	WAP to plot pie-chart using following instructions:
#a.	Define a dictionary where each key represents a grade (e.g., 'A', 'B', 'C', etc.) and the corresponding value represents the number of students who received that grade.
#b.	Use Matplotlib to create a pie chart where each slice represents a grade and its size represents the proportion of students who received that grade.
#c.	Customize the appearance of the pie chart by adding labels to the slices, adding a title, and adjusting the colors.

grades = {'A': 30, 'B': 25, 'C': 20, 'D': 15, 'F': 10}
labels = grades.keys()
sizes = grades.values()
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']
explode = (0.1, 0, 0, 0, 0)  # explode the first slice (A)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Grades')
plt.show()

#10.WAP to plot bar-chart using following instructions:
#a.	Define a dictionary where each key represents a product name and the corresponding value represents the sales amount for that product.
#b.	Use Matplotlib to create a bar chart where each bar represents a product and its height represents the sales amount.
#c.	Customize the appearance of the bar chart by adding labels to the x-axis and y-axis, adding a title, and adjusting the colors of the bars.
products = {'Product A': 150, 'Product B': 200, 'Product C': 300, 'Product D': 250}
labels = products.keys()
sales = products.values()
colors = ['blue', 'orange', 'green', 'red']

plt.bar(labels, sales, color=colors)
plt.xlabel('Products')
plt.ylabel('Sales Amount')

plt.title('Sales Amount by Product')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()

#11.WAP to plot subplot using following instructions:
#a.	Use this sample data: 
#b.	Use Matplotlib to create subplots with multiple plots arranged in a grid.
#c.	Customize the appearance of each subplot by adding labels, titles, and adjusting the colors and styles of the plots.
x = list(range(11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [0, 0.841, 0.909, 0.141, -0.757, -0.959, -0.279, 0.657, 0.989, 0.412, -0.544]  # Sample sine values
y2 = [1, 0.540, -0.416, -0.990, -0.654, 0.284, 0.960, 0.753, -0.145, -0.911, -0.839]  # Sample cosine values
y3 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Sample squared values
y4 = [1, 2.72, 7.39, 20.09, 54.6, 148.41, 403.43, 1096.63, 2980.96, 8103.08, 22026.47]  # Sample exponential values

fig,axs=plt.subplots(2,2)

axs[0,0].plot(x,y1)
axs[0,1].plot(x,y2)
axs[1,0].plot(x,y3)
axs[1,1].plot(x,y4)


