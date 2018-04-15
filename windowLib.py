import win32gui
from win32api import GetSystemMetrics
import psutil
import os

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake - Guake For Windows' in win32gui.GetWindowText(hwnd):
            m_width = GetSystemMetrics(0)
            m_length = GetSystemMetrics(1)
            w_width = int(m_width)
            w_length = int(m_length/2)
            win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

def window_resize():
    win32gui.EnumWindows(enumHandler, None)

def is_running(thing):
    return thing in (p.name() for p in psutil.process_iter())

def chdir(path):
    if '%' in path:
        env_var = path.upper().replace('%', '')
        #print(env_var)
        env_path = os.getenv(env_var)
    else:
        env_path = path
    #print(env_path)

    try:
        os.chdir(env_path)
    except Exception as e:
        print(e)

def get_dir(path_to_log="./path.log"):
    last = last_line(path_to_log)
    return last

def write_to_log(path, path_to_log=os.path.dirname(os.path.realpath(__file__))):
    pathlog = open('{}\\path.log'.format(path_to_log), 'a')
    pathlog.write('{}\n'.format(path))
    pathlog.close()

def last_line(inputfile):
    with open(inputfile, "rb") as f:
        first = f.readline()
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b"\n":
            f.seek(-2, os.SEEK_CUR)
        last = f.readline()
        return last
