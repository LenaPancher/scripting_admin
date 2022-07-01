import logging


def logging_conf(logging_level):
    # Display the logs in the logging.log file
    print(logging_level)
    logging.basicConfig(
        filename='logging_base64.log',
        level=logging_level,
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
