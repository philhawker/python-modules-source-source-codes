class Html:
    def __init__(self, content):
        self.content = content

    def render(self):
        raise NotImplementedError('Subclass must implement render method')    # Raise creates an red error message in the console
    

class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'

        
class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'
        
tags = [    
    Div('some content'),
    Heading('some content'),
    Div('another div'),
]

for tag in tags:
    print(tag.render())