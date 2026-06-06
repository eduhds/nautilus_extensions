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
icon_clojure = 'ne-clojure'
icon_groovy = 'ne-groovy'
icon_openjdk = 'ne-openjdk'
icon_rust = 'ne-rust'
icon_snapcraft = 'ne-snapcraft'
icon_julia = 'ne-julia'
icon_vala = 'ne-vala'

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

            # Directory name

            commom_names = [
                # Android
                ('android', icon_android),
                # macOS
                ('macos', icon_apple),
                # iOS
                ('ios', icon_ios),
                # Linux
                ('linux', icon_linux),
                ('ubuntu', icon_ubuntu),
                ('fedora', icon_fedora),
                ('manjaro', icon_manjaro),
                ('alpine', icon_alpine),
                ('deepin', icon_deepin),
                ('mint', icon_mint),
                ('centos', icon_centos),
                ('rocklinux', icon_rockylinux),
                ('debian', icon_debian),
                ('almalinux', icon_almalinux),
                ('opensuse', icon_opensuse),
                # Windows
                ('windows', icon_windows),
                ('snap', icon_snapcraft)
            ]

            for c_name in commom_names:
                if name.lower() == c_name[0]:
                    file.add_emblem(c_name[1])
                    return

            file_path = unquote(urlparse(file.get_uri()).path)
            dir_items = [f for f in os.listdir(
                file_path) if os.path.isfile(os.path.join(file_path, f))]

            # Directory content

            limit = 3
            count = 0

            tecnologies = [
                # Deno
                ('deno.json', None, icon_deno),
                # Bun
                ('bun.lock', None, icon_bun),
                # Flutter
                ('pubspec.yaml', None, icon_flutter),
                # Android Studio
                ('app/src/main/AndroidManifest.xml', None, icon_android_studio),
                # Node.JS
                ('package.json', None, icon_nodejs),
                # React Native
                ('metro.config.js', None, icon_react),
                # Electron
                ('forge.config.js', None, icon_electron),
                # NPM
                ('package-lock.json', None, icon_npm),
                # Yarn
                ('yarn.lock', None, icon_yarn),
                # Pnpm
                ('pnpm-lock.yaml', None, icon_pnpm),
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
                ('go.mod', ('.go'), icon_go),
                # HTML
                (None, ('.html', '.htm'), icon_html5),
                # JavaScript
                (None, ('.js', '.cjs', '.mjs'), icon_javascript),
                # TypeScript
                (None, ('.ts'), icon_typescript),
                # Lua
                (None, ('.lua'), icon_lua),
                # PHP
                ('composer.json', ('.php'), icon_php),
                # Composer
                ('composer.json', None, icon_composer),
                # Python
                (None, ('.py', '.pyz'), icon_python),
                # C#
                (None, ('.cs'), icon_csharp),
                # Ruby
                (None, ('.rb'), icon_ruby),
                # RubyGems
                ('Gemfile', None, icon_rubygems),
                # Swift
                (None, ('.swift'), icon_swift),
                # Kotlin
                (None, ('.kt', '.kts'), icon_kotlin),
                # Perl
                (None, ('.pl', '.pm'), icon_perl),
                # Rust
                (None, ('.rs'), icon_rust),
                # Groovy
                (None, ('.groovy'), icon_groovy),
                # Clojure
                (None, ('.clj'), icon_clojure),
                # Julia
                (None, ('.jl'), icon_julia),
                # Vala
                (None, ('.vala'), icon_vala),
                # Docker
                ('Dockerfile', None, icon_docker),
                ('docker-compose.yml', None, icon_docker),
                # Shell
                (None, ('.sh'), icon_bash),
                # PowerShell
                (None, ('.ps1'), icon_powershell)
            ]

            for lang in tecnologies:
                # (target?, extensions?, icon)
                (target, extensions, icon) = lang

                has_target = target is not None and os.path.exists(
                    os.path.join(file_path, target))

                ext_files = [
                    f for f in dir_items if f.endswith(extensions)] if extensions is not None else []

                if has_target or len(ext_files) > 0:
                    file.add_emblem(icon)
                    count += 1

                if count >= limit:
                    break
