def user_schemas(user) -> dict:
    return{"id": str(user["_id"]),
           "username": user["username"],
           "email": user["email"]}
    
def users_schemas(users) -> list:
    return [user_schemas(user) for user in users]

   