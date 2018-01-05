from .models import PostModel
from .fetch import HackerNewsClient


class HNCrawler(object):

    def __init__(self):
        self.crawl = False
        if not PostModel.objects.all().exists():
            self.hn = HackerNewsClient()
            self.crawl = True

    def get_top(self):
        if self.crawl:
            top_id = self.hn.get_top_stories()
            for i in range(0, 5):
                story = self.get_story(top_id[i])
                PostModel.objects.create(title=story['title'], url=story['url'])
        return PostModel.objects.all()

    def get_story(self, id):
        return self.hn.get_story(id)
