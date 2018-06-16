"""
this part checks external packages and install if not exist
"""

requirements = ['pygame']
import sys

# find and install any missing external packages
def check():
    # find missing packages
    from importlib.util import find_spec
    missing = [requirement for requirement in requirements if not(find_spec(requirement))]
    if not missing:
        return
    # install missing packages
    sys.stdout.write("Installing" + ','.join(missing) + ".\n")
    # redirect out to nothing so no installing messages will be seen.
    sys_stdout = sys.stdout
    sys_stderr = sys.stderr
    sys.stdout = None
    sys.stderr = None
    from pip.commands.install import InstallCommand
    from pip.status_codes import SUCCESS
    cmd = InstallCommand()
    for requirement in requirements:
        try:
            if cmd.main([requirement]) is not SUCCESS:
                sys_stderr.write("Can not install " + requirement + ", program aborts.\n")
                sys.exit()
        # this might occur because of redirection of stdout and stderr
        except AttributeError:
            pass
    # direct out back to normal
    sys.stdout = sys_stdout
    sys.stderr = sys_stderr
    sys.stdout.write("All packages are installed, starting game...")
    sys.stdout.flush()