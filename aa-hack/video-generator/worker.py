import logging
from queue import Queue
from threading import Thread
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class DownloadWorker(Thread):

    def __init__(self, queue, out_que):
        Thread.__init__(self)
        self.queue = queue
        self.out_que = out_que

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            video, txnId = self.queue.get()
            try:
                v = video.generate_video_part(txnId)
                self.out_que.put(v)
            finally:
                self.queue.task_done()


def main(video_obj_arr, txnId, n):
    ts = time()
    # Create a queue to communicate with the worker threads
    queue = Queue()
    out_que = Queue()
    # Create 7 worker threads
    for x in range(2):
        worker = DownloadWorker(queue, out_que)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for i in range(1, n):
        logger.info('Queueing {}'.format(i))
        queue.put((video_obj_arr[i-1], txnId))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    logging.info('Took %s', time() - ts)
    return out_que


if __name__ == '__main__':
    main()
