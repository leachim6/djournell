from django import template

register = template.Library()

def import_thickbox():
    return """
    <script type="text/javascript" src="/public/thickbox/jquery.js"></script>
    <script type="text/javascript" src="/public/thickbox/thickbox.js"></script>
    <link rel="stylesheet" href="/public/thickbox/thickbox.css" type="text/css" media="screen" />
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

register.simple_tag(import_thickbox)
register.simple_tag(import_topbar_css)
register.simple_tag(topbar)
