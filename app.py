from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt, mpld3
from matplotlib.dates import DateFormatter

app = Flask(__name__)

@app.route('/')
def home():
    # Read the CSV file
    df = pd.read_csv('static/speedtest.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create a new figure
    fig, ax = plt.subplots()

    # Plot the data as both lines and points
    ax.plot(df['timestamp'], df['download'], label='Download Speed')
    ax.scatter(df['timestamp'], df['download'])
    
    ax.plot(df['timestamp'], df['upload'], label='Upload Speed')
    ax.scatter(df['timestamp'], df['upload'])

    # Set the date formatter
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))

    # Set the legend
    ax.legend()

    # Label the axes
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed (Mbps)')

    # Set the title
    ax.set_title('Internet Speed Over Time')

    # Convert the plot to HTML
    plot_html = mpld3.fig_to_html(fig)

    # Render the plot in the 'index.html' template
    return render_template('index.html', plot=plot_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True) 