[app]
title = Esim Pro
package.name = esimpro
package.domain = org.guessar
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 1.0
requirements = kivy,phonenumbers,qrcode,pillow
orientation = portrait
fullscreen = 1
entrypoint = esim_pro.py
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.private_storage = true
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1