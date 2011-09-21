import re

header = """<html><head>
    <link rel="stylesheet" type="text/css"
        href="blueprintcss/typography.css"/>
    <link rel="stylesheet" type="text/css"
        href="blueprintcss/grid.css"/>
    <title>{title}</title>
</head><body>
    <div class="container" id="main">
        <h1 id="title">{title}</h1>
        <h3>who asked to be indexed</h3>
        <div class="span-5 colborder" id="sidebar">
"""


def sanitize_tag(t):
    return re.sub('[^a-zA-Z_]', '', t)

def write_header(f):
    t = "R&eacute;sum&eacute;s of Hacker Society Members"
    f.write(header.format(title=t))

def write_tag(f, tag):
    f.write('<a href="#{0}">{1}</a><br/>'.format(sanitize_tag(tag), tag))

def write_separator(f):
    f.write('</div><div class="span-18 last" id="content">')

def write_tag_header(f, tag):
    f.write('<h3><a name="{0}">{1}</a></h3>'.format(sanitize_tag(tag), tag))

def write_person_link(f, p):
    f.write('<li><a href="#{0}">{1}</a></li>'.format(sanitize_tag(p.name), p.name))

def write_page_divider(f):
    f.write("<br/><hr/>")

def write_person(f, p):
    f.write('<h3><a name={0} href="mailto:{p.email}">{p.name}</a></h3>'.format(sanitize_tag(p.name), **locals()))
    f.write('Major: {p.major}<br/>Tags: {p.tags}<br/><a href="{p.url}">R&eacute;sum&eacute;</a><br/>'.format(**locals()))

def write_footer(f):
    f.write("<br/><br/>Steve Johnson put this page together this year, but you can't hire him because he's got a job already ;-)</div></div></div></div></body></html>")

tag_lists = [
 [
 'bash',
 'bson',
 'c',
 'c#',
 'c++',
 'comptia a+',
 'css',
 'easy c',
 'glsl',
 'html',
 'java',
 'javascript',
 'json',
 'labview',
 'latex',
 'mathematica',
 'matlab',
 'neuron',
 'objective-c',
 'php',
 'python',
 'robot c',
 'ruby',
 'silverlight',
 'spss',
 'sql',
 'verilog',
 'x86 assembly',
 ],
 [
 'lamp',
 'mongodb',
 'mysql',
 'ruby on rails',
 'web applications',
 'web back end',
 'web design',
 'web development',
 'web front end',
 ],
 [
 'artificial intelligence',
 'bioinformatics',
 'biomechanics',
 'compilers',
 'computational intelligence',
 'computational modeling',
 'computational neuroscience',
 'design',
 'embedded',
 'french',
 'games',
 'graphic design',
 'image processing',
 'linear systems',
 'machine learning',
 'mobile robotics',
 'monte carlo simulations',
 'networks',
 'physics',
 'project management',
 'robot manipulators',
 'robotics',
 'systems',
 ],
 [
 '.net',
 'android',
 'cocoa',
 'game maker',
 'ios',
 'iphone',
 'matplotlib',
 'opengl',
 'xna'
 ],
 [
 'eclipse',
 'emacs',
 'excel',
 'git',
 'linux',
 'linux server administration',
 'mercurial',
 'office',
 'photoshop',
 'unix',
 'vim',
 'visual basic',
 'windows 8 app development',
 'windows server 2008 r2',
 ],
]
