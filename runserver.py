'''startup the server'''
from portfolio import app

# Running test server
app.run(host='0.0.0.0', port=5000, debug=True)
