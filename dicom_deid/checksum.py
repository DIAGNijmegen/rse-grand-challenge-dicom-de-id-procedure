import hashlib


def __calculate_sha256sum(filename):
    with open(filename, "rb") as f:
        # Small files, fine to read in one go
        return hashlib.sha256(f.read()).hexdigest()


def sha256sum(filename):
    sum = __calculate_sha256sum(filename)

    sum_filename = filename.with_name(filename.name + ".sha256")
    with open(sum_filename, "w") as f:
        f.write(sum)
