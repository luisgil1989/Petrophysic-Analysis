import lasio
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


las = lasio.read("Data/1044222726.las")
df = las.df()
df.reset_index(inplace=True)
df.rename(columns={'DEPT': 'DEPTH'}, inplace=True)

# Setup figure and plot
plt.figure(figsize=(5, 8))
plt.plot(df['GR'], df['DEPTH'], c='black', lw=0.5)

# Using the where argument to fill to a fixed value
plt.fill_betweenx(df['DEPTH'], 50, df['GR'], where=df['GR']<=50, facecolor='yellow')
plt.fill_betweenx(df['DEPTH'], df['GR'], 50, where=df['GR']>=50, facecolor='gray')

# Setup axes limits
plt.xlim(0, 150)

# Invert Y-axis
plt.gca().invert_yaxis()

# Move X-axis to the top
plt.gca().xaxis.tick_top()

# Create legend handles and labels for yellow and gray fills
yellow_patch = mpatches.Patch(color='yellow', label='Sand')
gray_patch = mpatches.Patch(color='gray', label='Shale')
plt.legend(handles=[yellow_patch, gray_patch])

plt.savefig('Log Plot/Shale-Sand-Log.png', dpi=300)

# Show the plot
plt.show()

