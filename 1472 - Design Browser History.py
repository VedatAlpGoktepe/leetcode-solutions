# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:
  def __init__(self, homepage: str):
    self.page = 0
    self.history = [homepage]

  def visit(self, url: str) -> None:
    self.page += 1
    self.history = self.history[:self.page]
    self.history.append(url)

  def back(self, steps: int) -> str:
    self.page = max(0, self.page-steps)
    return self.history[self.page]

  def forward(self, steps: int) -> str:
    self.page = min(self.page+steps, len(self.history)-1)
    return self.history[self.page]