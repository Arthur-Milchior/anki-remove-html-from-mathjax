from aqt import mw
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.qt import *
from aqt.utils import getText
from aqt import gui_hooks

def repl(match):
    return re.sub("<(?:(?![<>]).)*>", "", match.group(0), flags=re.M|re.S)

def replace(show_only):
    quote = "\""
    queries = list()
    for open, close in [("(", ")"), ("[", "]")]:
        open = f"\\\\\\{open}"
        close = f"\\\\\\{close}"
        not_open = f"(?!{open})."
        not_opens = f"(?:{not_open})*"
        query = f"{open}(?P<code>{not_opens}{not_opens}){close}"
        
        queries.append(query)
    nids = mw.col.find_notes("")
    replaces = []
    for nid in set(nids):
        change = False
        note = mw.col.getNote(nid)
        for i in range(len(note.fields)):
            old_field = field = note.fields[i]
            for query in queries:
                field = re.sub(query, repl, field, flags=re.M|re.S)
            if field != old_field:
                replaces.append((old_field, field))
                change = True
                note.fields[i] = field
        if change and not show_only:
            note.flush()
    print("The changes where:\n" + "\n".join(f"«{orig}»->«{res}»" for (orig, res) in replaces))
    

def menus(browser):
    action = QtWidgets.QAction(browser)
    action.setObjectName("noHtmlInMathJax")
    browser.form.menuEdit.addAction(action)
    action.setText("Remove all html in mathjax")
    qconnect(action.triggered, replace)
    
gui_hooks.browser_menus_did_init.append(menus)          
