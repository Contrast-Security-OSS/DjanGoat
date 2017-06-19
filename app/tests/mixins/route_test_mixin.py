from django.urls import reverse


# Mixin for testing the creation of routes
# Make sure your kwargs match your variable argument
class RouteTestingWithKwargs(object):
    # Verifies a route exists
    def test_route_exists(self):
        response = self.client.get(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_route_get(self):
        request = self.factory.get(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['GET'],
                         "your get method for route: " + self.route + " returned: " + str(response.status_code))

    def test_route_post(self):
        request = self.factory.post(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['POST'],
                         "your post method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_put(self):
        request = self.factory.put(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['PUT'],
                         "your put method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_patch(self):
        request = self.factory.patch(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['PATCH'],
                         "your patch method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_delete(self):
        request = self.factory.delete(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['DELETE'],
                         "your delete method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_head(self):
        request = self.factory.head(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['HEAD'],
                         "your head method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_options(self):
        request = self.factory.options(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['OPTIONS'],
                         "your options method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_trace(self):
        request = self.factory.trace(self.route)
        response = self.view(request, **self.kwargs)
        self.assertEqual(response.status_code, self.responses['TRACE'],
                         "your options method for route: " + self.route + "returned: " + str(response.status_code))
