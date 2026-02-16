import win32ui
from pypresence import Presence
from time import sleep, time

def wrap(client_id):  # Wait until Discord is open
    app = None
    while not app:
        try:
            app = Presence(client_id)
        except:
            sleep(15)
    return app


def is_genshin():
    try:
        # Detect Genshin window
        win32ui.FindWindow(None, 'Genshin Impact')
    except win32ui.error:
        return False
    return True


def update_presence(mod):
    genshin = is_genshin()

    if (not genshin) and mod:
        app.close()   # Close Discord RPC if game closed
        return False

    if genshin and (not mod):
        app.connect()
        app.update(
            details="Gooning",
            large_image="genshin",
            start=time()
        )
        return True

    return mod


app = wrap('YOUR_APP_ID')  # Replace with your App ID
mod = False

while True:   # Infinite loop
    try:
        mod = update_presence(mod)
    except:
        mod = False
    sleep(15)
