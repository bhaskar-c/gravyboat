from django.conf.urls import url

from gravyboat.apps.promotions.conf import PROMOTION_CLASSES
from gravyboat.core.application import Application
from gravyboat.core.loading import get_class
from gravyboat.apps.dashboard.promotions.views import ListView as list_view
from gravyboat.apps.dashboard.promotions.views import PageListView as page_list
from gravyboat.apps.dashboard.promotions.views import PageDetailView as page_detail
from gravyboat.apps.dashboard.promotions.views import CreateRedirectView as create_redirect_view
from gravyboat.apps.dashboard.promotions.views import DeletePagePromotionView as delete_page_promotion_view


def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


class PromotionsDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    # Dynamically set the CRUD views for all promotion classes
    view_names = (
        ('create_%s_view', 'Create%sView'),
        ('update_%s_view', 'Update%sView'),
        ('delete_%s_view', 'Delete%sView')
    )
    for klass in PROMOTION_CLASSES:
        for attr_name, view_name in view_names:
            full_attr_name = attr_name % klass.classname()
            full_view_name = view_name % klass.__name__
            view = my_import('gravyboat.apps.dashboard.promotions.views.' + full_view_name)
            locals()[full_attr_name] = view
            # bhaskar you have commented the above two lines for now


    def get_urls(self):
        urls = [
            url(r'^$', list_view.as_view(), name='promotion-list'),
            url(r'^pages/$', page_list.as_view(),
                name='promotion-list-by-page'),
            url(r'^page/(?P<path>/([\w-]+(/[\w-]+)*/)?)$',
                page_detail.as_view(), name='promotion-list-by-url'),
            url(r'^create/$',
                create_redirect_view.as_view(),
                name='promotion-create-redirect'),
            url(r'^page-promotion/(?P<pk>\d+)/$',
                delete_page_promotion_view.as_view(),
                name='pagepromotion-delete')]

        for klass in PROMOTION_CLASSES:
            code = klass.classname()
            urls += [
                url(r'create/%s/' % code,
                    getattr(self, 'create_%s_view' % code).as_view(),
                    name='promotion-create-%s' % code),
                url(r'^update/(?P<ptype>%s)/(?P<pk>\d+)/$' % code,
                    getattr(self, 'update_%s_view' % code).as_view(),
                    name='promotion-update'),
                url(r'^delete/(?P<ptype>%s)/(?P<pk>\d+)/$' % code,
                    getattr(self, 'delete_%s_view' % code).as_view(),
                    name='promotion-delete')]

        return self.post_process_urls(urls)


application = PromotionsDashboardApplication()
