import matplotlib.pyplot as plt 

snack_scores = [90, 66, 39]

slice_labels = ["Avocado", "Pineapple", "Coconut"]

plt.pie(snack_scores, labels=slice_labels)

plt.title("Sarah's Favorite Snacks")

plt.savefig("snack_scores")