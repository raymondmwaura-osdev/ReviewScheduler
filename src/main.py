"""
Use argparse to get the "init" argument.
If it is given, use the "init" module to initiate the scheduler in the current working directory.
"""

from init import init_scheduler
import argparse

parser = argparse.ArgumentParser(prog="ReviewScheduler")

# SubParsers
subparser = parser.add_subparsers(dest="command", required=True)

subparser.add_parser(
    "init",
    help="Initiate ReviewScheduler in the current directory."
)

args = parser.parse_args()

###

if args.command == "init":
    init_scheduler()

else:
    print("Not Initiating")
