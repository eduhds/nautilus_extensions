"""
Add an action to the Nautilus context-menu to convert png and jpeg images
to the wepb format.

Author: Egidio Docile
https://linuxconfig.org/how-to-write-nautilus-extensions-with-nautilus-python
"""

from urllib.parse import urlparse, unquote

from gi.repository import GObject, Nautilus
from PIL import Image


class ConvertToWebpMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    VALID_MIMETYPES = ('image/png', 'image/jpeg')

    def convert(self, menu, files):
        for file in files:
            file_path = unquote(urlparse(file.get_uri()).path)
            image = Image.open(file_path)
            image.save(f"{file_path}.webp", format="webp")

    def get_file_items(self, files):
        for file in files:
            if file.get_mime_type() not in self.VALID_MIMETYPES:
                return ()

        menu_item = Nautilus.MenuItem(
            name="convert_to_webp",
            label="Convert to wepb")

        menu_item.connect('activate', self.convert, files)

        return menu_item,
