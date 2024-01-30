import matplotlib.pyplot as plt

def plot_ratings(merged_ratings):
    plt.figure(figsize=(10, 6))
    plt.plot(merged_ratings.index, merged_ratings['kayak'], marker='o', label='Kayak', color='blue')
    plt.plot(merged_ratings.index, merged_ratings['scanner'], marker='o', label='Scanner', color='green')

    plt.title('Average Ratings by Year')
    plt.xlabel('Year')
    plt.ylabel('Score')
    plt.xticks(merged_ratings.index)  
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()