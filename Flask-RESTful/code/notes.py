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