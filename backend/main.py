#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     启动后台服务
#
#  Author:      半片叶
#
#  Created:     2020.08.11
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# import graphene
# from starlette.graphql import GraphQLApp



# class Query(graphene.ObjectType):
#     hello = graphene.String(name=graphene.String(default_value="stranger"), password=graphene.String(default_value="admin"))
#     qu = graphene.String(username=graphene.String(default_value="root"))
#     def resolve_hello(self, info, name, password):
#         return "Hello " + name + password
#
#     def resolve_qu(self, info, username):
#         return username
#
# app.add_route("/ql", GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8668)