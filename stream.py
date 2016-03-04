# This works great for any team's stream you want.
def stream(team):
    import praw
    import re
    r= praw.Reddit(user_agent = "Finding streams for football matches")
    subreddit = r.get_subreddit('soccerstreams')

    for submission in subreddit.get_hot() :
        thread_list = submission.title
        post_list = thread_list.split(" ")

        if team.lower() in (i.lower() for i in post_list):
            post_id = submission.id
            comments = submission.comments

            for x in comments:
                comments_text = x.body
                comments_text_list = comments_text.split(" ")

                for y in comments_text_list:
                    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',y)

                    for m in urls:
                        print (m)
                        return m
        else:
            return "Sorry not available"

