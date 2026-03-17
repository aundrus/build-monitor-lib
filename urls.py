"""
URL patterns for buildmonitor application
"""

from django.urls import re_path

# Import views for each page
from core.buildmonitor import viewsglobal as globalview  # Global build monitor view
from core.buildmonitor import viewsci as ciview         # CI build monitor view
from core.buildmonitor import viewsn as nview           # N build monitor view
from core.buildmonitor import viewstests as testsview   # Tests results view
from core.buildmonitor import viewscomps as compsview   # Components results view

# Define URL patterns for demo pages
urlpatterns = [
    re_path(r'^globalpage/$', globalview.globalviewDemo, name='BuildGlobal'),   # Global page
    re_path(r'^globalview/$', globalview.globalviewDemo, name='BuildGlobal'),   # Global view
    re_path(r'^ciview/$', ciview.civiewDemo, name='BuildCI'),                   # CI view
    re_path(r'^nview/$', nview.nviewDemo, name='BuildN'),                       # N view
    re_path(r'^testsview/$', testsview.testviewDemo, name='TestsRes'),          # Tests results view
    re_path(r'^compsview/$', compsview.compviewDemo, name='CompsRes'),          # Components results view
]