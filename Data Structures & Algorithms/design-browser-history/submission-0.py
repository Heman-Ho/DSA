class Node:
    def __init__(self, url, num):
        self.url = url
        self.next = None
        self.prev = None
        self.browser_num = num

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node("root", 0)
        self.head.next = Node(homepage, 1)
        self.head.next.prev = self.head
        self.cur_browser = self.head.next

    def visit(self, url: str) -> None:
        new_node = Node(url, self.cur_browser.browser_num + 1)
        new_node.prev = self.cur_browser
        self.cur_browser.next = new_node
        self.cur_browser = self.cur_browser.next

    def back(self, steps: int) -> str:
        for _ in range(min(steps, self.cur_browser.browser_num - 1)):
            self.cur_browser = self.cur_browser.prev
        return self.cur_browser.url
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.cur_browser.next:
                return self.cur_browser.url

            self.cur_browser = self.cur_browser.next
        return self.cur_browser.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)