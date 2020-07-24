from argparse import ArgumentParser, Action
import bitmath
import shutil

# Handle CLI options
# relied heavil on https://linuxacademy.com/cp/courses/lesson/course/3802/lesson/3

class ByteAction(Action):
     def __call__(self, parser, namespace, values, option_string=None)
     '''
     turns input of xB, xKi, xMi, xGi, xTi, xPi or xEi IEC into Bytes
     
     '''
        bitmath.parse_string_unsafe("", system=bitmath.NIST).to_Byte()


def create_parser():
    parser = ArgumentParser(description="""
        backup large directory structure to multiple smaller directories/devices.
        """)
    parser.add_argument("source_directory", help="Directory to copy from")
    parser.add_argument("target_directory", help="Directory to copy to")
    parser.add_argument("--index", "-i",
        help="Where to start in dir. eg 2G wouldn't backup the first 2 Gibibytes",
        nargs=1
        )
    parser.add_argument("--endindex", "-e",
        help="where to stop in dir. eg 2G would stop after backing up 2 Gibibytes",
        nargs=1)
    parser.add_argument("--quiet", "-q"
        help="program defaults to verbose, --quiet sets output to --quiet")
    parser.add_argument("--rsync", "-r"
        help="Use rsync instead of internal code to copy files over")
    parser.add_argument("--nohash", "-n"
        help="program defaults to no ")

    return parser

'''
class DiskAction():
    def __call__ (self, parser,)
    total, used, free = shutil.disk_usage('dir')

"""