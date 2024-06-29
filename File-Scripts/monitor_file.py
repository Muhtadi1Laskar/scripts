from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'{event.src_path} has been modified')

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='/path/to/monitor', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
