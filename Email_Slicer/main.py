def Email_slicer():

    email = input("Enter your E-mail:- ").strip()

    username = email[:email.index("@")]

    domainname = email[email.index("@")+1:]

    output1 = "Your username is:- {}".format(username)
    output2 = "Your Domain name is:- {}".format(domainname)
    print(output1 +"\n"+output2)

Email_slicer()