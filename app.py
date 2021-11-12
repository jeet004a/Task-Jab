from flask import Flask, app,render_template , request,redirect,url_for
import os
from pprint import pprint
from google.cloud import storage

app=Flask(__name__)

@app.route('/')
def hello_admin():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'resourcebusy-testing-de7c29735b17.json'

    storage_client = storage.Client()

    filename='index.html'
    
    UPLOADFILE=os.path.join(os.getcwd(),filename)
    bucket=storage_client.get_bucket('resoucebusyjeet12345')
    blob=bucket.blob(filename)
    blob.upload_from_filename(UPLOADFILE)
    
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)