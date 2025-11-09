"""data_ingestion.py
Simulates streaming by copying raw CSVs into a 'stream' folder as new messages.
Use --simulate flag to run once and create simulated message files.
"""
import argparse
from pathlib import Path
import shutil
import time

base = Path(__file__).resolve().parents[1]
raw = base / 'data' / 'raw'
stream_dir = base / 'data' / 'stream'
stream_dir.mkdir(parents=True, exist_ok=True)

def simulate_once():
    # Copy sample files into stream as simulated 'messages'
    for f in ['orders_sample.csv','route_density_sample.csv']:
        src = raw / f
        dest = stream_dir / f.replace('.csv', f'_msg_{int(time.time())}.csv')
        shutil.copy(src, dest)
        print('Simulated message written to', dest)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--simulate', action='store_true')
    args = parser.parse_args()
    if args.simulate:
        simulate_once()
    else:
        print('Run with --simulate to create simulated stream files.')
