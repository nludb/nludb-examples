from typing import Dict
from steamship import Steamship, EmbeddingIndex

from nludb.server import App, Response, Error, Request, post, create_lambda_handler

class QuestionAnswer(App):
  def __init__(self, client: Steamship):
    # In production, the lambda handler will provide an NLUDB client:
    # - Authenticated to the appropriate user
    # - Bound to the appropriate space
    self.client = client

    # Create an embedding index using (for now!) our
    # mock embedder.
    #
    # Note that the *scope* of this index is limited to the space
    # this app is executing within. Each new instance of the app
    # will resultingly have a fresh index.
    self.index = self.nludb.create_index(
      handle="qa-index",
      model="test-embedder-v1"     
    ).data
  
  @post('learn')
  def learn(self, fact: str = None) -> Response:
    """Learns a new fact."""
    if fact is None:
      return Error(message="Empty fact provided to learn.")
   
    if self.index is None:
      return Error(message="Unable to initialize QA index.")

    res = self.index.embed(fact)

    if res.error:
      # Steamship error messages can be passed straight
      # back to the user
      return Error(
        message = res.error.message,
        suggestion = res.error.suggestion,
        code = res.error.code
      )
    
    return Response(json=res.data)

  @post('query')
  def query(self, query: str = None, k: int = 1) -> Response:
    """Learns a new fact."""
    if query is None:
      return Error(message="Empty query provided.")
    
    if self.index is None:
      return Error(message="Unable to initialize QA index.")

    res = self.index.query(query=query, k=k)

    if res.error:
      # Steamship error messages can be passed straight
      # back to the user
      return Error(
        message = res.error.message,
        suggestion = res.error.suggestion,
        code = res.error.code
      )
    json=res.data)
    return Response(


handler = create_lambda_handler(QuestionAnswer)



