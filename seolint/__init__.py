import re
from urllib import urlopen
from argparse import ArgumentParser

from lxml.cssselect import CSSSelector
from lxml.html import parse
from lxml import etree


def extract_keywords(text):
    if text:
        return re.sub('[^A-Za-z0-9\-]', ' ', text).lower().split()
    else:
        return []


def keywords_for_tag(tag, tree):
    sel = CSSSelector(tag)
    keywords = []
    for e in sel(tree):
        keywords.extend(extract_keywords(e.text))
    return keywords


def lint(url):
    webf = urlopen(url)
    tree = parse(webf)
    check_tags = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'strong', 'em', 'p']
    for tag in check_tags:
        kw = " ".join(keywords_for_tag(tag, tree))
        if kw:
            print
            print "*** %s keywords ***" % tag
            print kw


def main():
    p = ArgumentParser(description='Checks on-page factors. Very basic.')
    p.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                   help='print detailed output')
    p.add_argument('url', type=str,
                   help='url to check')
    args = p.parse_args()
    print "Fetching %s" % args.url
    lint(args.url)


if __name__ == '__main__':
    main()
