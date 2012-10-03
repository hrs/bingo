#!/usr/bin/env python

import random, sys

# check for the right # of args
if len(sys.argv) != 4:
    print "USAGE: " + sys.argv[0], " [file of terms] [output file] [# of cards]"
    print "Example: " + sys.argv[0] + " bingo_terms.txt bingo.html 20"
    sys.exit(1)

# read in the bingo terms
in_file = open(sys.argv[1], 'r')
terms = [line.strip() for line in in_file.readlines()]
terms = filter(lambda x: x != "", terms)
in_file.close()

# XHTML4 Strict, y'all!
head = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
        "<html lang=\"en\">\n<head>\n"
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Bingo Cards</title>\n"
        "<style type=\"text/css\">\n"
        "\tbody { font-size: 12px; }\n"
        "\ttable { margin: 40px auto; border-spacing: 2px; }\n"
        "\t.newpage { page-break-after:always; }\n"
        "\ttr { height: 60px; }\n"
        "\ttd { text-align: center; border: thin black solid; padding: 10px; width: 60px; }\n"
        "</style>\n</head>\n<body>\n")

# Generates an HTML table representation of the bingo card for terms
def generateTable(terms, pagebreak = True):
    ts = terms[:12] + ["FREE SPACE"] + terms[12:24]
    if pagebreak:
        res = "<table class=\"newpage\">\n"
    else:
        res = "<table>\n"
    for i, term in enumerate(ts):
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

out_file = open(sys.argv[2], 'w')
out_file.write(head)
cards = int(sys.argv[3])
for i in range(cards):
    random.shuffle(terms)
    if i != cards - 1:
        out_file.write(generateTable(terms))
    else:
        out_file.write(generateTable(terms, False))
out_file.write("</body></html>")

out_file.close()
