# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.

#Methods
# 1. score_server - This function will serve the score. It will read the score from the scores file
# and will return an HTML that will be as follows:
#
# <html>
# <head>
# <title>Scores Game</title>
# </head>
# <body>
# <h1>The score is <div id="score">{SCORE}</div></h1>
# </body>
# </html>
#
# If the function will have a problem showing the result of reading the error it will return the
# following:
# <html>
# <head>
# <title>Scores Game</title>
# </head>
# <body>
# <body>
# <h1><div id="score" style="color:red">{ERROR}</div></h1>
# </body>
#</html>