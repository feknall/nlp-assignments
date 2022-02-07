def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


if __name__ == "__main__":
    with open('elapsed/elapsed_original.txt', 'r') as handle:
        lines = handle.readlines()
    seconds_set = set()
    for line in lines:
        seconds_set.add(str(get_sec(str(line))))
    with open('elapsed/elapsed_converted.txt', 'w') as f:
        for item in seconds_set:
            f.write(item + '\n')
