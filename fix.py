with open('dashboard.py', 'r') as f:
    content = f.read()

content = content.replace('''        else:
        elif self.path == "/api/skip":''', '''        elif self.path == "/api/skip":''')

with open('dashboard.py', 'w') as f:
    f.write(content)
