from flask import Flask

app = Flask(__name__)

@app.route('/<int:num>')
def server(num):
    fb_res = fb(num)
    return {"result": fb_res}

def fb(value):
    if value % 15 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
 
    return value