import feedparser, urllib2

d = feedparser.parse('http://squid-knits.blogspot.com/feeds/posts/default')

links = [x['link'] for x in d.entries]
print links

#entries = [urllib2.urlopen(x).read() for x in links]
#print entries[0]

entry = urllib2.urlopen(links[0]).read()
print entry

