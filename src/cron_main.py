import sys
import time

if __name__ == "__main__":
    try:
        for _ in range(10):
            print("hello")
            time.sleep(5)
    except KeyboardInterrupt:
        print("exiting")
        sys.exit(0)
