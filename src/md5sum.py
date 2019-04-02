import subprocess
import time

from apscheduler.schedulers.blocking import BlockingScheduler


def get_file_md5sum(file_path):
    p = subprocess.Popen("md5sum %s" % file_path, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    return output.split()[0].decode()


class MD5SUMBabySitter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(self.check, 'interval', seconds=5)
        self.last_md5 = None
        self.last_upd_time = None

    @property
    def time_since_last_update(self):
        return time.time() - self.last_upd_time

    def check(self):
        self.last_md5 = get_file_md5sum(self.file_path)
        self.last_upd_time = time.time()
        print(f"file last md5sum is: {self.last_md5} ({self.last_upd_time})")

    def start(self):
        self.scheduler.start()
