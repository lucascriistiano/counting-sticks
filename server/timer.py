# -*- coding: utf-8 -*-
import time
import threading


class ConfirmPresenceTimerThread(threading.Thread):

    def __init__(self, time_limit, counting_sticks, room_id, username):
        super(ConfirmPresenceTimerThread, self).__init__()

        self.lock = threading.Lock()
        self.time_limit = time_limit
        self.remaining_time = time_limit

        self.counting_sticks = counting_sticks
        self.room_id = room_id
        self.username = username
        self.running = True

    def run(self):
        while self.remaining_time > 0:
            time.sleep(1)
            self.lock.acquire()
            try:
                self.remaining_time -= 1
                if self.remaining_time == 0:
                    self.counting_sticks.disconnect_player(self.room_id, self.username)
                    self.running = False
                    return
            finally:
                self.lock.release()

    def reset(self):
        self.lock.acquire()
        if self.running:
            self.remaining_time = self.time_limit
        self.lock.release()