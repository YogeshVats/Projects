# Q. What is the http status code for creation ?
# A. It is 201 (CREATED).

# Q. What 202 http status code means ?
# A. 202 means accepted, and the accepted code is when you are delaying the creation. For e.g., if
# the objct creation takes a long time you may say "I'am gonna create this object, return 202 
# and the obect gets created then after 5 or 10 minutes". The client doesn't have to wait 5 or 10 minutes,
# but it knows that you have accepted the creation of that. It may then fail but that's out with
# the client's control.

# Using a corret status code is very important because it is a very quick way of clients like 
# web applications or mobile applications to check whether things went wrong or not. E.g. in the case 
# of 404 we don't even need to check the payload because we know that nothing's coming back that we are 
# really interested in. If 201 comes back then we need to check the payload to see what has been created.

# JWT stands for JSON Web Token. And essentially all that is an obfuscation of data. And that is we are
# gonna be encoding some data and that's a JSON Web Token. 
# For example: If I want to send you a private message that says "Hello", and I don't want anybody else to be
# able to see it, I can encode that message so that nobody else can understand it unless they have a 
# particular decryption key, so a way to decrypt it.  

# login flow and user session: 
# We are going to be doing that but with user IDs. So a user is going to be an entity that has a unique 
# identifying number and a username and a password. The user is going to send us a username and a password, 
# and we are going to send them, the client really, a JWT. And that JWT is going to be the user ID. When the 
# client has the JWT, they can send it to us with any request they make. And when they do that it's going to 
# tell us that they have previously authenticated, that means they are logged in.

# the payload is the contents of the JWT token and the identity function is unique to flask JWT 
# extension that we have installed.

# We used "_id" because "id" is a keyword in Python. We can import the user file in security file because they 
# are in the same directory in which we are in. by doing "from user import User".

# Sometimes string comparing in Python might throw error because of encodings, different versions etc, so we 
# need to compare strings safely and flask's "werkzeug" library has a "safe_str_cmp" method to compare strings 
# safely in all different encodings and Python versions. This is deprecated now so look for a better option.

# JWT creates a new endpoint and that endpoint is '/auth'. When we call '/auth' we send it a username and a 
# password and the JWT extension gets that username and password and sends it over to the authenticate 
# function, that takes in a username and a password. We are then going to find the correct user object using 
# that username and then we are going to compare its password to the one that we receive through the auth 
# endpoint. If they match we are going to return the user and that becomes sort of the identity. So what 
# happens next is the auth endpoint returns a JW Token. Now that JW Token in itself doesn't do anything, but 
# we can send it to the next request we make. So when we send a JW Token what JWT does is it calls the identity
# function and then it uses the JW Token to get the user ID and with that it gets the correct user for that 
# user ID that the JWT token represents. And if it can do that, that meas the user was authenticated, the JWT 
# is valid, and all is good.

# Logged in to a server means can you prove you are somebody. And we can prove it if we send in this 
# authorization header. Flask JWT is going to look at the authorization header, its going to understand that 
# we are a user and with this its going to decode it. It's going to retrieve a user ID from it, and in our 
# security file, it's going to call the identity payload, its going to get the user ID, and then it's going to 
# get the correct user for that ID. And because that user does exist, "bob" and "asdf", then it knows that we 
# are logged in and then we run get method of Item class.

# put method can be called multiple time but the outcome should remain same for same data. It can be used to create or update existing data.