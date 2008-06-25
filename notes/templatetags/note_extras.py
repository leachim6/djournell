from django import template

register = template.Library()

def import_greybox():
    return """
    <script type="text/javascript">
        var GB_ROOT_DIR = "http://localhost:8000/public/gb/greybox";
    </script>
    <script type="text/javascript" src="/public/gb/greybox/AJS.js"></script>
    <script type="text/javascript" src="/public/gb/greybox/AJS_fx.js"></script>
    <script type="text/javascript" src="/public/gb/greybox/gb_scripts.js"></script>
    <link rel="stylesheet" type="text/css" href="/public/greybox/gb_styles.css" />
    """

def import_iui():
    return """
    <script type="javascript" src="/public/iui/iui.js"></script>
    <script type="javascript" src="/public/iui/iuix.js"></script>
    <link rel="stylesheet" src="/public/iui/iui.css" />
    <link rel="stylesheet" src="/public/iui/iuix.css" />
    """

def import_mootools():
    return """
    <script type="text/javascript" src="/public/mootools.js"></script>
    """
def import_topbar_css():
    return """
    <link rel="stylesheet" href="/public/topbar.css" type="text/css" />
    """
def topbar():
    return """
    <div id="topbar">
     <ul id="topbar-links">
       <li><a href="/">Home</a></li>
       <li><a href="/admin">Admin</a></li>
       <li><a href="/about">About</a></li>
     </ul>
     </div>
<div id="topbar_handle">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    </div>
     """

register.simple_tag(import_greybox)
register.simple_tag(import_iui)
register.simple_tag(import_mootools)
register.simple_tag(import_topbar_css)
register.simple_tag(topbar)
