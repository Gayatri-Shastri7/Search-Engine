from flask import Flask,jsonify,request
from string import Template
import requests
import json
from project import show_skills

app=Flask(__name__)
@app.route('/description',methods=['GET','POST'])

def index():
   if(request.method=='POST'):
      _input = request.json
      desc=_input['desc'] if _input.get('desc') else ''
      result = {}
   else:
      return "Method is get"
   result = show_skills(desc)
   return jsonify(result)

if __name__=='__main__':
   app.run('0.0.0.0', port=5000)