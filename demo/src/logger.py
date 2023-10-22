import logging
import sys


def get_logger():
    logging.getLogger(__name__)


def setup_logger():
    # clear log
    file_to_delete = open("log.log",'w')
    file_to_delete.close()

    file_handler = logging.FileHandler(filename='log.log')
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    handlers = [file_handler, stdout_handler]

    logging.basicConfig(
        level=logging.INFO, 
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        handlers=handlers,
    )

    return get_logger()


def read_logs():
    sys.stdout.flush()
    with open("log.log", "r") as f:
        return f.read()
