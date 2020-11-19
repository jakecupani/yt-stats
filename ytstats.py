import requests

def getStats(channel_name):

  def getSubs(html):
    subs_index = html.find('subscriberCountText')
    subs_text = html[subs_index+36:subs_index+90]
    subs = subs_text[:subs_text.find("subscribers")-1]
    return subs

  def getViews(html):
    views_index = html.find("viewCountText")
    views_text = html[views_index+30:views_index+50]
    views = views_text[:views_text.find("views")-1]
    return views

  def getHTML(url):
    r = requests.get(url)
    if r.status_code != 200:
      return "Error: Invalid Channel Name"

    return r.text
  
  channel_url = "https://www.youtube.com/" + channel_name + "/about"
  channel_html = getHTML(channel_url)

  if channel_html == "Error: Invalid Channel Name":
    print("Error: Invalid Channel Name")
  else:
    print(channel_name + " has " + getSubs(channel_html) + " subscribers and " + getViews(channel_html) + " channel views.")

username = input("Enter username: ")
getStats(username)

