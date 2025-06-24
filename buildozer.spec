[app]

# Title of your application
title = Tunnel

# Package name and domain
package.name = tunnel
package.domain = org.test

# Main source directory and file extensions
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Main Python dependencies
requirements = python3,kivy

# Screen orientation (portrait or landscape)
orientation = portrait

# Use fullscreen (1 for yes, 0 for no)
fullscreen = 0

# Supported Android architectures
android.archs = arm64-v8a, armeabi-v7a

# Enable backup on Android
android.allow_backup = True

# Logcat filters to help with debugging
android.logcat_filters = *:S python:D

# Minimum and Target Android API versions
android.minapi = 21
android.api = 31

# Icon and presplash image (optional — provide your paths)
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# Enable private data storage
android.private_storage = True

# Uncomment if your app needs Internet
# android.permissions = INTERNET

# Uncomment this if you plan to use AndroidX/Kotlin/modern libraries
# android.enable_androidx = True

# Python for Android bootstrap
# p4a.bootstrap = sdl2

# Include additional assets if needed
# android.add_assets = assets/

# Optional: Use adaptive icons for Android 8+
# icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
# icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png


[buildozer]

# Verbosity level
log_level = 2

# Warn if Buildozer runs as root
warn_on_root = 1

# Build artifact output directories
# build_dir = ./.buildozer
# bin_dir = ./bin
