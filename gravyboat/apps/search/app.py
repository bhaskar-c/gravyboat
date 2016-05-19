from django.conf.urls import url
from haystack.views import search_view_factory

from gravyboat.apps.search import facets
from gravyboat.core.application import Application
from gravyboat.core.loading import get_class

from gravyboat.apps.search.views import FacetedSearchView as search_view
from gravyboat.apps.search.forms import SearchForm as search_form

class SearchApplication(Application):
    name = 'search'

    def get_urls(self):

        # The form class has to be passed to the __init__ method as that is how
        # Haystack works.  It's slightly different to normal CBVs.
        urlpatterns = [
            url(r'^$', search_view_factory(
                view_class=search_view,
                form_class=search_form,
                searchqueryset=self.get_sqs()),
                name='search'),
        ]
        return self.post_process_urls(urlpatterns)

    def get_sqs(self):
        """
        Return the SQS required by a the Haystack search view
        """
        return facets.base_sqs()


application = SearchApplication()
