# -*- mode: python -*-
import os

PATH = os.path.realpath('src/')
print(PATH)

block_cipher = None

added_files = [
    (PATH + '/FOLDER_1', 'src/FOLDER_1')
]

a = Analysis([PATH + '/jenkins_test.py'],
             pathex=[PATH],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='jenkins_test',
          debug=True,
          strip=False,
          upx=False,
          console=False, icon='/Users/sansorge/PycharmProjects/jenkins_test/src/FOLDER_1/jenkins.png.icns')
app = BUNDLE(exe,
             name='jenkins_test.app',
             icon='/Users/sansorge/PycharmProjects/jenkins_test/src/FOLDER_1/jenkins.png.icns',
             bundle_identifier=None)
