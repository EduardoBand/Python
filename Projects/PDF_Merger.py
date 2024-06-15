#pip istall pypdf

from pypdf import PdfWriter

pdfs = ['A.pdf', 'B.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write('result.pdf')
merger.close()


"""
If you wish to control which pages are appended from a particular file, you can use the pages keyword argument of append and merge, passing a tuple in the form (start, stop[, step]) (like the regular range function).
e.g.

merger.append(pdf, pages=(0, 3))    # first 3 pages
merger.append(pdf, pages=(0, 6, 2)) # pages 1,3,
"""