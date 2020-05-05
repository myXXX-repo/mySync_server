from mySync.apps.Git import init_app_Git
from mySync.apps.Main import init_app_Main
from mySync.apps.Markdown import init_app_Markdown
from mySync.apps.Sticky import init_app_Sticky
from mySync.apps.VisitCounter import init_app_VisitCounter
from mySync.apps.ApplicationData import init_app_ApplicationData


def init_app(server):
    init_app_Git(server)
    init_app_Main(server)
    init_app_Markdown(server)
    init_app_Sticky(server)
    # init_app_VisitCounter(server)
    init_app_ApplicationData(server)
    return server
