__author__ = 'Soumen'

import re
import urllib2 as req
from datetime import timedelta
from datetime import datetime

def gdeltDownloader():

        #...................................  DOWNLOAD GDELT ARCHRIVE FILES  ............................... #
        N = 2260  # NUMBER OF DAYS TO GO BACK TO PREVIOUS YEAR #
        date_N_days_ago = datetime.now() - timedelta(days=N)
        sart_dat = datetime.now()
        end_date = date_N_days_ago
        # sart_dat = datetime.now().strftime('%Y%m%d')+"export.CSV.zip"
        end_date = date_N_days_ago.strftime('%Y%m')+".zip"
        url= req.urlopen(u"http://data.gdeltproject.org/events/index.html")
        byte_ = end_date.encode(encoding='UTF-8')
        counter = 0

        start_date = (str(sart_dat.year)+str(sart_dat.month)+"0"+str(sart_dat.day - 2) +  ".export.CSV.zip")

        for html in url.readlines():
            link = re.findall(b'<A HREF="?\'?([^"\'>]*)', html)
            if link != [] and link[0] != b"md5sums" and link[0] != b"filesizes" and \
                            link[0] != b"GDELT.MASTERREDUCEDV2.1979-2013.zip":
                #print(link[0], " --- ", counter)

                if end_date == link[0]:
                     break
                else:
                    if counter >= 1425:
                        download_file_lnk = b"http://data.gdeltproject.org/events/" + link[0]
                        #download_file_lnk_conv = download_file_lnk.decode(encoding='UTF-8')
                        #file_name = req.urlopen(download_file_lnk_conv)
                        #response = file_name.read()
                        #with open(b"Gdelt_Files__\\"+link[0], 'wb') as f:
                            #f.write(response)
                        #f.close()

                        print(link[0] + b"FILE DOWNLOADED .." + str(counter))
                counter += 1
        print("DOWNLOADING COMPLETED ... ")
        #.................................................................................................... #
