#!/bin/python3
from features import (
    add,
    init,
    review
)
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

review_parser = subparser.add_parser(
    "review",
    help="Output a markdown file showing reviews for the given date."
)
review_parser.add_argument(
    "review_date",
    help="Review date. Can be \"today\" or a date in this format: 'YYYY-MM-DD'."
)

args = parser.parse_args()

###

if args.command == "init":
    init.init_rs()

elif args.command == "add":
    add.study_date(args.study_date)

elif args.command == "review":
    review.get_reviews(args.review_date)
