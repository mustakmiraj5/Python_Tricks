# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Miraj",
    590: "Emon",
    951: "Mobin",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
# "Hi Alice!"

print(greeting(333333))
# "Hi there!"