from argparse import ArgumentParser, Action
import bitmath
import shutil

# Handle CLI options
# relied heavil on https://linuxacademy.com/cp/courses/lesson/course/3802/lesson/3
'''
     def __call__(self, parser, namespace, values, option_string=None)
     
     turns input of xB, xKi, xMi, xGi, xTi, xPi or xEi IEC into Bytes

     
        bitmath.parse_string_unsafe("", system=bitmath.NIST).to_Byte()
'''

def create_parser():
    parser = ArgumentParser(description="""
        backup large directory structure to multiple smaller directories/devices.
        """)
    parser.add_argument("source_directory", help="Directory to copy from")
    parser.add_argument("target_directory", help="Directory to copy to")
    parser.add_argument("--index", "-i",
        help="""
        Where to start in dir. eg 2G wouldn't backup the first 2 Gibibytes. 1k=1KiB 2M=2MiB etc (defaults to 0 Bytes)
        """,
        nargs=1,
        default='0B'
        )
    parser.add_argument("--endindex", "-e",
        help="where to stop in dir. eg 2G would stop after backing up 2 Gibibytes, read --index for more, (defaults to available space in target_directory",
        nargs=1
        ) # need to add defau;t
    parser.add_argument("--quiet", "-q",
        help="program defaults to verbose, --quiet sets output to --quiet")
    parser.add_argument("--rsync", "-r",
        help="Use rsync instead of internal code to copy files over")
    parser.add_argument("--nohash", "-n",
        help="program defaults to hashing, (not necessary for backing up to filesystems that check for data integrity(e.g. zfs, most cloud storage))")

    return parser

