
from urllib.parse import urlparse, unquote

from gi.repository import GObject, Nautilus
from PIL import Image

import base64


class ImageUtilsMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    VALID_MIMETYPES = ('image/png', 'image/jpeg')

    def convert_to_webp(self, menu, files):
        for file in files:
            file_path = unquote(urlparse(file.get_uri()).path)
            image = Image.open(file_path)
            image.save(f"{file_path}.webp", format="webp")

    def convert_to_base64(self, menu, files):
        for file in files:
            file_path = unquote(urlparse(file.get_uri()).path)
            with open(file_path, "rb") as image_file:
                image_data = image_file.read()
                base64_encoded = base64.b64encode(image_data)
                base64_string = base64_encoded.decode("utf-8")
                with open(f"{file_path}.txt", "w") as b64:
                    b64.write(base64_string)

    def get_file_items(self, files):
        for file in files:
            if file.get_mime_type() not in self.VALID_MIMETYPES:
                return ()

        menu_item_webp = Nautilus.MenuItem(
            name="convert_to_webp", label="✨ Convert to WEBP")
        menu_item_webp.connect('activate', self.convert_to_webp, files)

        menu_item_base64 = Nautilus.MenuItem(
            name="convert_to_base64", label="✨ Convert to Base64")
        menu_item_base64.connect('activate', self.convert_to_base64, files)

        return menu_item_webp, menu_item_base64
