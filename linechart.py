import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('householdtask3.csv')
own = df['own']
age = df['age']
fig, ax = plt.subplots()
ax.plot(df, age)
ax.set_title('Line Chart Example')
ax.set_xlabel('own')
ax.set_ylabel('age')
plt.show()