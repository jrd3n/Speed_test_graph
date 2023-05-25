import speedtest
import pandas as pd
from datetime import datetime
import os

def speed_test():
    s = speedtest.Speedtest()

    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    data = {
        'timestamp': datetime.now(),
        'download': res["download"] / 10**6,  # Convert bytes to megabytes
        'upload': res["upload"] / 10**6,  # Convert bytes to megabytes
        'ping': res["ping"]
    }

    return data

if __name__ == "__main__":
    data = speed_test()

    # Create or append to csv
    df = pd.DataFrame([data])

    file_path = "static/speedtest.csv"

    # Check if the file does not exist and write the header
    if not os.path.isfile(file_path):
        df.to_csv(file_path, mode='a', header=True)
    else:  # else it exists so append without writing the header
        df.to_csv(file_path, mode='a', header=False)