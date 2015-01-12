import urllib
import json as simplejson
import urllib2

def scan_url(scanurl):
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    parameters = {"url": scanurl, "apikey": "22d79a72dad85f0618d324115924c6021e8afe397595becbed506d0b70b6014c"}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    response_dict = simplejson.loads(json)
    return response_dict

def query_url(scanurl):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    parameters = {"resource": scanurl, "apikey": "22d79a72dad85f0618d324115924c6021e8afe397595becbed506d0b70b6014c"}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    response_dict = simplejson.loads(json)
    return response_dict

def format_url_report(result):
    scans = result.get("scans")
    print("Detection ratio: %s/%s" % (result['positives'], result['total']))
    print("Analysis date: %s" % result['scan_date'])
    print("-"*72)
    for k, v in scans.items():
        if v['detected'] == True:
            print ("%s: %s") % (k, v['result'])
        else:
            print ("%s: No Detection") % (k)
    print("-"*72)
    print("URL: %s" % result['url'])
    print("Permalink: %s" % result['permalink'])

def getRatio(result):
    ratio = float(float(result['positives'])/float(result['total']))
    return ratio

resUrlScan = scan_url("http://antalya.ru/")
resQueryScan = query_url(resUrlScan['scan_id'])
print getRatio(resQueryScan)

if resQueryScan!=None:
     format_url_report(resQueryScan)
else:
     print("There could be problem with the file.")
