class PrivacySuggestionApp:
    def __init__(self):
        self.suggestions = {
            'discord': 'Use Element or Session (both open-source).',
            'google chrome': 'Consider using Mozilla Firefox (open-source).',
            'whatsapp': 'Try Signal (open-source).',
            'instagram': 'Consider using Pixelfed or Mastodon (both open-source).',
            'facebook': 'Try MeWe or Minds (both open-source).',
            'zoom': 'Use Jitsi Meet (open-source).',
            'linkedin': 'Consider using ProtonMail (open-source).',
            'snapchat': 'Try Signal (open-source) or Telegram (open-source).',
            'twitter': 'Consider using Mastodon (open-source).',
            'spotify': 'Use Audacity (open-source) or Deezer.',
            'unity': 'Use Godot (open-source).',
            'adobe photoshop': 'Use GIMP (open-source).',
            'slack': 'Use Mattermost (open-source).',
            'windows media player': 'Use VLC (open-source).',
            'grammarly': 'Use LanguageTool (open-source).',
            'youtube': 'Use PeerTube (open-source).',
            'lastpass': 'Use Bitwarden (open-source).',
            'windows': 'Consider using Linux Mint (open-source).',
            # Add more app suggestions here
            'chrome': 'Consider using Brave (open-source) or Firefox (open-source).',
            'skype': 'Use Jitsi Meet (open-source) or Signal (open-source).',
            'microsoft office': 'Use LibreOffice (open-source) or OnlyOffice (open-source).',
            'dropbox': 'Use Nextcloud (open-source) or Sync (open-source).',
            'google drive': 'Use Nextcloud (open-source) or Tresorit.',
            'evernote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'teamviewer': 'Use AnyDesk (open-source) or Chrome Remote Desktop.',
            'viber': 'Try Signal (open-source) or Telegram (open-source).',
            'telegram': 'Consider using Signal (open-source).',
            'apple music': 'Use Spotify or Deezer.',
            'itunes': 'Use foobar2000 (open-source) or MusicBee (open-source).',
            'outlook': 'Use ProtonMail (open-source) or Tutanota (open-source).',
            'gmail': 'Consider using ProtonMail (open-source) or Tutanota (open-source).',
            'adobe illustrator': 'Use Inkscape (open-source).',
            'premiere pro': 'Use DaVinci Resolve (open-source) or Shotcut (open-source).',
            'zoom': 'Use Jitsi Meet (open-source) or Microsoft Teams.',
            'microsoft teams': 'Use Zoom (open-source) or Jitsi Meet (open-source).',
            'snapchat': 'Try Signal (open-source) or Telegram (open-source).',
            'tiktok': 'Consider using Triller or Dubsmash.',
            'whatsapp': 'Try Signal (open-source) or Telegram (open-source).',
            'wechat': 'Consider using Signal (open-source) or Line.',
            'signal': 'Consider using Telegram (open-source).',
            'google maps': 'Use OpenStreetMap (open-source) or MapQuest.',
            'apple maps': 'Use OpenStreetMap (open-source) or MapQuest.',
            'netflix': 'Use Hulu or Popcorn Time (open-source).',
            'hulu': 'Use Popcorn Time (open-source) or Stremio (open-source).',
            'popcorn time': 'Use Stremio (open-source) or Kodi (open-source).',
            'stremio': 'Use Kodi (open-source) or Jellyfin (open-source).',
            'kodi': 'Use Jellyfin (open-source) or Plex (open-source).',
            'jellyfin': 'Use Plex (open-source) or Emby (open-source).',
            'plex': 'Use Emby (open-source) or Infuse (open-source).',
            'infuse': 'Use Kodi (open-source) or Jellyfin (open-source).',
            'photoshop express': 'Use Snapseed or Pixlr.',
            'snapseed': 'Consider using Photoshop Express or Pixlr.',
            'pixlr': 'Use Photoshop Express or Snapseed.',
            'adobe premiere rush': 'Use Kinemaster or InShot.',
            'kinemaster': 'Consider using Adobe Premiere Rush or InShot.',
            'inshot': 'Use Adobe Premiere Rush or Kinemaster.',
            'microsoft edge': 'Consider using Mozilla Firefox (open-source) or Brave (open-source).',
            'brave': 'Consider using Mozilla Firefox (open-source) or Microsoft Edge (open-source).',
            'opera': 'Consider using Mozilla Firefox (open-source) or Brave (open-source).',
            'firefox focus': 'Use Brave (open-source) or DuckDuckGo Privacy Browser (open-source).',
            'duckduckgo privacy browser': 'Use Brave (open-source) or Firefox Focus (open-source).',
            'chromebook': 'Consider using Linux (open-source) or Windows laptop.',
            'android': 'Consider using LineageOS (open-source).',
            'ios': 'Consider using LineageOS (open-source).',
            'lineageos': 'Consider using Android (open-source).',
            'vscode': 'Use Atom (open-source) or Sublime Text.',
            'atom': 'Use Visual Studio Code (open-source) or Sublime Text.',
            'sublime text': 'Use Visual Studio Code (open-source) or Atom.',
            'android studio': 'Use Eclipse (open-source) or IntelliJ IDEA.',
            'eclipse': 'Use Android Studio (open-source) or IntelliJ IDEA.',
            'intellij idea': 'Use Android Studio (open-source) or Eclipse.',
            'notion': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'obs studio': 'Use Streamlabs OBS (open-source) or XSplit.',
            'streamlabs obs': 'Use OBS Studio (open-source) or XSplit.',
            'xsplit': 'Use OBS Studio (open-source) or Streamlabs OBS (open-source).',
            'postman': 'Use Insomnia (open-source) or Paw.',
            'insomnia': 'Use Postman (open-source) or Paw.',
            'paw': 'Use Postman (open-source) or Insomnia.',
            'vmware': 'Use VirtualBox (open-source) or QEMU.',
            'virtualbox': 'Use VMware (open-source) or QEMU.',
            'qemu': 'Use VirtualBox (open-source) or VMware.',
            'evernote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'slack': 'Use Mattermost (open-source) or Rocket.Chat (open-source).',
            'mattermost': 'Use Slack (open-source) or Rocket.Chat (open-source).',
            'rocket.chat': 'Use Slack (open-source) or Mattermost (open-source).',
            'trello': 'Use Wekan (open-source) or Taiga.',
            'wekan': 'Use Trello (open-source) or Taiga.',
            'taiga': 'Use Trello (open-source) or Wekan.',
            'microsoft word': 'Use LibreOffice Writer (open-source) or OnlyOffice (open-source).',
            'libreoffice writer': 'Use Microsoft Word (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft Word (open-source) or LibreOffice Writer (open-source).',
            'microsoft excel': 'Use LibreOffice Calc (open-source) or OnlyOffice (open-source).',
            'libreoffice calc': 'Use Microsoft Excel (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft Excel (open-source) or LibreOffice Calc (open-source).',
            'microsoft powerpoint': 'Use LibreOffice Impress (open-source) or OnlyOffice (open-source).',
            'libreoffice impress': 'Use Microsoft PowerPoint (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft PowerPoint (open-source) or LibreOffice Impress (open-source).',
            'gimp': 'Use Krita or Photopea (open-source).',
            'krita': 'Use GIMP or Photopea (open-source).',
            'photopea': 'Use GIMP or Krita (open-source).',
            'corel videostudio': 'Use Shotcut or DaVinci Resolve (open-source).',
            'shotcut': 'Use DaVinci Resolve (open-source) or Olive (open-source).',
            'davinci resolve': 'Use Shotcut (open-source) or Olive (open-source).',
            'olive': 'Use Shotcut (open-source) or DaVinci Resolve (open-source).',
            'lightroom': 'Use Darktable or RawTherapee (open-source).',
            'darktable': 'Use Lightroom or RawTherapee (open-source).',
            'rawtherapee': 'Use Lightroom or Darktable (open-source).',
            'microsoft visio': 'Use Draw.io (open-source) or LibreOffice Draw (open-source).',
            'draw.io': 'Use Microsoft Visio (open-source) or LibreOffice Draw (open-source).',
            'libreoffice draw': 'Use Microsoft Visio (open-source) or Draw.io (open-source).',
            'autocad': 'Use FreeCAD or LibreCAD (open-source).',
            'freecad': 'Use AutoCAD or LibreCAD (open-source).',
            'librecad': 'Use AutoCAD or FreeCAD (open-source).',
            'adobe after effects': 'Use Natron (open-source) or HitFilm Express.',
            'natron': 'Use Adobe After Effects or HitFilm Express.',
            'hitfilm express': 'Use Adobe After Effects or Natron (open-source).',
            'android auto': 'Use OpenAuto or Raspotify (open-source).',
            'openauto': 'Use Android Auto or Raspotify (open-source).',
            'raspotify': 'Use Android Auto or OpenAuto (open-source).',
            'adobe lightroom': 'Use Darktable or RawTherapee (open-source).',
            'avidemux': 'Use Shotcut or Olive (open-source).',
            'cubase': 'Use Ardour (open-source) or Tracktion.',
            'ardour': 'Use Cubase or Tracktion.',
            'tracktion': 'Use Cubase or Ardour (open-source).',
            'fl studio': 'Use LMMS (open-source) or Ardour (open-source).',
            'lmms': 'Use FL Studio or Ardour (open-source).',
            'reaper': 'Use Ardour (open-source) or Tracktion.',
            'notion': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'obs studio': 'Use Streamlabs OBS (open-source) or XSplit.',
            'streamlabs obs': 'Use OBS Studio (open-source) or XSplit.',
            'xsplit': 'Use OBS Studio (open-source) or Streamlabs OBS (open-source).',
            'postman': 'Use Insomnia (open-source) or Paw.',
            'insomnia': 'Use Postman (open-source) or Paw.',
            'paw': 'Use Postman (open-source) or Insomnia.',
            'vmware': 'Use VirtualBox (open-source) or QEMU.',
            'virtualbox': 'Use VMware (open-source) or QEMU.',
            'qemu': 'Use VirtualBox (open-source) or VMware.',
            'evernote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'slack': 'Use Mattermost (open-source) or Rocket.Chat (open-source).',
            'mattermost': 'Use Slack (open-source) or Rocket.Chat (open-source).',
            'rocket.chat': 'Use Slack (open-source) or Mattermost (open-source).',
            'trello': 'Use Wekan (open-source) or Taiga.',
            'wekan': 'Use Trello (open-source) or Taiga.',
            'taiga': 'Use Trello (open-source) or Wekan.',
            'microsoft word': 'Use LibreOffice Writer (open-source) or OnlyOffice (open-source).',
            'libreoffice writer': 'Use Microsoft Word (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft Word (open-source) or LibreOffice Writer (open-source).',
            'microsoft excel': 'Use LibreOffice Calc (open-source) or OnlyOffice (open-source).',
            'libreoffice calc': 'Use Microsoft Excel (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft Excel (open-source) or LibreOffice Calc (open-source).',
            'microsoft powerpoint': 'Use LibreOffice Impress (open-source) or OnlyOffice (open-source).',
            'libreoffice impress': 'Use Microsoft PowerPoint (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft PowerPoint (open-source) or LibreOffice Impress (open-source).',
            'blender': 'Use Autodesk Maya or Cinema 4D.',
            'autodesk maya': 'Use Blender or Cinema 4D.',
            'cinema 4d': 'Use Blender or Autodesk Maya.',
            'coreldraw': 'Use Inkscape (open-source) or Scribus (open-source).',
            'inkscape': 'Use CorelDRAW or Scribus (open-source).',
            'scribus': 'Use CorelDRAW or Inkscape (open-source).',
            'onenote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'joplin': 'Use OneNote or Standard Notes (open-source).',
            'standard notes': 'Use OneNote or Joplin (open-source).',
            'zotero': 'Use Mendeley or EndNote.',
            'mendeley': 'Use Zotero or EndNote.',
            'endnote': 'Use Zotero or Mendeley.',
            'matlab': 'Use Octave (open-source) or Scilab (open-source).',
            'octave': 'Use MATLAB or Scilab (open-source).',
            'scilab': 'Use MATLAB or Octave (open-source).',
            'openoffice': 'Use LibreOffice (open-source) or Microsoft Office.',
            'libreoffice': 'Use OpenOffice or Microsoft Office.',
            'microsoft office': 'Use OpenOffice or LibreOffice (open-source).',
            'opencpn': 'Use SeaClear or Polar Navy.',
            'seaclear': 'Use OpenCPN or Polar Navy.',
            'polar navy': 'Use OpenCPN or SeaClear.',
            'jira': 'Use Trello or Asana.',
            'trello': 'Use Jira or Asana.',
            'asana': 'Use Jira or Trello.',
            'bitbucket': 'Use GitLab (open-source) or GitHub.',
            'gitlab': 'Use Bitbucket or GitHub.',
            'github': 'Use Bitbucket or GitLab (open-source).',
            'notepad++': 'Use Visual Studio Code (open-source) or Atom.',
            'visual studio code': 'Use Notepad++ or Atom.',
            'atom': 'Use Notepad++ or Visual Studio Code (open-source).',
            'picasa': 'Use digiKam (open-source) or Shotwell (open-source).',
            'digikam': 'Use Picasa or Shotwell (open-source).',
            'shotwell': 'Use Picasa or digiKam (open-source).',
            'gimp': 'Use Krita or Photopea (open-source).',
            'krita': 'Use GIMP or Photopea (open-source).',
            'photopea': 'Use GIMP or Krita (open-source).',
            'corel videostudio': 'Use Shotcut or DaVinci Resolve (open-source).',
            'shotcut': 'Use DaVinci Resolve (open-source) or Olive (open-source).',
            'davinci resolve': 'Use Shotcut (open-source) or Olive (open-source).',
            'olive': 'Use Shotcut (open-source) or DaVinci Resolve (open-source).',
            'lightroom': 'Use Darktable or RawTherapee (open-source).',
            'darktable': 'Use Lightroom or RawTherapee (open-source).',
            'rawtherapee': 'Use Lightroom or Darktable (open-source).',
            'microsoft visio': 'Use Draw.io (open-source) or LibreOffice Draw (open-source).',
            'draw.io': 'Use Microsoft Visio (open-source) or LibreOffice Draw (open-source).',
            'libreoffice draw': 'Use Microsoft Visio (open-source) or Draw.io (open-source).',
            'autocad': 'Use FreeCAD or LibreCAD (open-source).',
            'freecad': 'Use AutoCAD or LibreCAD (open-source).',
            'librecad': 'Use AutoCAD or FreeCAD (open-source).',
            'adobe after effects': 'Use Natron (open-source) or HitFilm Express.',
            'natron': 'Use Adobe After Effects or HitFilm Express.',
            'hitfilm express': 'Use Adobe After Effects or Natron (open-source).',
            'android auto': 'Use OpenAuto or Raspotify (open-source).',
            'openauto': 'Use Android Auto or Raspotify (open-source).',
            'raspotify': 'Use Android Auto or OpenAuto (open-source).',
            'adobe lightroom': 'Use Darktable or RawTherapee (open-source).',
            'avidemux': 'Use Shotcut or Olive (open-source).',
            'cubase': 'Use Ardour (open-source) or Tracktion.',
            'ardour': 'Use Cubase or Tracktion.',
            'tracktion': 'Use Cubase or Ardour (open-source).',
            'fl studio': 'Use LMMS (open-source) or Ardour (open-source).',
            'lmms': 'Use FL Studio or Ardour (open-source).',
            'reaper': 'Use Ardour (open-source) or Tracktion.',
            'natron': 'Use Adobe After Effects or HitFilm Express.',
            'hitfilm express': 'Use Adobe After Effects or Natron (open-source).',
            'android auto': 'Use OpenAuto or Raspotify (open-source).',
            'openauto': 'Use Android Auto or Raspotify (open-source).',
            'raspotify': 'Use Android Auto or OpenAuto (open-source).',
            'adobe lightroom': 'Use Darktable or RawTherapee (open-source).',
            'avidemux': 'Use Shotcut or Olive (open-source).',
            'cubase': 'Use Ardour (open-source) or Tracktion.',
            'ardour': 'Use Cubase or Tracktion.',
            'tracktion': 'Use Cubase or Ardour (open-source).',
            'fl studio': 'Use LMMS (open-source) or Ardour (open-source).',
            'lmms': 'Use FL Studio or Ardour (open-source).',
            'reaper': 'Use Ardour (open-source) or Tracktion.',
            'blender': 'Use Autodesk Maya or Cinema 4D.',
            'autodesk maya': 'Use Blender or Cinema 4D.',
            'cinema 4d': 'Use Blender or Autodesk Maya.',
            'coreldraw': 'Use Inkscape (open-source) or Scribus (open-source).',
            'inkscape': 'Use CorelDRAW or Scribus (open-source).',
            'scribus': 'Use CorelDRAW or Inkscape (open-source).',
            'onenote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'joplin': 'Use OneNote or Standard Notes (open-source).',
            'standard notes': 'Use OneNote or Joplin (open-source).',
            'zotero': 'Use Mendeley or EndNote.',
            'mendeley': 'Use Zotero or EndNote.',
            'endnote': 'Use Zotero or Mendeley.',
            'matlab': 'Use Octave (open-source) or Scilab (open-source).',
            'octave': 'Use MATLAB or Scilab (open-source).',
            'scilab': 'Use MATLAB or Octave (open-source).',
            'openoffice': 'Use LibreOffice (open-source) or Microsoft Office.',
            'libreoffice': 'Use OpenOffice or Microsoft Office.',
            'microsoft office': 'Use OpenOffice or LibreOffice (open-source).',
            'opencpn': 'Use SeaClear or Polar Navy.',
            'seaclear': 'Use OpenCPN or Polar Navy.',
            'polar navy': 'Use OpenCPN or SeaClear.',
            'jira': 'Use Trello or Asana.',
            'trello': 'Use Jira or Asana.',
            'asana': 'Use Jira or Trello.',
            'bitbucket': 'Use GitLab (open-source) or GitHub.',
            'gitlab': 'Use Bitbucket or GitHub.',
            'github': 'Use Bitbucket or GitLab (open-source).',
            'notepad++': 'Use Visual Studio Code (open-source) or Atom.',
            'visual studio code': 'Use Notepad++ or Atom.',
            'atom': 'Use Notepad++ or Visual Studio Code (open-source).',
            'picasa': 'Use digiKam (open-source) or Shotwell (open-source).',
            'digikam': 'Use Picasa or Shotwell (open-source).',
            'shotwell': 'Use Picasa or digiKam (open-source).',
            'krita': 'Use GIMP or Photopea (open-source).',
            'photopea': 'Use GIMP or Krita (open-source).',
            'corel videostudio': 'Use Shotcut or DaVinci Resolve (open-source).',
            'shotcut': 'Use DaVinci Resolve (open-source) or Olive (open-source).',
            'davinci resolve': 'Use Shotcut (open-source) or Olive (open-source).',
            'olive': 'Use Shotcut (open-source) or DaVinci Resolve (open-source).',
            'lightroom': 'Use Darktable or RawTherapee (open-source).',
            'skype': 'Use Jitsi Meet (open-source) or Signal (open-source).',
            'microsoft office': 'Use LibreOffice (open-source) or OnlyOffice (open-source).',
            'dropbox': 'Use Nextcloud (open-source) or Sync (open-source).',
            'google drive': 'Use Nextcloud (open-source) or Tresorit.',
            'evernote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'teamviewer': 'Use AnyDesk (open-source) or Chrome Remote Desktop.',
            'viber': 'Try Signal (open-source) or Telegram (open-source).',
            'telegram': 'Consider using Signal (open-source).',
            'apple music': 'Use Spotify or Deezer.',
            'itunes': 'Use foobar2000 (open-source) or MusicBee (open-source).',
            'outlook': 'Use ProtonMail (open-source) or Tutanota (open-source).',
            'gmail': 'Consider using ProtonMail (open-source) or Tutanota (open-source).',
            'adobe illustrator': 'Use Inkscape (open-source).',
            'premiere pro': 'Use DaVinci Resolve (open-source) or Shotcut (open-source).',
            'zoom': 'Use Jitsi Meet (open-source) or Microsoft Teams.',
            'microsoft teams': 'Use Zoom (open-source) or Jitsi Meet (open-source).',
            'snapchat': 'Try Signal (open-source) or Telegram (open-source).',
            'tiktok': 'Consider using Triller or Dubsmash.',
            'whatsapp': 'Try Signal (open-source) or Telegram (open-source).',
            'wechat': 'Consider using Signal (open-source) or Line.',
            'signal': 'Consider using Telegram (open-source).',
            'google maps': 'Use OpenStreetMap (open-source) or MapQuest.',
            'apple maps': 'Use OpenStreetMap (open-source) or MapQuest.',
            'netflix': 'Use Hulu or Popcorn Time (open-source).',
            'hulu': 'Use Popcorn Time (open-source) or Stremio (open-source).',
            'popcorn time': 'Use Stremio (open-source) or Kodi (open-source).',
            'stremio': 'Use Kodi (open-source) or Jellyfin (open-source).',
            'kodi': 'Use Jellyfin (open-source) or Plex (open-source).',
            'jellyfin': 'Use Plex (open-source) or Emby (open-source).',
            'plex': 'Use Emby (open-source) or Infuse (open-source).',
            'infuse': 'Use Kodi (open-source) or Jellyfin (open-source).',
            'photoshop express': 'Use Snapseed or Pixlr.',
            'snapseed': 'Consider using Photoshop Express or Pixlr.',
            'pixlr': 'Use Photoshop Express or Snapseed.',
            'adobe premiere rush': 'Use Kinemaster or InShot.',
            'kinemaster': 'Consider using Adobe Premiere Rush or InShot.',
            'inshot': 'Use Adobe Premiere Rush or Kinemaster.',
            'microsoft edge': 'Consider using Mozilla Firefox (open-source) or Brave (open-source).',
            'brave': 'Consider using Mozilla Firefox (open-source) or Microsoft Edge (open-source).',
            'opera': 'Consider using Mozilla Firefox (open-source) or Brave (open-source).',
            'firefox focus': 'Use Brave (open-source) or DuckDuckGo Privacy Browser (open-source).',
            'duckduckgo privacy browser': 'Use Brave (open-source) or Firefox Focus (open-source).',
            'chromebook': 'Consider using Linux (open-source) or Windows laptop.',
            'android': 'Consider using LineageOS (open-source).',
            'ios': 'Consider using LineageOS (open-source).',
            'lineageos': 'Consider using Android (open-source).',
            'vscode': 'Use Atom (open-source) or Sublime Text.',
            'atom': 'Use Visual Studio Code (open-source) or Sublime Text.',
            'sublime text': 'Use Visual Studio Code (open-source) or Atom.',
            'android studio': 'Use Eclipse (open-source) or IntelliJ IDEA.',
            'eclipse': 'Use Android Studio (open-source) or IntelliJ IDEA.',
            'intellij idea': 'Use Android Studio (open-source) or Eclipse.',
            'notion': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'obs studio': 'Use Streamlabs OBS (open-source) or XSplit.',
            'streamlabs obs': 'Use OBS Studio (open-source) or XSplit.',
            'xsplit': 'Use OBS Studio (open-source) or Streamlabs OBS (open-source).',
            'postman': 'Use Insomnia (open-source) or Paw.',
            'insomnia': 'Use Postman (open-source) or Paw.',
            'paw': 'Use Postman (open-source) or Insomnia.',
            'vmware': 'Use VirtualBox (open-source) or QEMU.',
            'virtualbox': 'Use VMware (open-source) or QEMU.',
            'qemu': 'Use VirtualBox (open-source) or VMware.',
            'evernote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'slack': 'Use Mattermost (open-source) or Rocket.Chat (open-source).',
            'mattermost': 'Use Slack (open-source) or Rocket.Chat (open-source).',
            'rocket.chat': 'Use Slack (open-source) or Mattermost (open-source).',
            'trello': 'Use Wekan (open-source) or Taiga.',
            'wekan': 'Use Trello (open-source) or Taiga.',
            'taiga': 'Use Trello (open-source) or Wekan.',
            'microsoft word': 'Use LibreOffice Writer (open-source) or OnlyOffice (open-source).',
            'libreoffice writer': 'Use Microsoft Word (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft Word (open-source) or LibreOffice Writer (open-source).',
            'microsoft excel': 'Use LibreOffice Calc (open-source) or OnlyOffice (open-source).',
            'libreoffice calc': 'Use Microsoft Excel (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft Excel (open-source) or LibreOffice Calc (open-source).',
            'microsoft powerpoint': 'Use LibreOffice Impress (open-source) or OnlyOffice (open-source).',
            'libreoffice impress': 'Use Microsoft PowerPoint (open-source) or OnlyOffice (open-source).',
            'onlyoffice': 'Use Microsoft PowerPoint (open-source) or LibreOffice Impress (open-source).',
            'blender': 'Use Autodesk Maya or Cinema 4D.',
            'autodesk maya': 'Use Blender or Cinema 4D.',
            'cinema 4d': 'Use Blender or Autodesk Maya.',
            'coreldraw': 'Use Inkscape (open-source) or Scribus (open-source).',
            'inkscape': 'Use CorelDRAW or Scribus (open-source).',
            'scribus': 'Use CorelDRAW or Inkscape (open-source).',
            'onenote': 'Use Joplin (open-source) or Standard Notes (open-source).',
            'joplin': 'Use OneNote or Standard Notes (open-source).',
            'standard notes': 'Use OneNote or Joplin (open-source).',
            'zotero': 'Use Mendeley or EndNote.',
            'mendeley': 'Use Zotero or EndNote.',
            'endnote': 'Use Zotero or Mendeley.',
            'matlab': 'Use Octave (open-source) or Scilab (open-source).',
            'octave': 'Use MATLAB or Scilab (open-source).',
            'scilab': 'Use MATLAB or Octave (open-source).',
            'openoffice': 'Use LibreOffice (open-source) or Microsoft Office.',
            'libreoffice': 'Use OpenOffice or Microsoft Office.',
            'microsoft office': 'Use OpenOffice or LibreOffice (open-source).',
            'opencpn': 'Use SeaClear or Polar Navy.',
            'seaclear': 'Use OpenCPN or Polar Navy.',
            'polar navy': 'Use OpenCPN or SeaClear.',
            'jira': 'Use Trello or Asana.',
            'trello': 'Use Jira or Asana.',
            'google': 'Use DuckDuckGo or Searx.',
            'bitbucket': 'Use GitLab (open-source) or GitHub.',
            'gitlab': 'Use Bitbucket or GitHub.',
            'github': 'Use Bitbucket or GitLab (open-source).',
            'notepad++': 'Use Visual Studio Code (open-source) or Atom.',
            'visual studio code': 'Use Notepad++ or Atom.',
            'atom': 'Use Notepad++ or Visual Studio Code (open-source).',
            'picasa': 'Use digiKam (open-source) or Shotwell (open-source).',
            'digikam': 'Use Picasa or Shotwell (open-source).',
            'shotwell': 'Use Picasa or digiKam (open-source).'


        }

        # ANSI escape codes for text color
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'end': '\033[0m',
        }

        self.ascii_banner = r"""
############################
# _   _     ____ ___ ____  #
#| | | |___|  _ \_ _/ ___| #
#| | | |_  / | | | |\___ \ #
#| |_| |/ /| |_| | | ___) |#
# \___//___|____/___|____/ #
############################
"""
        self.created_by_message = f"{self.colors['green']}Created by Hoso{self.colors['end']}\n"

    def suggest_alternative(self, app_name):
        app_name_lower = app_name.lower()
        suggestion = self.suggestions.get(app_name_lower, f"{self.colors['red']}No privacy suggestion found for {app_name}.{self.colors['end']}")
        return f"{self.colors['green']}Privacy Suggestion: {suggestion}{self.colors['end']}"

    def display_banner(self):
        print(self.ascii_banner)
        print(self.created_by_message)


if __name__ == "__main__":
    privacy_app = PrivacySuggestionApp()

    privacy_app.display_banner()

    while True:
        search_query = input("Enter the app you want a privacy suggestion for (or type 'exit' to quit): ")

        if search_query.lower() == 'exit':
            break

        app_suggestion = privacy_app.suggest_alternative(search_query)
        print(app_suggestion)
