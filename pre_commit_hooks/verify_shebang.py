#!/usr/bin/env python
import sys


def file_starts_with_shebang(filepath):
    data = open(filepath, 'rb').read(2)
    return data == b'#!'


def verify_shebang(staged_files):
    for filepath in staged_files:
        if not file_starts_with_shebang(filepath):
            print('Found staged script file that does not start with a shebang: {}'.format(filepath))
            return 1
    return 0


def main():
    staged_files = sys.argv[1:]
    status_code = verify_shebang(staged_files)
    sys.exit(status_code)


if __name__ == '__main__':
    main()
