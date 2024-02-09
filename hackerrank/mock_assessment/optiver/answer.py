import sys

# example input in log.txt
with open('./log.txt', 'r') as file:
    csv_input = file.read()
# csv_input = sys.stdin.read()   # from test


# Enter your code here. The csv input has been populated for you into a string, csv_input. Print output to STDOUT

# function to sanitise rows by removing commas found between double quotes
def sanitise_row(row):
    quote_indices = []
    for i in range(len(row)):
        if row[i] == '"':
            quote_indices.append(i)

    if len(quote_indices) % 2 != 0:
        raise Exception(f"Data error, row contained odd amount of double quotes:\n {row}")

    for i in range(len(quote_indices) - 1):
        row = row[:quote_indices[i]] + row[quote_indices[i]:quote_indices[i + 1]].replace(',', '_') + row[quote_indices[
                                                                                                              i + 1]:]
    return row.split(',')


csvRows = csv_input.split("\n")

header = csvRows[0].split(",")
DATE_INDEX = header.index('date')
PROCESS_INDEX = header.index('process')
BYTES_INDEX = header.index('bytes')
csvRows = csvRows[1:]

# build dictionary of dictionaries where high-level key is date and the values are themselves keys of the exchange name with inner values of the output row with cumulative total bytes field
# this process makes sorting later simple
dates_dict = {}
for row in csvRows:
    split_row = row.split(",")
    if (len(split_row) > len(header)):
        split_row = sanitise_row(row)
    date = split_row[DATE_INDEX]
    exchange = split_row[PROCESS_INDEX].split("_")[0]
    bytes = split_row[BYTES_INDEX]

    if date not in dates_dict:
        dates_dict[date] = {}
    elif exchange not in dates_dict[date]:
        dates_dict[date][exchange] = None
    else:
        if dates_dict[date][exchange] is not None:
            existing_row = dates_dict[date][exchange]
            existing_bytes = int(existing_row.split(",")[2])
            bytes = int(bytes) + existing_bytes

    new_row_string = f"{date},{exchange},{bytes}"
    dates_dict[date][exchange] = new_row_string

# sort by exchange within a given date
for k, v in dates_dict.items():
    dates_dict[k] = dict(sorted(v.items()))
# sort by date
sorted_dates_dict = dict(sorted(dates_dict.items()))

new_header = "date,exchange,total_bytes"
print(new_header)
for dateKey, dateValue in sorted_dates_dict.items():
    for row in sorted_dates_dict[dateKey].values():
        print(row)
