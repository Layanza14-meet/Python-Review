def create_youtube_video (title,description):

	title=input("the title is:")
	description=input("the description is:")
	



	video={"title":title,"description":description,"likes":0, "dislikes":0,"comments":{}}

	return video


def like (video):
	if "likes" in video:
		video["likes"]+=1
		return video

def like (video):
	if "dislikes" in video:
		video["dislikes"]+=1
		return video


def add_comment(youtubevideo,username,comment_text):

     youtubevideo["comments"][username]=comment_text


     return youtubevideo



newvid=create_youtube_video("loveme","a song offerd to the fans ")
for i in range(496):
	like(newvid)
print(newvid)

























	    





		
