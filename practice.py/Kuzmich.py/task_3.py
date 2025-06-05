import sys
from datetime import datetime

class Logger:
    def __init__(self, out_stream=sys.stderr, time_format='%Y-%m-%d %H:%M:%S'):
       
        self.out_stream = out_stream
        self.time_format = time_format
    
    def log(self, message):
   
        current_time = datetime.now().strftime(self.time_format)
        log_message = f"[{current_time}] {message}\n"
        self.out_stream.write(log_message)
        self.out_stream.flush()  


if __name__ == "__main__":
    
    logger = Logger()  

    logger.log('This is an informational message')
    logger.log('Warning: something is wrong')
    logger.log('Error: critical failure')
