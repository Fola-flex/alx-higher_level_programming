#!/usr/bin/python3
# Author: Muiz Olaore

if __name__ == "__main__":
    import hidden_4
    arr = dir(hidden_4)
    for name in arr:
        if name[:2] != '__':
            print(name)
