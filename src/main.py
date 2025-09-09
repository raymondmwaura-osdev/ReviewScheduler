from generator import add_study_date
from init import init_scheduler
import argparse

parser = argparse.ArgumentParser(prog="ReviewScheduler")

# SubParsers
subparser = parser.add_subparsers(dest="command", required=True)

subparser.add_parser(
    "init",
    help="Initiate ReviewScheduler in the current directory."
)

add_date_parser = subparser.add_parser(
    "add",
    help="Add study date."
)
add_date_parser.add_argument(
    "study_date",
    help="Study date. Can be 'today' or a date in this format: 'YYYY-MM-DD'.",
    metavar="today / YYYY-MM-DD"
)

args = parser.parse_args()

###

if args.command == "init":
    init_scheduler()

elif args.command == "add":
    add_study_date(args.study_date)
