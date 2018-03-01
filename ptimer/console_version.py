import sys
import time


class Ptimer(object):
    def __init__(self, round_time=25, break_time=5, large_break_time=20):
        # convert to seconds
        self.round_time = round_time * 60
        self.break_time = break_time * 60
        self.large_break_time = large_break_time * 60
        self.round_sleep = .5  # settable in this way to speed up tests
        self.ring_sleep = 3  # settable in this way to speed up tests

    def ring(self):
        # Extra spaces to cover up any lingering characters from previous writes
        sys.stdout.write("\r ring ring ring ring                               ")
        sys.stdout.flush()

        # sleep so it rings for a few seconds
        time.sleep(self.ring_sleep)

    def round(self, message, max_time):
        time_elapsed = 0
        time_started = time.time()
        while time_elapsed < max_time:
            time_elapsed = time.time() - time_started
            sys.stdout.write(message + " %i:%i time left             " % ((max_time - time_elapsed) // 60, (max_time - time_elapsed) % 60))
            sys.stdout.flush()
            # Sleeping here drastically reduces CPU load
            time.sleep(self.round_sleep)
            time_elapsed = time.time() - time_started

        self.ring()

    def start(self):
        for i in range(4):
            message = "\r On round %i. There is" % (i + 1)
            self.round(message, self.round_time)
            if i == 3:
                message = "\r On break %i. There is" % (i + 1)
                self.round(message, self.large_break_time)
            else:
                message = "\r On break %i. There is" % (i + 1)
                self.round(message, self.break_time)
