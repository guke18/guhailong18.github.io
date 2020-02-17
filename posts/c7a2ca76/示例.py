from lxml import etree
text = '''
<div>
<ul>
<li class="book-0"><a href="link.html">first item </a></li>
<li class="book-1"><a href="link.html">second item </a></li>
<li class="book-000"><a href="link.html">third item </a></li>
<li class="book-1"><a href="link.html">fourth item </a></li>
<li class="book-0"><a href="link.html">fifth item </a></li>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))