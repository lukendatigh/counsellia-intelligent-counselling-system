from django.urls import path, include

from . import views as analysis_views
from . views import (
    ReportsPastView,
    ReportsArchivedView,
    display_charts,
)



urlpatterns = [
    path('past/', ReportsPastView.as_view(), name = 'reports-past'),
    path('archived/', ReportsArchivedView.as_view(), name = 'reports-archived'),
    path('twitter/', display_charts, name = 'analyze-twitter'),

]