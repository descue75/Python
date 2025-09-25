from pathlib import Path

print(Path())
print(Path('03 - Input').exists())

path = Path("emails")
if(path.exists() == False):
  path.mkdir()
else:
  path.rmdir()

path = Path()
files = path.glob('*.*')
for file in files:
  print(file.name)

files_and_dirs = path.glob('*')
for item in files_and_dirs:
  print(item)