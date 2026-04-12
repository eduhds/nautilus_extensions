from gi.repository import Nautilus, GObject
from urllib.parse import urlparse, unquote
import os

icon_android = 'ne-android'
icon_apple = 'ne-apple'
icon_arduino = 'ne-arduino'
icon_composer = 'ne-composer'
icon_cplusplus = 'ne-cplusplus'
icon_css = 'ne-css'
icon_c = 'ne-c'
icon_dart = 'ne-dart'
icon_deno = 'ne-deno'
icon_dotenv = 'ne-dotenv'
icon_electron = 'ne-electron'
icon_flutter = 'ne-flutter'
icon_github = 'ne-github'
icon_git = 'ne-git'
icon_gnome = 'ne-gnome'
icon_go = 'ne-go'
icon_html5 = 'ne-html5'
icon_ios = 'ne-ios'
icon_javascript = 'ne-javascript'
icon_linux = 'ne-linux'
icon_lua = 'ne-lua'
icon_nodejs = 'ne-nodejs'
icon_php = 'ne-php'
icon_python = 'ne-python'
icon_react = 'ne-react'
icon_ruby = 'ne-ruby'
icon_swift = 'ne-swift'
icon_typescript = 'ne-typescript'

skip_dirs = ['node_modules', 'vendor']


class DevIconExtension(GObject.GObject, Nautilus.InfoProvider):
    def __init__(self):
        super().__init__()
        print("Initialized DevIconExtension")

    def update_file_info_full(self, provider, handle, closure, file):
        if file.is_directory():
            name: str = file.get_name()

            if name in skip_dirs:
                return

            if name.startswith('.'):
                return

            file_path = unquote(urlparse(file.get_uri()).path)
            dir_items = os.listdir(file_path)

            # Android
            if name.lower() == 'android':
                file.add_emblem(icon_android)

            # Apple
            if name.lower() == 'macos':
                file.add_emblem(icon_apple)

            # .ino (Arduino)
            ext_files = [f for f in dir_items if f.endswith('.ino')]
            if len(ext_files) > 0:
                file.add_emblem(icon_arduino)

            # composer.json (Composer)
            target_file = os.path.join(file_path, 'composer.json')
            if os.path.exists(target_file):
                file.add_emblem(icon_composer)

            # .cpp, .hpp (C++)
            ext_files = [f for f in dir_items if f.endswith(('.cpp', '.hpp'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_cplusplus)

            # .css (CSS)
            ext_files = [f for f in dir_items if f.endswith('.css')]
            if len(ext_files) > 0:
                file.add_emblem(icon_css)

            # .c, .h (C)
            ext_files = [f for f in dir_items if f.endswith(('.c', '.h'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_c)

            # deno.json (Deno)
            target_file = os.path.join(file_path, 'deno.json')
            if os.path.exists(target_file):
                file.add_emblem(icon_deno)

            # .env (Dotenv)
            ext_files = [f for f in dir_items if f.startswith('.env')]
            if len(ext_files) > 0:
                file.add_emblem(icon_dotenv)

            # .dart (Dart)
            ext_files = [f for f in dir_items if f.endswith('.dart')]
            if len(ext_files) > 0:
                file.add_emblem(icon_dart)

            # deno.json (Deno)
            target_file = os.path.join(file_path, 'deno.json')
            if os.path.exists(target_file):
                file.add_emblem(icon_deno)

            # forge.config.js (Electron)
            target_file = os.path.join(file_path, 'forge.config.js')
            if os.path.exists(target_file):
                file.add_emblem(icon_electron)

            # pubspec.yaml (Flutter)
            target_file = os.path.join(file_path, 'pubspec.yaml')
            if os.path.exists(target_file):
                file.add_emblem(icon_flutter)

            # .github (GitHub)
            target_file = os.path.join(file_path, '.github')
            if os.path.exists(target_file):
                file.add_emblem(icon_github)

            # go.mod or .go (Golang)
            target_file = os.path.join(file_path, 'go.mod')
            ext_files = [f for f in dir_items if f.endswith('.go')]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_go)

            # .html, .htm (HTML)
            ext_files = [f for f in dir_items if f.endswith(('.html', '.htm'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_html5)

            # iOS
            if name.lower() == 'ios':
                file.add_emblem(icon_ios)

            # .js, .cjs, .mjs, .jsx (JavaScript)
            ext_files = [f for f in dir_items if f.endswith(
                ('.js', '.cjs', '.mjs', '.jsx'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_javascript)

            # Linux
            if name.lower() == 'linux':
                file.add_emblem(icon_linux)

            # .lua (Lua)
            ext_files = [f for f in dir_items if f.endswith('.lua')]
            if len(ext_files) > 0:
                file.add_emblem(icon_lua)

            # package.json (Node.js)
            target_file = os.path.join(file_path, 'package.json')
            if os.path.exists(target_file):
                file.add_emblem(icon_nodejs)

            # .php (PHP)
            ext_files = [f for f in dir_items if f.endswith('.php')]
            if len(ext_files) > 0:
                file.add_emblem(icon_php)

            # .py (Python)
            ext_files = [f for f in dir_items if f.endswith('.py')]
            if len(ext_files) > 0:
                file.add_emblem(icon_python)

            # metro.config.js or .jsx, .tsx (React/React Native)
            target_file = os.path.join(file_path, 'metro.config.js')
            ext_files = [f for f in dir_items if f.endswith(('.jsx', '.tsx'))]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_react)

            # Gemfile or .rb (Ruby)
            target_file = os.path.join(file_path, 'Gemfile')
            ext_files = [f for f in dir_items if f.endswith('.rb')]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_ruby)

            # Package.swift or .swift (Swift)
            target_file = os.path.join(file_path, 'Package.swift')
            ext_files = [f for f in dir_items if f.endswith('.swift')]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_swift)

            # .ts, .tsx (TypeScript)
            ext_files = [f for f in dir_items if f.endswith(('.ts', '.tsx'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_typescript)
