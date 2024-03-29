import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd




def plot_ratings(merged_ratings):
    # Create traces
    trace_kayak = go.Scatter(x=merged_ratings.index, y=merged_ratings['kayak'], mode='markers+lines', name='Kayak', marker=dict(color='rgb(237, 114, 50)'))
    trace_scanner = go.Scatter(x=merged_ratings.index, y=merged_ratings['scanner'], mode='markers+lines', name='SkyScanner', marker=dict(color='rgb(49, 110, 219)'))

    # Create layout
    layout = go.Layout(title='Average Ratings by Year',
                       xaxis=dict(title='Year', tickfont=dict(color='rgb(96, 112, 224)')),  # Set x-axis tick font color
                       yaxis=dict(title='Rating', tickfont=dict(color='rgb(96, 112, 224)')),  # Set y-axis tick font color
                       showlegend=True,
                        xaxis_gridcolor='rgb(180,191,244)',  # Set x-axis grid color
                       yaxis_gridcolor='rgb(180,191,244)',  # Set y-axis grid color
                       plot_bgcolor='rgba(255, 255, 255, 0)',  # Transparent background
                       paper_bgcolor='rgba(255, 255, 255, 0)', # Transparent plot area
                      )

    # Create figure
    fig = go.Figure(data=[trace_kayak, trace_scanner], layout=layout)
    
    pio.write_image(fig, 'average_rating_per_year.svg', format='svg')

    # Show plot
    fig.show()

def plot_histogram(merged_ratings):
    # Create traces
    trace_kayak = go.Bar(x=merged_ratings.index, y=merged_ratings['kayak'], name='Kayak', marker=dict(color='rgb(237, 114, 50)'))
    trace_scanner = go.Bar(x=merged_ratings.index, y=merged_ratings['scanner'], name='SkyScanner', marker=dict(color='rgb(49, 110, 219)'))

    # Create layout
    layout = go.Layout(title='Ratings Histogram',
                       xaxis=dict(title='Rating', tickfont=dict(color='rgb(96, 112, 224)')),  # Set x-axis tick font color
                       yaxis=dict(title='Frequency', tickfont=dict(color='rgb(96, 112, 224)')),  # Set y-axis tick font color
                       barmode='group',  # Group bars
                       showlegend=True,
                       xaxis_gridcolor='rgb(180,191,244)',  # Set x-axis grid color
                       yaxis_gridcolor='rgb(180,191,244)',  # Set y-axis grid color
                       plot_bgcolor='rgba(255, 255, 255, 0)',  # Transparent background
                       paper_bgcolor='rgba(255, 255, 255, 0)', # Transparent plot area
                      )

    # Create figure
    fig = go.Figure(data=[trace_kayak, trace_scanner], layout=layout)
    
    pio.write_image(fig, 'average_rating_histogram.svg', format='svg')

    # Show plot
    fig.show()

    
def words_count(df):
    all_reviews = ' '.join(df.astype(str))
    words = all_reviews.lower().split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    word_counts_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])

    sorted_word_counts = word_counts_df.sort_values(by='Count', ascending=False)
    return sorted_word_counts