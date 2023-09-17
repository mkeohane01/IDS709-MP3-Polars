
import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv("https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv")
print(df.head(10))
print(df.describe())

position_counts = df['Position'].value_counts()

fig, ax = plt.subplots()
ax.bar(position_counts['Position'], position_counts['counts']) #error 'DataFrame' object has no attribute 'index'
ax.set_xlabel('Position')
ax.set_ylabel('Count')
ax.set_title('Number of players in each position')
# set the size of the labels on the x-axis to be smaller
ax.tick_params('x', labelsize=6)
fig.savefig('position_counts.png')


fig2, ax2 = plt.subplots()
ax2.scatter(df['Height'], df['Weight'])
ax2.set_xlabel('Height (inches)')
ax2.set_ylabel('Weight (pounds)')
ax2.set_title('Weight as a function of Height')
fig2.savefig('weight_vs_height.png')



