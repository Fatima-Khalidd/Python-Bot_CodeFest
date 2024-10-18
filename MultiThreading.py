import threading
from Selenium import submit_form

def process_rows_in_threads(rows, thread_count):
    threads = []  
    for row in rows:
        if len(row) >= 2:  
            name = row[0]
            email = row[1]
            thread = threading.Thread(target=submit_form, args=(name, email))
            threads.append(thread)
            thread.start() 

            
            if len(threads) >= thread_count:
                for thread in threads:
                    thread.join() 
                threads = []  

    for thread in threads:
        thread.join()
