from flask import Flask, render_template
from GameServer.Utils import BAD_RETURN_CODE
import glob, os
# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.

# Methods
# 1. score_server - This function will serve the score. It will read the score from the scores file
# and will return an HTML that will be as follows:

hst = '0.0.0.0'
pt = '30000'
app = Flask(__name__, template_folder='.', static_folder='css')
file_name = "../GameServer//Scores.txt"
path_files = "../GameServer"
webpath = "../WebClient"
web_file_name = "index.html"


def init_file():
    pattern = "*.txt"
    os.chdir(path_files)
    os.getcwd()
    files = glob.glob(pattern)
    if len(files) > 0:
        files.sort(key=lambda x: os.path.getmtime(x))
        lastfile = files[len(files)-1]
        print("Most recent file matching {}: {}".format(pattern, lastfile))
        file_name = lastfile
        return file_name
    else:
        return False


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
    http = f'''
            <html>
        <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link rel="stylesheet" href="/css/style.css" />
         <meta http-equiv="refresh" content="2; URL=/">

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
    number_td = ''
    name_td = ''
    score_td = ''
    ind = 0
    for line in file:
        if ind == 0:
            ind += 1
            continue
        else:
            last = len(line.split())
            i = 0
            tmp = ''
            laststr = ''
            for u in line.split():
                if i == last - 1:
                    laststr = u
                    break
                else:
                    tmp += u + ' '
                i += 1
            #print(f'tmp - {tmp}, // laststr - {laststr}')
            (key, value) = (tmp, laststr)
            tmp_name = key
            SCORE = value
            http += f'''<tr class="hvr" ><th scope="row" class="ctr">#{ind}</th><td > {tmp_name} </td><td class="ctr2"> {SCORE} </td></tr>\n'''
            ind += 1
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
    file_names = init_file()
    ERROR = f"""ERROR  -  {BAD_RETURN_CODE}"""
    os.chdir(webpath)
    os.getcwd()
    try:
        file = open(file_name)
        http_success = success(http, file)
        http_done = done(http_success)
        file.close()
        f = open(web_file_name, 'w+')
        f.write(http_done)
        f.close()
    except Exception as e:
        print(f'error {e}')
        ERROR = str(e)
        http_error = error(http, ERROR)
        http_done = done(http_error)
        f = open(web_file_name, 'w+')
        f.write(http_done)
        f.close()
    finally:

        return render_template(web_file_name)


def score_server():
    app.run(host=hst, port=pt, debug=True)
