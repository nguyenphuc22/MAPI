import  pickle
import os

def getPathFile(msg):
    return msg[msg.index("send") + 4:len(msg)].strip()


def getTree(path):
    link = path[path.index("list") + 4:len(path)].strip()
    if not link:
        link = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    tree = link + "\n"
    for root, dirs, files in os.walk(link):
        level = root.replace(link, '').count(os.sep)
        indent = ' ' * 4 * (level)
        # print('{}{}/'.format(indent, os.path.basename(root)))
        tree = tree + ('{}{}/'.format(indent, os.path.basename(root))) + "\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            # print('{}{}'.format(subindent, f))
            tree = tree + ('{}{}'.format(subindent, f)) + "\n"

    return tree