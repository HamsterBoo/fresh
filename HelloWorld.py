import praw
import urllib
import urllib2
import webbrowser
import sys
import re
import time

i_max = 5
r = praw.Reddit(user_agent="fresh_pics")

r.login("fresh_pics", "karmadecay")
ffsub = r.get_subreddit("fresh_pics")

submissions = r.get_subreddit('pics').get_hot(limit=i_max)
#urls = [str(x.url) for x in submissions]

url = "http://karmadecay.com"
#req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
#con = urllib2.urlopen(req)
#print con.read()


"""
search = r.search("http://i.imgur.com/LxauLP0.gif", limit=None)
#search = r.search("http://imgur.com/mBYNCOn", limit=None)

try:
	results = [str(x) for x in search]
except praw.errors.RedirectException as e:
	target = re.search(" to (.*)$", str(e)).group(1)
	
	print "broken"

	#page = r.get_content(target)
	#print [str(x) for x in page]

	#sys.exit()
	#req = urllib2.Request(target)
	#con = urllib2.urlopen(req)
	#contents = con.read()
	#rint contents.find("submit to reddit")

	#print str(e).find("reddit.com/submit")
sys.exit()

"""

with open("pics_posted.txt", 'r') as f:
	post_list = f.read()

with open("pics_posted.txt", "a") as f:
	for sub in submissions:
		print sub.id
		#print sub.short_link

		#print post_list
		#sys.exit()
		
		#temporary, in future use reddit search (once praw is updated)
		if post_list.find(sub.id) != -1:
			continue
	
		data = urllib.urlencode({'url': sub.url})
		req = urllib2.Request(url, data, headers={'User-Agent' : "Magic Browser"})
		con = urllib2.urlopen(req)
		contents = con.read()
	
		new = contents.find("No very similar images were found") != -1
		image = contents.find("Unable to find an image") == -1
	
		f.write(sub.id+'\n')
		if new and image:
			print "OC!"
			try:
				subbed = r.submit(ffsub, sub.title, url=sub.url)
				subbed.add_comment('[Original post]('+sub.short_link+')')
				time.sleep(4)
			except praw.errors.AlreadySubmitted:
				print "Already submitted"
				time.sleep(2)

			
			#input("Press Enter to continue...")
