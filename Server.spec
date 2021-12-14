# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/MATHE/projeto_whatsapp_mais_elaborado/Server.py'],
             pathex=['C:\\Users\\MATHE\\projeto_whatsapp_mais_elaborado'],
             binaries=[],
             datas=[('C:/Users/MATHE/projeto_whatsapp_mais_elaborado/Base.csv', '.'), ('C:/Users/MATHE/projeto_whatsapp_mais_elaborado/msg.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\Users\\MATHE\\Downloads\\search.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Server')
