import matplotlib.pyplot as plt
import csv

#csv file contains : hour , test result, name of student
#we use csv and not numpy because we can't get the name with numpy
x =[]
y =[]
names =[]
with open('ExampleForGraph.csv','r') as csv_file:
    plots = csv.reader(csv_file,delimiter = ',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        names.append(row[2])
    print(plots)
print(names)
plt.scatter(x,y)
plt.title('Effect of Study Time on Test Scores')
plt.xlabel('Hours')
plt.ylabel('Score')
plt.show()
