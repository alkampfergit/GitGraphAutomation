"""
Invoke git and grab output
"""
import os
import subprocess


def invoke_git_log(limit=0, directory=""):
    """
    Invoke git via commandline requesting a json output format.
    @param limit: Maximum number of commit to log, to avoid having a super big image
    @param directory: Path that contains git repository you want to render
    @return:
    """
    # When directory is not specified we work in current directory.
    if directory == "":
        directory = os.path.dirname(__file__)

    # # baseCommand = "git --git-dir='C:/develop/GitHub/AzureDevopsWordPlayground/.git' log --pretty=format:'{%n  \"refs\" : \"%D\",%n  \"hash\": \"%H\",%n  \"hashAbbrev\" : \"%h\",%n  \"parents\" : [\"%P\"],%n  \"author\": {%n    \"name\": \"%aN\",%n    \"email\": \"%aE\",%n    \"timestamp\": \"%aD\"%n  },%n  \"subject\": \"%s\"%n},'"
    # # if limit > 0:
    # #     baseCommand += f' -n {limit}'
    # command = ['git']
    # command.append('--git-dir=C:/develop/GitHub/AzureDevopsWordPlayground/.git')
    # command.append('log')
    # command.append("--pretty=format:'{%n  \"refs\" : \"%D\",%n  \"hash\": \"%H\",%n  \"hashAbbrev\" : \"%h\",%n  \"parents\" : [\"%P\"],%n  \"author\": {%n    \"name\": \"%aN\",%n    \"email\": \"%aE\",%n    \"timestamp\": \"%aD\"%n  },%n  \"subject\": \"%s\"%n},")

    # if limit > 0:
    #     command.append(f'-n {limit}')

    # output = subprocess.run(command, capture_output=True)
    # result = output.stdout.decode('utf-8')

    command = ['git']
    # command.append('--git-dir=C:/develop/GitHub/AzureDevopsWordPlayground/.git')
    command.append('log')
    command.append(
        "--pretty=format:{\"refs\" : \"%D\",  \"hash\": \"%H\",  \"hashAbbrev\" : \"%h\",  \"parents\" : \"%P\",  \"author\": {    \"name\": \"%aN\",    \"email\": \"%aE\",    \"timestamp\": \"%aD\"  },  \"subject\": \"%s\"},")

    if limit > 0:
        command.append(f'-n {limit}')

    process = subprocess.Popen(command, cwd=directory, stdout=subprocess.PIPE)
    result = process.communicate()[0].decode('utf-8')
    return result
