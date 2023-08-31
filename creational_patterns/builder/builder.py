"""
BUILDER DESIGN PATTERN
-------------------------
why?
- we need it when we need several statement to construct something

"""

class HtmlElement:
    indent_size = 2
    def __init__(self,name:str="", text:str=""):
        self.name = name
        self.text = text
        self.elements = []
    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            il = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{il}{self.text}')
        for e in self.elements:
            lines.append(e.__str(indent+1))
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    def __str__(self) -> str:
        return self.__str(0)
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self,root_name) -> None:
        self.root_name = root_name
        self.__root.name = root_name

    # fluent design
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name,child_text)
        )
        return self
    
    def __str__(self):
        return str(self.__root)
    
builder = HtmlElement.create('ul')
builder.add_child('li','item 1')\
    .add_child('li','item2')\
    .add_child('li','item 3')
print(builder)
        
            