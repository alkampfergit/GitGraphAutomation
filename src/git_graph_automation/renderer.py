import os

def renderHtml(jsonContent, outFile):
    with open(f'{os.path.dirname(__file__)}/output.html', 'r') as file:
        data = file.read()
    
    data = data.replace("***COMMITHERE***", jsonContent)

    with open(outFile, 'w') as file:
        data = file.write(data)