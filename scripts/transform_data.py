"""transform_data.py
Processes files in data/stream, transforms them, and writes cleaned CSVs to data/processed.
"""
import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parents[1]
stream = base / 'data' / 'stream'
processed = base / 'data' / 'processed'
processed.mkdir(parents=True, exist_ok=True)

def process_stream_files():
    files = list(stream.glob('*.csv'))
    for f in files:
        print('Processing', f)
        df = pd.read_csv(f)
        df.columns = [c.strip() for c in df.columns]
        # If it's orders
        if 'order_id' in df.columns:
            df['order_placed_at'] = pd.to_datetime(df['order_placed_at'])
            df['delivered_at'] = pd.to_datetime(df['delivered_at'])
            df['delivery_hours'] = (df['delivered_at'] - df['order_placed_at']).dt.total_seconds() / 3600.0
            df.to_csv(processed / ('cleaned_' + f.name), index=False)
        else:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df.to_csv(processed / ('cleaned_' + f.name), index=False)
        f.unlink()

if __name__ == '__main__':
    process_stream_files()
