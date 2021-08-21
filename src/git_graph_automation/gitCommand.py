import os
from posixpath import basename

def invokeGitLog(limit = 0):
    baseCommand = "git log --pretty=format:'{%n  \"refs\" : \"%D\",%n  \"hash\": \"%H\",%n  \"hashAbbrev\" : \"%h\",%n  \"parents\" : [\"%P\"],%n  \"author\": {%n    \"name\": \"%aN\",%n    \"email\": \"%aE\",%n    \"timestamp\": \"%aD\"%n  },%n  \"subject\": \"%s\"%n},'"
    if limit > 0:
        baseCommand += f' -n {limit}'
    stream = os.popen(baseCommand)
    output = stream.read()
    return output