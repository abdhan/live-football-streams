# This works great for any team's stream you want.
def stream(team):
    import praw
    import re
    r= praw.Reddit(user_agent = "Finding streams for football matches")
    print("getting the subreddit")
    subreddit = r.get_subreddit('soccerstreams')
    print("got the subreddit")
    l=[]

    for submission in subreddit.get_hot() :
        thread_list = submission.title
        #post_list = thread_list.split(" ")
        #if team in (i.lower() for i in post_list):
        if team.lower() in thread_list.lower():
            print("looking for liverpool")
            print ("\n" , thread_list)
            post_id = submission.id
            print ("\n" , post_id)
            comments = submission.comments
            for x in comments:
                comments_text = x.body
                comments_text_list = comments_text.split(" ")
                for y in comments_text_list:
                    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',y)
                    for m in urls:
                        l.append(m)
    print (l)
    return l

