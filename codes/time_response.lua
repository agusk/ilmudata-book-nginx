ngx.header.content_type = 'text/html';
ngx.say("<html><body>")
ngx.say("<h1>Current time: " .. os.date("%Y-%m-%d %H:%M:%S") .. "</h1>")
ngx.say("</body></html>")