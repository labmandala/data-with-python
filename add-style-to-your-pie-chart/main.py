import matplotlib.pyplot as plt 

snack_scores = [90, 66, 39]

slice_labels = ["Avocado", "Pineapple", "Coconut"]

colors = ["#5F9EA0","#FF1493","#7FFFD4"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)

plt.title("Sarah's Favorite Snacks", fontsize=22)

plt.savefig("snack_scores")