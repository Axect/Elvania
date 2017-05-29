from subprocess import call
link = raw_input('')
call('youtube-dl --embed-thumbnail --format mp4 '+link, shell=True)