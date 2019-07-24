import webbrowser

def makeurl(token, method):
    return f'https://api.telegram.com/bot{token}/{method}'

def docs():
    webbrowser.open('https://telegram.com')
    return True