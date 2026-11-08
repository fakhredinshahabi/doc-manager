# from fastapi import APIRouter
# from app.store import USERS,find_user_by_id
# routers=APIRouter(prefix="/users",tags=["users"])
# @routers.get('')
# def get_users():
#     return USERS
# @routers.get('/search')
# def serc_in_users(text:str,limit:int=10,page:int=1):
#     skip=(page-1)*limit
#     list_users=USERS
#     if text:
#         list_users=[
#           user  for user in USERS
#             if text in user["full_name"]
#         ]
#         return list_users[skip:skip+limit]
#     return list_users[skip:skip+limit]
# @routers.get('/{user_id}')
# def get_user_by_id(user_id:int):
#    return find_user_by_id(user_id)