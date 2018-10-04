import falcon


class Get_Characters:
	
	def on_get(self, req, resp):
		query = req.get_param("company")
		if query == "Marvel":
			resp.body = "Iron Man, Thor"
		else:
			resp.body = "Bat man, Joker"



api = falcon.API()

api.add_route("/characters",Get_Characters())
