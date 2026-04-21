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
icon_android_studio = 'ne-androidstudio'
icon_kotlin = 'ne-kotlin'
icon_docker = 'ne-docker'
icon_perl = 'ne-perl'
icon_rubygems = 'ne-rubygems'
icon_xcode = 'ne-xcode'
icon_ubuntu = 'ne-ubuntu'
icon_debian = 'ne-debian'
icon_fedora = 'ne-fedora'
icon_alpine = 'ne-alpinelinux'
icon_opensuse = 'ne-opensuse'
icon_almalinux = 'ne-almalinux'
icon_manjaro = 'ne-manjaro'
icon_rockylinux = 'ne-rockylinux'
icon_centos = 'ne-centos'
icon_deepin = 'ne-deepin'
icon_mint = 'ne-mint'

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
            distros = [
                ('ubuntu', icon_ubuntu),
                ('fedora', icon_fedora),
                ('manjaro', icon_manjaro),
                ('alpine', icon_alpine),
                ('deepin', icon_deepin),
                ('oraclelinux', None),
                ('mint', icon_mint),
                ('centos', icon_centos),
                ('gentoo', None),
                ('rocklinux', icon_rockylinux),
                ('debian', icon_debian),
                ('kali', None),
                ('almalinux', icon_almalinux),
                ('opensuse', icon_opensuse),
                ('archlinux', None)
            ]
            for distro in distros:
                if name.lower() == distro[0]:
                    file.add_emblem(distro[1] or icon_linux)
                    return
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

            # app/src/main/AndroidManifest.xml (Android Studio)
            target_file = os.path.join(
                file_path, 'app/src/main/AndroidManifest.xml')
            if os.path.exists(target_file):
                file.add_emblem(icon_android_studio)
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

            languages = [
                # Arduino
                (None, ('.ino'), icon_arduino),
                # C++
                (None, ('.cpp', '.hpp'), icon_cplusplus),
                # CSS
                (None, ('.css'), icon_css),
                # C
                (None, ('.c', '.h'), icon_c),
                # Dart
                (None, ('.dart'), icon_dart),
                # React
                (None, ('.jsx', '.tsx'), icon_react),
                # Golang
                (('go.mod', None), ('.go'), icon_go),
                # HTML
                (None, ('.html', '.htm'), icon_html5),
                # JavaScript
                (None, ('.js', '.cjs', '.mjs'), icon_javascript),
                # TypeScript
                (None, ('.ts'), icon_typescript),
                # Lua
                (None, ('.lua'), icon_lua),
                # PHP
                (('composer.json', icon_composer), ('.php'), icon_php),
                # Python
                (None, ('.py', '.pyz'), icon_python),
                # C#
                (None, ('.cs'), icon_csharp),
                # Ruby
                (('Gemfile', icon_rubygems), ('.rb'), icon_ruby),
                # Swift
                (None, ('.swift'), icon_swift),
                # Kotlin
                (None, ('.kt', '.kts'), icon_kotlin),
                # Perl
                (None, ('.pl', '.pm'), icon_perl),
                # Docker
                (('Dockerfile', None), None, icon_docker),
                (('docker-compose.yml', None), None, icon_docker),
                # Shell
                (None, ('.sh'), icon_bash),
                # PowerShell
                (None, ('.ps1'), icon_powershell)
            ]

            for lang in languages:
                # ((target, icon?)?, extensions?, icon)
                (target, extensions, icon) = lang

                target_matched = False

                if target is not None:
                    (tfile, ticon) = target
                    target_file = os.path.join(file_path, tfile)

                    if os.path.exists(target_file):
                        target_matched = True
                        file.add_emblem(icon)
                        if ticon is not None:
                            file.add_emblem(ticon)
                        count += 1

                if not target_matched and extensions is not None:
                    ext_files = [
                        f for f in dir_items if f.endswith(extensions)]
                    if len(ext_files) > 0:
                        file.add_emblem(icon)
                        count += 1

                if count >= limit:
                    break
