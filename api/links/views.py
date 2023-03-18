from flask_restx import Namespace, Resource
from ..database.db import database

links_namespace = Namespace('links', description="a namespace for links")


@links_namespace.route('/<string:app_id>')
class GetUrl(Resource):
    @links_namespace.doc(
        description="Retrieve all orders",
        params={
            "app_id": "An ID for a given app"
        }
    )
    def get(self, app_id):
        """
        :param app_id:
        :return json with url, status and id:

        """
        data = dict(database.child('urls').child(app_id).get().val())
        print(data)
        return data
