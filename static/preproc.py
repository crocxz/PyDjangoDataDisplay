import csv
import json
import sys
import glob
import os
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# check if args, no args = current dir
def main(argv):
    buffer = []
    dir_path = ''
    out_path = ''
    dfile = 'dump.json'

    # no args default: current directory for read, write output to default "dump.json"
    if len(sys.argv) == 1:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        out_path = os.path.join(os.getcwd(), dfile)
        print("executing with no args, dir_path is: {}  out_path is {}".format(
            dir_path, out_path))
    # else set dir_path and out_path
    else:
        dir_path = sys.argv[1]
        out_path = sys.argv[2]
        print("executing with args, dir_path is: {}  out_path is {}".format(
            dir_path, out_path))

    #scan for csv files, populate buffer with csv data, write buffer to json
    names = scan(dir_path)
    read_csv(names, buffer)
    write_json(buffer, out_path)

    # modify handler
    class Event(PatternMatchingEventHandler):
        patterns = ["*.csv"]
        def on_any_event(self, event):
            names = scan(dir_path)
            buffer = []
            read_csv(names, buffer)
            write_json(buffer, out_path)
            print("rescanned and repopulated json")

    # setup handler 
    print("listening")
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, dir_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
            
# return file names of csvs in dir
def scan(dir_path):
    os.chdir(dir_path)
    names = glob.glob("*.csv")
    print("Files scanned")
    return names

# read csv files data into buffer
def read_csv(names, buffer):
    fieldnames = ("date", "filename", "action", "rating")
    for file in names:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            print("Read a file: {} ".format(file))
            for row in reader:
                if reader.line_num == 1:
                    continue
                buffer.append(row)

# write buffer into jsonfile
def write_json(buffer, out_path):
    jsonfile = open(out_path, 'w')
    jsonfile.write(json.dumps([row for row in buffer], indent=4))
    print("Write complete")

if __name__ == "__main__":
    main(sys.argv[1:])
