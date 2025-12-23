import string

BASE62 = string.ascii_letters + string.digits

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]

    result = []
    while num > 0:
        num, rem = divmod(num, 62)
        result.append(BASE62[rem])

    return ''.join(result)
