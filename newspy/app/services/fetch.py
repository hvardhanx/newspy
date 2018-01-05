from firebase import firebase

class HackerNewsClient(object):
    def __init__(self):
        self.firebase_app = firebase.FirebaseApplication('https://hacker-news.firebaseio.com', None)

    def get_top_stories(self):
        top_stories = self.firebase_app.get('/v0/topstories', None)
        return top_stories

    def get_best_stories(self):
        best_stories = self.firebase_app.get('/v0/beststories', None)
        return best_stories

    def get_story(self, id):
        story = self.firebase_app.get('/v0/item/{0}'.format(id), None)
        return story