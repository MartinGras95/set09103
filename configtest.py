import ConfigParser

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello Napier from the configuration testing app"

@app.route('/config/')
def config():
    str1 = []
    str1.append('Debug:'+str(app.config['DEBUG']))
    str1.append('port:'+app.config['port'])
    str1.append('url:'+app.config['url'])
    str1.append('ip_address:'+app.config['ip_address'])
    return '\t'.join(str1)

def init(app):
    config = ConfigParser.ConfigParser()
    try:
        print "sads"
        config_location = 'static/etc/defaults.cfg'
        print "sads"
        print config_location
        config.read(config_location)
        print "sads"

        app.config['DEBUG'] = config.get("config","debug")
        app.config['ip_address'] = config.get("config","ip_address")
        app.config['port'] = config.get("config","port")
        app.config['url'] = config.get("config","url")
    except:
        print "Could not read configs from: ", config_location

if __name__ == '__main__':
    init(app)
    app.run(
            host=app.config['ip_address'],
            port=int(app.config['port']))

