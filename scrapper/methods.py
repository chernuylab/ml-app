import os
import errno


class Methods:
    def make_sure_path_exists(path):
        try:
            os.mkdir(path, 0o777)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
