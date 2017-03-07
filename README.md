#djdt-user-panel

Panel for the [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)
to easily and quickly switch between users.
 * View details on the currently logged in user.
 * Easily switch between recently logged in users.
 * Login as any user from an arbitrary email address, username or user ID.
 
#####Requirements

* Django 1.10
* Python 3.5
* Django Debug Toolbar 1.6

 
##Installation

Add ``djdt_user_panel`` to your ``INSTALLED_APPS``

    INSTALLED_APPS = (
    ...
        'djdt_user_panel',
        ...
    )
    
Add ``djdt_user_panel.panels.UserPanel`` to ``DEBUG_TOOLBAR_PANELS``

    DEBUG_TOOLBAR_PANELS = (
        'djdt_user_panel.panels.UserPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    )

You can disable any of the above panels you do not wish to show in the Debug Toolbar by removing them or commenting them out.

##Links
 Based on original code by [playfire](https://github.com/playfire/django-debug-toolbar-user-panel)