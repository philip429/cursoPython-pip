import matplotlib.pyplot as plt

def Generate_BarChart(name,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def Generate_PieChart(labels, values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig('./imgs/PieChart.png')
    plt.close()