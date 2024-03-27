    from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
  return '<center><h1>Rodriguez Loaya Maik</h1><img src="https://ih1.redbubble.net/image.571103176.4760/st,small,845x845-pad,1000x1000,f8f8f8.u4.jpg"><h2>Maik</h2></center>'

if __name__=="__main__":
  app.run(debug = True)
    
   