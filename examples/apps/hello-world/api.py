from typing import Dict
from nludb.server import App, Response, Request, post, create_lambda_handler

class HelloWorld(App):
  @post('greet')
  def greet(self, name: str = "Person") -> Response:
    return Response(string='Hello, {}'.format(name))

handler = create_lambda_handler(HelloWorld())
