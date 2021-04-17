import uuid


def random_filename(filename:str,length=36):
    suffix = filename.rsplit('.',maxsplit=1)[-1]
    uid = uuid.uuid4().__str__()[:length]
    filename_new = uid + '.' + suffix
    return filename_new
