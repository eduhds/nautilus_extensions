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
icon_bun = 'ne-bun'
icon_npm = 'ne-npm'
icon_yarn = 'ne-yarn'
icon_pnpm = 'ne-pnpm'
icon_bash = 'ne-bash'
icon_windows = 'ne-windows'
icon_powershell = 'ne-powershell'
icon_csharp = 'ne-csharp'

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
            dir_items = [f for f in os.listdir(
                file_path) if os.path.isfile(os.path.join(file_path, f))]

            # Directory name

            # Android
            if name.lower() == 'android':
                file.add_emblem(icon_android)
                return

            # macOS
            if name.lower() == 'macos':
                file.add_emblem(icon_apple)
                return

            # iOS
            if name.lower() == 'ios':
                file.add_emblem(icon_ios)
                return

            # Linux
            if name.lower() == 'linux':
                file.add_emblem(icon_linux)
                return

            # Windows
            if name.lower() == 'windows':
                file.add_emblem(icon_windows)
                return

            # Frameworks

            # deno.json (Deno)
            target_file = os.path.join(file_path, 'deno.json')
            if os.path.exists(target_file):
                file.add_emblem(icon_deno)
                return

            # bun.lockb (Bun)
            target_file = os.path.join(file_path, 'bun.lockb')
            if os.path.exists(target_file):
                file.add_emblem(icon_bun)
                return

            # pubspec.yaml (Flutter)
            target_file = os.path.join(file_path, 'pubspec.yaml')
            if os.path.exists(target_file):
                file.add_emblem(icon_flutter)
                return

            # composer.json (Composer)
            target_file = os.path.join(file_path, 'composer.json')
            if os.path.exists(target_file):
                file.add_emblem(icon_composer)
                return

            # Node.JS ecossystem
            is_node = False

            # metro.config.js (React Native)
            target_file = os.path.join(file_path, 'metro.config.js')
            if os.path.exists(target_file):
                file.add_emblem(icon_react)
                is_node = True

            # forge.config.js (Electron)
            target_file = os.path.join(file_path, 'forge.config.js')
            if not is_node and os.path.exists(target_file):
                file.add_emblem(icon_electron)
                is_node = True

            # package.json (Node.js)
            target_file = os.path.join(file_path, 'package.json')
            if not is_node and os.path.exists(target_file):
                file.add_emblem(icon_nodejs)
                is_node = True

            # Package manager
            if is_node:
                # NPM
                if 'package-lock.json' in dir_items:
                    file.add_emblem(icon_npm)
                # Yarn
                if 'yarn.lock' in dir_items:
                    file.add_emblem(icon_yarn)
                # Pnpm
                if 'pnpm-lock.yaml' in dir_items:
                    file.add_emblem(icon_pnpm)

                return

            # File extensions

            limit = 3
            count = 0

            # .ino (Arduino)
            ext_files = [f for f in dir_items if f.endswith('.ino')]
            if len(ext_files) > 0:
                file.add_emblem(icon_arduino)
                count += 1

            if count >= limit:
                return

            # .cpp, .hpp (C++)
            ext_files = [f for f in dir_items if f.endswith(('.cpp', '.hpp'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_cplusplus)
                count += 1

            if count >= limit:
                return

            # .css (CSS)
            ext_files = [f for f in dir_items if f.endswith('.css')]
            if len(ext_files) > 0:
                file.add_emblem(icon_css)
                count += 1

            if count >= limit:
                return

            # .c, .h (C)
            ext_files = [f for f in dir_items if f.endswith(('.c', '.h'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_c)
                count += 1

            if count >= limit:
                return

            # .dart (Dart)
            ext_files = [f for f in dir_items if f.endswith('.dart')]
            if len(ext_files) > 0:
                file.add_emblem(icon_dart)
                count += 1

            if count >= limit:
                return

            # .jsx, .tsx (React/React Native)
            ext_files = [f for f in dir_items if f.endswith(('.jsx', '.tsx'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_react)
                count += 1

            if count >= limit:
                return

            # go.mod or .go (Golang)
            target_file = os.path.join(file_path, 'go.mod')
            ext_files = [f for f in dir_items if f.endswith('.go')]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_go)
                count += 1

            if count >= limit:
                return

            # .html, .htm (HTML)
            ext_files = [f for f in dir_items if f.endswith(('.html', '.htm'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_html5)
                count += 1

            if count >= limit:
                return

            # .js, .cjs, .mjs (JavaScript)
            ext_files = [f for f in dir_items if f.endswith(
                ('.js', '.cjs', '.mjs'))]
            if len(ext_files) > 0:
                file.add_emblem(icon_javascript)
                count += 1

            if count >= limit:
                return

            # .ts (TypeScript)
            ext_files = [f for f in dir_items if f.endswith('.ts')]
            if len(ext_files) > 0:
                file.add_emblem(icon_typescript)
                count += 1

            if count >= limit:
                return

            # .lua (Lua)
            ext_files = [f for f in dir_items if f.endswith('.lua')]
            if len(ext_files) > 0:
                file.add_emblem(icon_lua)
                count += 1

            if count >= limit:
                return

            # .php (PHP)
            ext_files = [f for f in dir_items if f.endswith('.php')]
            if len(ext_files) > 0:
                file.add_emblem(icon_php)
                count += 1

            if count >= limit:
                return

            # .py (Python)
            ext_files = [f for f in dir_items if f.endswith('.py')]
            if len(ext_files) > 0:
                file.add_emblem(icon_python)
                count += 1

            if count >= limit:
                return

            # .cs (C#)
            ext_files = [f for f in dir_items if f.endswith('.cs')]
            if len(ext_files) > 0:
                file.add_emblem(icon_csharp)
                count += 1

            if count >= limit:
                return

            # Gemfile or .rb (Ruby)
            target_file = os.path.join(file_path, 'Gemfile')
            ext_files = [f for f in dir_items if f.endswith('.rb')]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_ruby)
                count += 1

            if count >= limit:
                return

            # Package.swift or .swift (Swift)
            target_file = os.path.join(file_path, 'Package.swift')
            ext_files = [f for f in dir_items if f.endswith('.swift')]
            if os.path.exists(target_file) or len(ext_files) > 0:
                file.add_emblem(icon_swift)
                count += 1

            if count >= limit:
                return

            # .sh (Shell)
            ext_files = [f for f in dir_items if f.endswith('.sh')]
            if len(ext_files) > 0:
                file.add_emblem(icon_bash)
                count += 1

            if count >= limit:
                return

            # .ps1 (PowerShell)
            ext_files = [f for f in dir_items if f.endswith('.ps1')]
            if len(ext_files) > 0:
                file.add_emblem(icon_powershell)
