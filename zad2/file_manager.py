class FileManager:
    def __init__(self, name):
        self.name = name
    def filePatch(self):
        try:
            loading = open(self.name, 'a' , encoding='utf-8')
            read = loading.read()
            return read
        except: print("Nie mozna załadowac pliku")
    def update(self, text):
        try:
            loading = open(self.name, 'a' , encoding='utf-8')
            loading.write(text)
            loading.close(text)
        except: print("Nie można zapisać")
    
