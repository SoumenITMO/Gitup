__author__ = 'Soumen'

from newspaper import Article
import socket
import urllib2
from bs4 import BeautifulSoup
import urllib
import html2text

keywords = ["painful", "refugee", "funding", "dysfunctional", "asylum", "voucher", "agency",
            "stipend", "sanitation", "deterioration", "allocate", "humanitarian",
            "regional", "aid", "applicant", "infrastructure", "deteriorate", "displace",
            "chaos", "seekers", "coast", "aid", "help", "border", "immigrants", "attacks",
            "worse", "recession", "occasions", "condemn", "terrible", "undocumented immigrants",
            "missiles", "injuring", "town", "others", "Nazi", "freedom", "freedom fighters",
            "suffering", "suckered", "jihad", "affect", "elections", "Syria", "facilities", "established",
            "enormous", "billion", "activities", "donors", "conflict", "flee", "police", "Grants", "arrive",
            "worse", "force", "Asylum, Right of", "Child Detention", "Compulsory resettlement", "Defectors",
            "Deportation", "Displaced persons", "Ethnic cleansing", "Exile", "Expulsion", "Forcible displacement",
            "Forced migration", "Genocide", "Human trafficking", "Human rights", "Internal displacement",
            "Internal migrants", "Internally displaced persons", "International human rights",
            "Involuntary resettlement", "Mass migration", "Migration, forced", "Migration, internal", "Persecution",
            "Political migrants", "Population resettlement", "Population transfers", "Refugee children",
            "Refugee policy", "Refugees", "Relocation, forced", "Resettlement, involuntary", "Sanctuary (law)",
            "Social Justice", "War crimes", "Women refugees"]


def search_word(url__):
    error = 0
    title = ""
    url = "http://voiceofrussia.com/us/2014_04_01/Five-Gitmo-prisoners-might-receive-refugee-status-in-Uruguay-6380/"
    #url = "http://greece.greekreporter.com/2014/01/01/syrian-refugees-having-a-hard-time-in-greece/"
    str =""
    """
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    try:
        req = urllib2.Request(url, headers=hdr)
        f = urllib2.urlopen(req)
        soup = BeautifulSoup(f.read(), from_encoding=f.info().getparam('charset'))
        title = soup.find('title').text
        print(title)
    except UnicodeDecodeError:
        print("ERROR")
        error = 1
    """


    try:
            article = Article(url__)
            article.download()
            article.parse()
            text = article.text.split(" ")
            str = ""
            keyword_count = 0

            for word in text:
                if word != " " and word != None:
                    if word in keywords:
                        str += word + ","
            keyword_count += 1
    except socket.timeout:
        ""
    return str

