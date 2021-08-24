# What is it

This is an experiment to use [GitGraph.js](https://gitgraphjs.com/#0) library to render a graph of git commits automatically with a simple Python script.

## How to use it

You need to install [playwright](https://playwright.dev/python/docs/intro/) to automatically render image using chromium. 

> rendering image with playwright is completely optional, just avoid  --renderpng parameter and you will only have html file rendered

```bash
pip install playwright
playwright install
```

After that you can use it with simple command line to render commit list of repository specified with --repo parameter.

Windows command line:

```powershell
python .\gitRender.py --repo C:\develop\github\GitGraphAutomation\ --outhtml c:\temp\render.html --renderpng c:\temp\render.png
```

Linux command line:

```bash
./gitRender.py --repo /home/user/develop/myrepo --outhtml /tmp/render.html --renderpng /tmp/render.png
```
