#!/usr/bin/env python
"""
Basic template for CSV file processing.

This script will read through each row in a CSV file, re-order the columns, and then write a new CSV as output.

Usage:

    ./process_csv.py input.csv > output.csv

The starting `#!` lets us execute the file directly without typing `python process_csv.py`.
"""

import csv
import sys


def process(filename):
    """
    Process the CSV file.

    In this example we are simply going to re-order the columns.
    """
    # This will contain all the rows we want to output
    output = []
    # First add the headers in our new order
    output.append(['Title', 'Author', 'Year', 'ISBN'])
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_number = 0
        for row in csv_reader:
            line_number += 1
            if line_number == 1:
                # Ignore the first row since they are headers
                continue
            try:
                # Copy the cells into variables so its easier to tell what we're working with
                title = row[0]
                isbn = row[1]
                author = row[2]
                year = row[3]
                # Add a row to our output with the new ordering
                output.append([title, author, year, isbn])
            except IndexError:
                # If a column is missing, write a helpful error message and skip the row
                sys.stderr.write('Missing column on line {}, skipping\n'.format(line_number))
    # We have finished processing the CSV, now write our new output
    # By writing to sys.stdout we can easily redirect output to a file like `> output.csv`
    # It's important to use csv.writer to handle special characters like `,`
    csv_writer = csv.writer(sys.stdout)
    for row in output:
        csv_writer.writerow(row)


# This if statement ensures this only runs when executed as script, not when included from an import
if __name__ == '__main__':
    try:
        # Grab the filename from the first argument
        filename = sys.argv[1]
        # Call our file processing function
        process(filename)
    except IndexError:
        # Write to stderr instead of printing so we don't interfere with normal CSV output
        sys.stderr.write('Error, no filename provided\n')
        # sys.argv[0] is the name of our script, this lets us rename our script without updating this string
        sys.stderr.write('Usage: {} filename\n'.format(sys.argv[0]))
