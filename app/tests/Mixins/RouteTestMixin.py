from django.urls import reverse


# Mixin for testing the creation of routes
# HTTP request objects should be in the form [GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, TRACE]

class RouteTestingMixin(object):
    # Verifies a route exists
    def test_route_exists(self):
        response = self.client.get(reverse(self.route_name))
        self.assertEqual(response.status_code, 200)

    def test_route_get(self):
        request = self.factory.get(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[0],
                         "your get method for route: " + self.route + " returned a different status code")

    def test_route_post(self):
        request = self.factory.post(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[1],
                         "your post method for route: " + self.route + "returned a different status code")

    def test_route_put(self):
        request = self.factory.put(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[2],
                         "your put method for route: " + self.route + "returned a different status code")

    def test_route_patch(self):
        request = self.factory.patch(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[3],
                         "your patch method for route: " + self.route + "returned a different status code")

    def test_route_delete(self):
        request = self.factory.delete(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[4],
                         "your delete method for route: " + self.route + "returned a different status code")

    def test_route_head(self):
        request = self.factory.head(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[5],
                         "your head method for route: " + self.route + "returned a different status code")

    def test_route_options(self):
        request = self.factory.options(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[6],
                         "your options method for route: " + self.route + "returned a different status code")

    def test_route_trace(self):
        request = self.factory.trace(self.route)
        response = self.view(request)
        self.assertEqual(response.status_code, self.responses[7],
                         "your options method for route: " + self.route + "returned a different status code")
