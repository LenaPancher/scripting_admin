import logging

mylogs = logging.getLogger(__name__)
mylogs.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
streamformat = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
stream.setFormatter(streamformat)

mylogs.addHandler(stream)
