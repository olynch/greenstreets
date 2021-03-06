from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home
    url(r'^$', TemplateView.as_view(template_name='survey/index.html'), name='home'),
    # Commuterform
    url(r'^commuterform/$', 'survey.views.commuter', name='commuterform'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^grappelli/', include('grappelli.urls')),
    url(r'^leaderboard/$', 'leaderboard.views.leaderboard'),
    url(r'^leaderboard-bare/$', 'leaderboard.views.leaderboard_bare'),
    url(r'^test-chart/$', 'leaderboard.views.testchart'),
    url(r'^emplbreakdown/(?P<month>[-\w]+)/$', 'leaderboardlist.views.empBreakDown'),
    url(r'^emplbreakdown/$', 'leaderboardlist.views.chooseMonth'),
	url(r'^nvobreakdown/$', 'leaderboard.views.nvobreakdown'),
	url(r'^nvobreakdown/(?P<selEmpID>[-\w]+)/$', 'leaderboard.views.nvobreakdown'),
)

urlpatterns += staticfiles_urlpatterns()
