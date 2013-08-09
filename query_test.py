# do some queries and make stuff happen!
import model 

user_list = model.session.query(model.user).all()
print user_list

