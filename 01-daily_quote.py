#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "Don’t be so humble — you are not that great. (Golda Meir)",
    "If you can’t be kind, at least be vague. ( Judith Martin)",
    "Always forgive your enemies; nothing annoys them so much. (Oscar Wilde)",
    "Whoever said that money can’t buy happiness, simply didn’t know where to go shopping. (Bo Derek)",
    "I always arrive late at the office, but I make up for it by leaving early. (Charles Lamb)",
    "When a man tells you that he got rich through hard work, ask him: ‘Whose?’ (Don Marquis)"
]

def get_quote_of_the_day(quotes):
    todays_quote = None
    today = date.today().isoformat()
    random.seed(today)
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt