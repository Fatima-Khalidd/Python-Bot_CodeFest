from api import fetch_data
from MultiThreading import process_rows_in_threads

def main():
    start_row = 2  # row 2 skips the header row
    rows = fetch_data(start_row)
    if rows:
        process_rows_in_threads(rows, thread_count=3)
    else:
        print("No data found.")

if __name__ == "__main__":
    main()
