import requests
import sys

def getStats(channel_name):

  # Gets the number of channel subscriptions
  def getSubs(html):
    subs_index = html.find('subscriberCountText')
    subs_text = html[subs_index+36:subs_index+90]
    subs = subs_text[:subs_text.find("subscribers")-1]
    return subs

  # Gets the number of total channel views
  def getViews(html):
    views_index = html.find("viewCountText")
    views_text = html[views_index+30:views_index+50]
    views = views_text[:views_text.find("views")-1]
    return views

  # Gets the raw HTML for the channel's About page
  def getHTML(url):
    r = requests.get(url)
    if r.status_code != 200:
      sys.exit("Invalid Username")
    return r.text
  
  channel_url = "https://www.youtube.com/" + channel_name + "/about"
  channel_html = getHTML(channel_url)

  print(channel_name + " has " + getSubs(channel_html) + " subscribers and " + getViews(channel_html) + " channel views.")

username = input("Enter username: ")
getStats(username)

