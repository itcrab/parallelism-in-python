import subprocess

subprocess.Popen('ls')
subprocess.Popen(['ls', '-all'])

subprocess.Popen('ls -all', shell=True)
subprocess.Popen('ls -all &>/dev/null', shell=True)


sp = subprocess.Popen('cat', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print(sp.poll())  # None

sp_bytes = sp.stdin.write(b'Hello World!')
print('STDIN {} bytes'.format(sp_bytes))
sp.stdin.close()

print(sp.stdout.read())  # b'Hello World!'
print(sp.poll())  # 0 - success
