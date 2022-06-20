# flaskHelloWorld
Hello World in Python-Flask


pre-requisite :
 - download & install OS compatible version of python from https://www.python.org/downloads/
 - once done , windows user can verify the installation by running the command "python --version" in command prompt 
    
    <img width="499" alt="image" src="https://user-images.githubusercontent.com/54891488/174519402-b9b08845-6acc-4771-a163-2a7b251944d5.png">
    
 - download the source from repo and unzip into desired location

folder structure :
  - python-flask app follows a simple folder structure 
  - project name "HELLOWORLDPYTHON"
    - app.py   
    - templates
      -   index.html
    - static
      -   img
      -   media   
      -   style.css    ## could be also placed under a sub-folder css

running the app:
  - open the command prompt in the same location where app.py file exist in the downloaded folder 
  - run the command "python .\app.py" from the command prompt 
    
    <img width="639" alt="image" src="https://user-images.githubusercontent.com/54891488/174519609-07c0e6be-f1d0-4edf-a19a-341c1940bb79.png">
    
  - goto browser 
    -  type the url "http://127.0.0.1:5000/"        ## html page content will be rendered from index.html
    -  type the url "http://127.0.0.1:5000/hello"   ## static text from the hello() function of app.py will be rendered 

Extension /Excercise :
  - Create a new html page contactMe.html to render the below form  
    -  ![image](https://user-images.githubusercontent.com/54891488/174520356-cda759b0-3a73-45b4-95d3-5954bb81c25f.png)
  - Create a new route in app.py called contactMe()  
    -  Code Hint 
        ## @app.route('/ContactMe')   
        ## def ContactMePage():
        ##   return render_template("ContactMe.html")



