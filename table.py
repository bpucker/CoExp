### Andreas Rempel ###
### andreas.rempel@uni-bielefeld.de ###
### v0.24 ###

class text_open:
  def __enter__(self):
    return self
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()
  
  def __init__(self, name, mode='w'):
    self.file = open(name, mode)
  
  def add_header(self, *args):
    self.file.write(f'{"	".join(f"{arg}" for arg in args)}\n' )
  def add_row(self, *args):
    self.file.write(f'{"	".join(f"{arg}" for arg in args)}\n' )
  
  def close(self):
    self.file.close()

## - # - # - # - # - # - # - # - # - ##

class html_open:
  def __enter__(self):
    return self
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()
  
  def __init__(self, name, mode='w'):
    self.file = open(name, mode)
    self.file.write( '<html>\n' )
    self.file.write( '  <style>\n' )
    self.file.write( '    @import url("https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap");\n' )
    self.file.write( '    table {\n' )
    self.file.write( '      width: 100%;\n' )
    self.file.write( '      border-collapse: collapse;\n' )
    self.file.write( '      font-family: "Source Code Pro", monospace;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    table, th, td {\n' )
    self.file.write( '      border: 1px solid #ddd;\n' )
    self.file.write( '      padding: 8px;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    th {\n' )
    self.file.write( '      padding-top: 12px;\n' )
    self.file.write( '      padding-bottom: 12px;\n' )
    self.file.write( '      text-align: left;\n' )
    self.file.write( '      background-color: #004080;\n' )
    self.file.write( '      color: white;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    tr:nth-child(even) {\n' )
    self.file.write( '      background-color: rgba(242, 242, 242, 0.1);\n' )
    self.file.write( '    }\n' )
    self.file.write( '    tr:nth-child(odd) {\n' )
    self.file.write( '      background-color: rgba(242, 242, 242, 0.3);\n' )
    self.file.write( '    }\n' )
    self.file.write( '    tr:nth-child(even):hover {\n' )
    self.file.write( '      background-color: rgba(242, 242, 242, 0.7);\n' )
    self.file.write( '    }\n' )
    self.file.write( '    tr:nth-child(odd):hover {\n' )
    self.file.write( '      background-color: rgba(242, 242, 242, 0.9);\n' )
    self.file.write( '    }\n' )
    self.file.write( '    .filter {\n' )
    self.file.write( '      width: 100%;\n' )
    self.file.write( '      display: flex;\n' )
    self.file.write( '      justify-content: flex-end;\n' )
    self.file.write( '      align-items: center;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    label {\n' )
    self.file.write( '      margin-right: 10px;\n' )
    self.file.write( '      font-family: "Source Code Pro", monospace;\n' )
    self.file.write( '      font-size: 1em;\n' )
    self.file.write( '      color: #333;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    select {\n' )
    self.file.write( '      border: 1px solid #ddd;\n' )
    self.file.write( '      border-radius: 4px;\n' )
    self.file.write( '      padding: 8px;\n' )
    self.file.write( '      font-family: "Source Code Pro", monospace;\n' )
    self.file.write( '      font-size: 1em;\n' )
    self.file.write( '      background-color: #f9f9f9;\n' )
    self.file.write( '      color: #333;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    select:focus {\n' )
    self.file.write( '      border-color: #004080;\n' )
    self.file.write( '      outline: none;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    a:link {\n' )
    self.file.write( '      color: #1529E1;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    a:link:hover {\n' )
    self.file.write( '      color: #2337EE;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    a:link:active {\n' )
    self.file.write( '      color: #091DD5;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    a:visited {\n' )
    self.file.write( '      color: #563FAC;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    a:visited:hover {\n' )
    self.file.write( '      color: #644DB9;\n' )
    self.file.write( '    }\n' )
    self.file.write( '    a:visited:active {\n' )
    self.file.write( '      color: #4B349F;\n' )
    self.file.write( '    }\n' )
    self.file.write( '  </style>\n' )
  
  def begin_section(self, title, list):
    self.section = title
    self.file.write( '  <script>\n' )
    self.file.write(f'    function select{self.section}() {{\n' )
    self.file.write(f'      let {title}Select = document.getElementById("{self.section}Select");\n' )
    self.file.write(f'      let {title}Tables = document.getElementsByClassName("{self.section}Table");\n' )
    self.file.write(f'      for (let {title}Table of {title}Tables) {title}Table.hidden = true;\n' )
    self.file.write(f'      document.getElementById({title}Select.value).hidden = false;\n' )
    self.file.write( '    }\n' )
    self.file.write( '  </script>\n' )
    self.file.write( '  <div class="filter">\n' )
    self.file.write(f'    <label for="{self.section}Select">{self.section}:</label>\n' )
    self.file.write(f'    <select id="{self.section}Select" onchange="select{self.section}();">\n' )
    for id in list:
      self.file.write(f'      <option value="{id}">{id}</option>\n' )
    self.file.write( '    </select>\n' )
    self.file.write( '  </div>\n' )
  
  def begin_table(self, id=None):
    if id and hasattr(self, "section"):
      self.file.write(f'  <table id="{id}" class="{self.section}Table">\n' )
    else:
      self.file.write( '  <table>\n' )
  
  def add_header(self, *args):
    self.file.write(f'    <tr>{"".join(f"<th>{arg}</th>" for arg in args)}</tr>\n' )
  def add_row(self, *args):
    self.file.write(f'    <tr>{"".join(f"<td>{arg}</td>" for arg in args)}</tr>\n' )
  
  def end_table(self):
    self.file.write( '  </table>\n' )
  
  def end_section(self):
    self.file.write( '  <script>\n' )
    self.file.write(f'    select{self.section}();\n' )
    self.file.write( '  </script>\n' )
    del self.section
  
  def close(self):
    self.file.write( '</html>\n' )
    self.file.close()
