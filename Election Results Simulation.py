import matplotlib.pyplot as plt

def PutValue(val): #puts number of votes
    return int(val * 1.4)
def ShowWinner(powers):
    Max = max(powers)
    p = []
    for i in powers:
        if i == Max:
            p.append(0.1)
        else:
            p.append(0)
    return tuple(p)
Powers = [40,32,28,21,19] # 140
names = ["Right","Left","Green","New","Seniors"]
color = ['r','b','green','m','yellow']
plt.pie(Powers,
        startangle = 90,
        labels = names,
        colors = color,
        autopct = PutValue,
        explode = ShowWinner(Powers))
plt.title("Election Results\n2019")
plt.show()

