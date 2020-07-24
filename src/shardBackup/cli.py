from argparse import ArgumentParser, Action
import bitmath

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
    parser.add_argument("source", help="Directory to copy from")
    parser.add_argument("target", help="Directory to copy to")
    parser.add_argument("--index",
        help="Where to start in dir. eg 2G wouldn't backup the first 2 Gibibytes",
        nargs=2
        )
    parser.add_argument("--endIndex",
        help="where to stop in dir. eg 2G would stop after backing up 2 Gibibytes",
        nargs=2)

    return parser