
import re
from flask import escape
from system.core.controller import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Welcome(Controller):

    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
    
    def index(self):
        #if 'user_id' in session and 'name' in session:
        #    return self.load_view('success.html',id=id)
        user= self.models['WelcomeModel'].get_product()
        return self.load_view('index.html',user=user)

    def product_new(self):
        return self.load_view('productnew.html')

    def product_show(self,id):
        session['id']=id
        #print session['id']
        product=self.models['WelcomeModel'].get_id(id)
        return self.load_view('productInfo.html',id =session['id'], product = product)

    def product_edit(self,id):
        session['id']=id
        #print id
        product=self.models['WelcomeModel'].get_id(id)
        return self.load_view('productedit.html',id =session['id'], product = product)

    def product_update(self,id):
        session['id']=id
        name=request.form['name']
        description=request.form['description']
        price=request.form['price']
        product_update=self.models['WelcomeModel'].update_info(id, name, description, price)
        return redirect('/')

    def create(self):
        #print "welcome#create"
        session['name']=request.form['name'] 
        session['description']=request.form['description']
        session['price']=request.form['price']
        #print session['name']
        self.models['WelcomeModel'].add_product(session['name'],session['description'],session['price'])
        user= self.models['WelcomeModel'].get_product()

    def delete (self, id):
        session['id']=id
        print session['id']
        self.models['WelcomeModel'].delete(id)
        return redirect('/')
               
    
        

