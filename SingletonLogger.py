import threading
import datetime
from enum import Enum
import time


class ErrorType(Enum):

    CRITICAL = 1,
    ERROR = 2,
    WARN = 3
    INFO = 4
    DEBUG = 5


class SingletonLogger:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls,file_name):

        if cls._instance is None:
            with cls._lock:

                if not cls._instance:
                    cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self,file_name):
        self.file_name = file_name

    def _write_log(self, type, msg):
        
        now = datetime.datetime.now()
        
        try:

            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}][{1}] {2}\n".format(now.__str__(), type.name, msg))
        
        except IOError as e:
            print(e)
            print(e.errno)
            print(e.strerror)
            print("I couldn't open the file")

    def log(self, type:ErrorType, msg):
        self._write_log(type, msg)

    def critical(self, msg):
        self._write_log(ErrorType.CRITICAL, msg)

    def error(self, msg):
        self._write_log(ErrorType.ERROR, msg)

    def warn(self, msg):
        self._write_log(ErrorType.WARN, msg)

    def info(self, msg):
        self._write_log(ErrorType.INFO, msg)

    def debug(self, msg):
        self._write_log(ErrorType.DEBUG, msg)




if __name__ == "__main__":

    s1 = SingletonLogger("logfile.txt")
    
    s1.log(ErrorType.CRITICAL, "Critical message")

    time.sleep(3)

    s2 = SingletonLogger(r"C:\Users\User\Desktop\logfile.txt")
    s2.critical("Another critical message")
