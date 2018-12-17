import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movTitle, movieStoryline, posterImg, trailerYouTube):
    	# initialize instance of class Movie, I changed the input variable names, but the instance variables are the same as used in the fresh_tomatoes file
    	self.title=movTitle
    	self.storyline=movieStoryline
    	self.poster_image_url=posterImg
    	self.trailer_youtube_url=trailerYouTube
        
    def show_trailer(self):
    	# displays the trailer when the poster is clicked on, this is called from the fresh_tomatoes file
    	webbrowser.open(self.trailer_youtube_url)
