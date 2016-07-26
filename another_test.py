import re
from newspaper import Article
import os
import zipfile as z
from TwitterSearch import *
import json
from pymongo import MongoClient
import sys
import socket
import urllib2


# ... SET DEFAULT ENCODING ... #
reload(sys)
sys.setdefaultencoding('utf-8')
# ............................ #

searchWords = []
events_limiter = 10    # EVENT LIMITER FOR NOT TO PROCESS FULL ARCHRIVE FILE
posts = MongoClient('localhost', 27017)
db = posts.local

# ---- CLEAR ARRAY -------- #
def clearArr(arr_Key):
    index = 0
    for key_ in arr_Key:
        index += 1
    index = index - 1
    while index >= 0:
        del searchWords[index]
        index -= 1
# ------------------------- #
# -------------------->> TWITTER FUNCTION <<------------------- #
def twitter_search_(keys_arr, archive_fileName):

    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords(keys_arr)  # let's define all words we would like to have a look for
        # tso.set_language('en')  # FOR LANGUAGE
        tso.set_include_entities(True)  # and don't give us all those entity information
        ts = TwitterSearch(
            consumer_key = 'EKx977DCnbfn96jNaZsaXz4uH',
            consumer_secret = 'nC2xfYnMHVWCvZY14ZNcXBr6K94xaAr0sbrlNbxmUXFeSEVXc1',
            access_token = '1364904890-QJh9eK1ToUkDWZzCaNDr6aAvOPooNLwtnciBVXd',
            access_token_secret = '381eYQ54oB0ucxWvgiDizIIA5JeDkszaxsay1RgALQYDW'
         )
        print(searchWords)
        for tweet in ts.search_tweets_iterable(tso):
            with open('data.txt', 'w') as outfile:
                json.dump(tweet, outfile)
                new_posts = [{"Keyword__": searchWords, "GDELT_file": archive_fileName, "Twitter_data_": tweet}]
                db.Syria_Refugee.insert(new_posts)
                print(tweet)

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)
    clearArr(searchWords)
# ------------------------------------------------------------- #

skip_words_list = ["a", "in", "offer", "do", "must", "the", "on", "before", "round", "upon", "come", "to", "us",
                   "provide", "more", "-", ".", ";", "push", "face", "hand", "leg", "for", "be", "aid", "Leave",
                   "Access", "Denied", "continues", "provides", "keep", "skeleton", "staff", "International",
                   "accepts", "Holds", "by", "Flee", "TV", "news", "press", "Page", "not", "found", "how", "out", "of",
                   "running", "situation", "Not Found", "On", "eve", "up", "under", "The", "its", "Upcoming", "will",
                   "hit", "out", "at", "welcomed", "after", "welcomes", "-", "\xc2\xa316", "home", "chilly",
                   "applauded", "changing", "support", "million", "allocates", "|", "border", "Al", "Bawaba",
                   "rules", "admit", "Just a moment...", "Archive", "response", "with", "needs", "world", "Monarch",
                   "--", "Breaking News", "from", "over", "plan", "tenth", "we", "I", "you", "our", "my", "his",
                   "her", "she", "he", "jets", "all", "lost", "404", "found", "as", "plight", "families", "Visits",
                   "Pic", "Superfast", "3g", "3G", "4g", "4G", "Broadband", "[VIDEO]", "World", "world", "Describes",
                   "Scene", "Official", "U.N.", "COMMENT:", "Million", "Euro", "Grants", "posts", "net", "profit",
                   "QR708mn", "say", "country", "Prime", "a", "offers", "Open", "are", "is", "am", "was", "were", "Not",
                   "has", "been", "have", "arrive", "expected", "taken", "more", "only", "year", "last", "meets",
                   "children", "'", "Only", "agrees", "don&rsquo;t", "''", "Egypt", "toll", "Iraq's", "province", "Aid",
                   "Lack", "than", "camp", "Camp", "Island", "head", "vulnerable", "A", "Child", "UK", "US", "We",
                   "who", "which", "where", "essential", "Senator", "Artists", "Largest", "'a'", "country", "Minister",
                   "worse", "know", '', "frets", "civilian", "\xcb\x88regretful\xcb\x88", "1", "500", "News24", "YPE",
                   "html", "PUBLIC", "-//W3C//DTD", "XHTML", "1.0", 'Transitional//EN"', "Guide2.co.nz", "Home", "Loans"
                   , "welcomed", "accept", "Newshub", "NZNews", "100", "NZ", "Voxy.co.nz",
                   "(From', 'Redhill', 'And', 'Reigate', 'Life)", "MP", "'6'", "February", "2014", "ReliefWeb", "31",
                   "Istanbul", "&", "Blog", "&raquo;", "what", "so", "April", "2012", "Wasn\xe2\x80\x99t", "Lost",
                   "\xe2\x80\x98Lost\xe2\x80\x99", "Boy", "Viral", "From", "Alone", "PanARMENIAN.Net", "Columbian",
                   "visits", "calls", "Voice", "Expert", "opinion", "podcasts", "Jolie&#039;s", "&#039;Dangerous&#039;"
                   , "Us&#039;:", "&#039;Her", "Peshawar", "Pakistan", "dying", "Lebanon", "html><html",
                   'lang="en"><head><meta', 'charset="utf-8"/><meta', 'content="width=device-width,',
                   "initial-scale=1.0,", "maximum-scale=2.0,", 'user-scalable=yes"',
                   "\xd0\xa1\xd1\x82\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x80\xd1\x82",
                   "\xd0\x9d\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xbd\xd0\xb8,", "\xd0\xba\xd0\xbe\xd0\xb8\xd1\x82\xd0\xbe",
"900,000&#x20;Syrians&#x20;take&#x20;refuge&#x20;in&#x20;Turkey,&#x20;says&#x20;UNICEF&#x20;&#x20;-&#x20;France&#x20;24",
                   "UN", "close", "cutting", "route", "U.N.,", "Urge", "\xe2\x80\x94", "\tFour", "These", "Of", "Human",
                    "Resiliency", "An", "KCBA", "Fox", "35", "&#8211;", "/", "Square","Times", "VICE", "dont", "get",
                   "too", ".html", "Songs", "Song"]



# [u'Christmas', u'Island', u'worse', u'than', u'Jordan', u'refugee', u'camp']
t = [u'Christmas', u'Island', u'worse', u'than', u'Jordan', u'refugee', u'camp']

# twitter_search_(searchWords, "ff")  ## FOR TESTING PURPOSES


#...................................  DOWNLOAD GDELT ARCHRIVE FILES  ............................... #
"""
N = 1830  # NUMBER OF DAYS TO GO BACK TO PREVIOUS YEAR #
date_N_days_ago = datetime.now() - timedelta(days=N)
sart_dat = datetime.now()
end_date = date_N_days_ago
# sart_dat = datetime.now().strftime('%Y%m%d')+"export.CSV.zip"
end_date = date_N_days_ago.strftime('%Y%m')+".zip"
url= req.urlopen(u"http://data.gdeltproject.org/events/index.html")
byte_ = end_date.encode(encoding='UTF-8')
counter = 0
    for html in url.readlines():
        link = re.findall(b'<A HREF="?\'?([^"\'>]*)', html)

        if link != [] and link[0] != b"md5sums" and link[0] != b"filesizes" and \
                        link[0] != b"GDELT.MASTERREDUCEDV2.1979-2013.zip":
            if counter > 640 and counter <= 1222:
                download_file_lnk = b"http://data.gdeltproject.org/events/" + link[0]
                # print(link[0], counter)
                download_file_lnk_conv = download_file_lnk.decode(encoding='UTF-8')
                file_name = req.urlopen(download_file_lnk_conv)
                response = file_name.read()

                with open(b"Gdelt_Files__\\"+link[0], 'wb') as f:
                    f.write(response)
                f.close()
                print(link[0] + b"FILE DOWNLOADED ..");
            counter += 1
    print("DOWNLOADING COMPLETED ... ")
"""
#.................................................................................................... #

#................................. START CRAWLING ................................................... #
def crawl():
    dirs = os.listdir("Gdelt_Files__")
    for file in dirs:
        zf = z.ZipFile("Gdelt_Files__\\"+file)
        getCSV_File = zf.namelist()[0]
        content = zf.read(getCSV_File, "r").split(" ")

        for event_data in content:
            if "SYR" in event_data and "REF" in event_data:
                urls = re.findall('http(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', event_data)

                if urls != []:
                    if re.match(r'^((http://)|(https://)).*?[Rre]fuge.*', urls[0]):
                        article = Article(urls[0])
                        article.download()
                        article.parse()

                        twitt_key = re.findall('text=(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]'
                        '|(?:%[0-9a-fA-F][0-9a-fA-F]))+', article.html)

                        if twitt_key != []:
                               # print("PASS IT")
                               if "%27beirut,%20lb%27%29&format=" not in twitt_key[0] \
                                    and "+encodeURI(document.title)" not in twitt_key[0] \
                                    and "+getShareTitle()" not in twitt_key[0] \
                                    and "a;a=document.getElementsByTagName('" not in twitt_key[0] \
                                    and "My+Profile" not in twitt_key[0] and "The" not in twitt_key[0] \
                                    and "UN" not in twitt_key[0] and ";" not in twitt_key[0] \
                                    and "$" not in twitt_key[0]:
                                    twitter_query = twitt_key[0].split("=")[1]


                                    if "&" in twitter_query:
                                        modify_ = urllib.unquote(twitter_query).decode('utf-8', 'ignore').split("&")[0]
                                        modify_ = modify_.replace("+", " ")

                                        # if "http" in modify_:
                                            # print("URL .... ")

                                        if "http" not in modify_ and "$" not in modify_ and "%" not in modify_:
                                            keys_ = modify_.split(" ")
                                            print("PROCESSING ... "+file)
                                            print("--------------------- IF PART KEYS -------------------------------")

                                            for words in keys_:
                                                if words not in skip_words_list:
                                                    if "'" in words:
                                                        words = words.replace("'", "")
                                                        if words not in skip_words_list:
                                                            searchWords.append(words)
                                                    else:
                                                        searchWords.append(words)
                                            twitter_search_(searchWords, file)

                                            # tc._twitter_api(searchWords, file)
                                            # clearArr(searchWords)

                                            print("------------------------------------------------------------------")

                                    else:
                                        modify_ = urllib2.unquote(twitter_query).decode('utf-8', 'ignore')
                                        # if "http" in modify_:
                                            # print("URL .... ")

                                        if "http" not in modify_ and "$" not in modify_ and "%" not in modify_:
                                            keysELSE_ = modify_.split(" ")
                                            print("PROCESSING ... "+file)
                                            print("--------------------- ELSE PART KEYS ---------------------------")

                                            for wordsE in keysELSE_:
                                                if wordsE not in skip_words_list:
                                                    if "'" in wordsE:
                                                        wordsE = wordsE.replace("'", "")
                                                        if wordsE not in skip_words_list:
                                                            searchWords.append(wordsE)
                                                    else:
                                                        searchWords.append(wordsE)
                                            twitter_search_(searchWords, file)
                                            print("---------------------------------------------------------------")

                        else:  # THIS SECTION IS FOR THOSE PAGE WHICH DON'T HAS ANY TWITTER BUTTON
                            if re.match(r'^((http://)|(https://)).*?[Ss]yria.*', urls[0]):
                                try:
                                    response = urllib2.urlopen(urls[0], timeout=5)
                                    html = response.read()
                                    begin = html.find('<title>')
                                    end   = html.find('</title>')
                                    title = html[begin+len('<title>'):end].strip()
                                    title_keys_ = title.split(" ")
                                    countwords = 0

                                    if "permission" in title_keys_ and "access" in title_keys_:
                                        print("URL ERROR ... ")

                                    else:
                                        for err_word in url_err:
                                            if "yria" in err_word:
                                                err_word = err_word.split("-")
                                                if err_word not in skip_words_list:
                                                    searchWords.append(err_word)
                                        twitter_search_(searchWords, file)

                                except (urllib2.URLError) as e:
                                    print "Oops, timed out?"
                                    url_err =  urls[0].split("/")

                                    for err_word in url_err:
                                        if "yria" in err_word:
                                            err_word = err_word.split("-")
                                            if err_word not in skip_words_list:
                                                searchWords.append(err_word)
                                    twitter_search_(searchWords, file)

                                except socket.timeout:
                                    print "socket timeout"
        print("FILE PROCESSED -------------------------------------------------------------> " + file)
#.................................................................................................................... #
# crawl()
