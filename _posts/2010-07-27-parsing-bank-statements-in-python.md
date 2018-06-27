---
id: 2448
title: Parsing Bank Statements in Python
date: 2010-07-27T10:00:25+00:00
author: Peter Backx
layout: post
guid: http://www.streamhead.com/?p=2448
permalink: /parsing-bank-statements-in-python/
dsq_thread_id:
  - "122615199"
image: /wp-content/uploads/2010/07/money.png
categories:
  - New Media and the World
---
A few weeks ago, <a title="How to Move From Wesabe to the PearBudget Spreadsheet" href="http://www.streamhead.com/wesabe-to-pearbudget/" target="_blank">I mentioned my new way of tracking my budget</a> and also figured that there&#8217;s one gaping hole: importing bank statements. This is part 1, where I create a simple parser for bank statements provided by my bank in CSV format.

<!--more-->The exported statements follow a very easy format that, I presume, mirrors the more common OFX format, used by Microsoft Money and others. The CSV file has its data ordered in 8 columns and even includes a (Dutch for me) header, so there&#8217;s no possible confusion. The format looks as follows (I removed any identifying items of course):

<pre style="overflow:scroll">"JAAR + REFERTE";"UITVOERINGSDATUM";"VALUTADATUM";"BEDRAG";"MUNT V/D REKENING";"TEGENPARTIJ VAN DE VERRICHTING";"DETAILS";"REKENINGNUMMER"
"2010-0245";"12/07/2010";"12/07/2010";"-9,99";"EUR";"XXX-XXXXXXXX-XX";"REMOVED TO PROTECT MY INNOCENCE";"XXX-XXXXXXXX-XX"
"2010-0244";"12/07/2010";"12/07/2010";"-100,00";"EUR";"DIRECT DEBIT";"REMOVED TO PROTECT MY INNOCENCE";"XXX-XXXXXXXX-XX"
"2010-0243";"12/07/2010";"10/07/2010";"+100,00";"EUR";"XXX-XXXXXXXX-XX";"REMOVED TO PROTECT MY INNOCENCE";"XXX-XXXXXXXX-XX"
"2010-0242";"12/07/2010";"11/07/2010";"-5,00";"EUR";"CASH WITHDRAWEL";"REMOVED TO PROTECT MY INNOCENCE";"XXX-XXXXXXXX-XX"
"2010-0241";"12/07/2010";"12/07/2010";"-1000,00";"EUR";"OTHER";"REMOVED TO PROTECT MY INNOCENCE";"XXX-XXXXXXXX-XX"<br /></pre>

Depending on your bank, the header will most likely be in another language and could be slightly different.

The parser looks like this:

<pre lang="python">#!/usr/bin/env python3
# www.streamhead.com

import collections
import sys

ID, EXECUTION_DATE, VALUE_DATE, AMOUNT, CURRENCY, COUNTERPARTY, DETAILS, ACCOUNT_NUMBER = range(8)
SEPERATOR = ';'

Transaction = collections.namedtuple("Transaction",
                "id executionDate valueDate amount currency counterparty details accountNumber")

def process_line(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == SEPERATOR:
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)
    return Transaction(fields[ID], fields[EXECUTION_DATE],
                       fields[VALUE_DATE], fields[AMOUNT],
                       fields[CURRENCY], fields[COUNTERPARTY],
                       fields[DETAILS], fields[ACCOUNT_NUMBER])

def print_transactions(transactions):
    for transaction in transactions:
        print("{0.id} on {0.executionDate}: {0.currency} {0.amount} for {0.counterparty}".format(transaction))

def main():
    if len(sys.argv) == 1:
        sys.argv.insert(1, "data\\TEST.CSV")
    filename = sys.argv[1]
    print("loading file {}".format(filename))
    transactions = []
    for line in list(open(filename))[1:]:
        line = line.rstrip()
        if line:
            transactions.append(process_line(line))
    transactions.sort(key=lambda t: t.id)
    print_transactions(transactions)

main()</pre>

By default it will take a testfile I have in a &#8220;data&#8221; subdirectory, but it can also get the filename from the command line. And that&#8217;s really all there is to parsing in Python (I suppose it can be made even simpler, by using the csv module, but this is a Python exercise for me).

Next up: actually doing something with the data.

([image credit](http://www.flickr.com/photos/pagedooley/3302646512/in/photostream/))

<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->