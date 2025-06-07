import os


def get_data_dir_path():
    """Gets the path to repo 'data' directory"""

    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
