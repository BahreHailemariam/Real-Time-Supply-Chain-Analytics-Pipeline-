"""automate_etl.py
Runs transform_data -> kpi_calculations periodically using schedule.
"""
import time, schedule, subprocess, sys
from pathlib import Path

base = Path(__file__).resolve().parents[1]

def run_etl():
    print('Running ETL cycle...')
    subprocess.run([sys.executable, base / 'scripts' / 'transform_data.py'])
    subprocess.run([sys.executable, base / 'scripts' / 'kpi_calculations.py'])
    print('ETL cycle complete.')

if __name__ == '__main__':
    schedule.every(30).seconds.do(run_etl)
    print('Scheduler started. Press Ctrl+C to stop.')
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print('Scheduler stopped.')
