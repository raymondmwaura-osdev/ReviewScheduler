from scheduler import schedule_review_dates
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
add_date_parser.add_argument("study_date")

args = parser.parse_args()

###

if args.command == "init":
    init_scheduler()

elif args.command == "add":
    print(schedule_review_dates(args.study_date))
