# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['bot.py'],
    pathex=[],
    binaries=[],
    datas=[('config.py', '.'), ('C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\setuptools\\_distutils', 'setuptools/_distutils')],
    hiddenimports=['setuptools._distutils', 'setuptools._distutils.errors', 'setuptools._distutils.spawn', 'setuptools._distutils.compilers', 'distutils', 'distutils.errors', 'distutils.spawn', 'distutils.compilers'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='qwe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
