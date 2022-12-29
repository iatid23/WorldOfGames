from flask import Flask, render_template

# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.

# Methods
# 1. score_server - This function will serve the score. It will read the score from the scores file
# and will return an HTML that will be as follows:

hst = '0.0.0.0'
pt = '30000'
app = Flask(__name__, template_folder='.', static_folder='css')


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


def init_http():
    http = '''
            <html>
        <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link rel="stylesheet" href="/css/style.css" />
        <title>Scores Game</title>
        </head>
        <h1> Winning Score Board </h1>
        <body>
            <table class="table table-hover table-dark table-bordered">
                <thead>
                    <tr >
                        <th scope="col" class="col-sm-1" >1234</th>
                        <th scope="col" class="col-sm-12" ></th>
                        <th scope="col" class="col-sm-1" >1234</th>
                    </tr>
                </thead>
                <hr>
                <tbody>
        '''
    return http


def success(http, file):
    print("suc2")
    number_td = ''
    name_td = ''
    score_td = ''
    ind = 0
    print("suc3")
    try:
        for line in file:
            print("suc4", ind)
            if ind == 0:
                ind += 1
                continue
            else:
                (key, value) = line.split()
                print(f'key - {key} , value - {value} , index - {ind}')
                tmp_name = key
                SCORE = value
                http += f'''<tr class="hvr" ><th scope="row" class="ctr">#{ind}</th><td > {tmp_name} </td><td class="ctr2"> {SCORE} </td></tr>\n'''
                ind += 1
    except Exception as e:
        print('Error', e)

    print("suc4")
    return http


def error(http, err):
    http += f'''<tr style="background-color:#E78587; height:250px"><th scope="row" ></th><td style="font-size:32px;  text-align:center"> {err} </td><td ></td></tr>\n'''
    return http


def done(http):
    http += '''
              </tbody>
              </table>
              </body>
              </html>
              '''
    return http


@app.route("/")
def score_server_run():
    http = init_http()
    ERROR = """ERROR  -                          
    
    The score file does not exists"""

    try:
        file = open('Scores.txt')
        print("suc1")
        http_success = success(http, file)
        http_done = done(http_success)
        print(http_done)
        file.close()
        f = open('index.html', 'w+')
        f.write(http_done)
        f.close()
    except Exception as e:
        print(f'error {e}')
        http_error = error(httpp, ERROR)
        http_done = done(http_error)
        f = open('index.html', 'w+')
        f.write(http_done)
        f.close()
    finally:

        return render_template('index.html')


def score_server():
    app.run(host=hst, port=pt, debug=True)
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
# </html>
