from datetime import datetime

def Main():
    log_file_path = "C:/Users/David$$/Desktop/log.txt"
    parsed_logs = ParseLogFile(log_file_path)
    for log_entry in parsed_logs:
        date_time, error = log_entry
        print(f"Date Time: {date_time}, Error: {error}")

def ParseLogFile(file_path):
    log_entries = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('-')
                    if len(parts) >= 2:
                        date_time_str = parts[0].strip()
                        error = ':'.join(parts[1:]).strip()

                        try:
                            date_time = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')
                            log_entries.append((date_time.date(), date_time.time(), error))
                        except ValueError:
                            print(f"Ignoring invalid log entry: {line}")
                            
    except FileNotFoundError:
        print("Log file not found at the specified path.")
    
    return log_entries



if __name__ == '__main__':
    Main()