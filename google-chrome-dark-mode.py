import shutil, re, os, time, sys

with open('/usr/share/applications/google-chrome.desktop', 'r') as x:
    with open('google-chrome.desktop', 'w') as ll:

        for l in x.readlines():
            if re.search('^Exec', l):
                z = l.replace('\n', ' --force-dark-mode\n')
                print(z)
                ll.write(z)
            else:
                ll.write(l)

pathname = os.path.dirname(sys.argv[0])
current_path = os.path.abspath(pathname)
os.remove('/usr/share/applications/google-chrome.desktop')

time.sleep(0.1)

dup_file_path = current_path + '/google-chrome.desktop'
shutil.copyfile(dup_file_path, '/usr/share/applications/google-chrome.desktop')
os.remove(dup_file_path)
