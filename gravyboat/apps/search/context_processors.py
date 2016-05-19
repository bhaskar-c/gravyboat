from gravyboat.core.loading import get_class

from gravyboat.apps.search.forms import SearchForm



def search_form(request):
    """
    Ensure that the search form is available site wide
    """
    return {'search_form': SearchForm(request.GET)}
