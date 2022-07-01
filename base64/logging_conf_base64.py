import logging


def logging_conf(logging_level):
    """
    Configuration to display logs in the console
    Args:
        logging_level: Lowest severity log message that a recorder will process
    """
    print(logging_level)
    logging.basicConfig(
        filename='logging_base64.log',
        level=logging_level,
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s : %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
