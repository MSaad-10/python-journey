"""
    - A simple html file is given.
    - You have to extract the links from the html file and write them to a text file named 'links.txt'.
"""


# ============= Solution 1 =============
with (
    open('Ex_03.html', 'r', encoding='utf-8') as htmlf,
    open('links.txt', 'a', encoding='utf-8') as lf,
):
    for line in htmlf.readlines():
        if '<a href=' in line:
            pos = line.find('<a href=')
            first_quote = line.find('\"', pos)
            second_quote = line.find('"', first_quote+1)
            url = line[first_quote+1:second_quote]
            lf.write(f'{url}\n')


# ============= Solution 2 =============
with (
    open('Ex_03.html', 'r', encoding='utf-8') as htmlf,
    open('links.txt', 'a', encoding='utf-8') as lf,
):
    page = htmlf.read()
    link_exist = True
    while link_exist:
        pos = page.find('<a href=')
        if pos == -1:
            link_exist = False
            break
        else:
            first_quote = page.find('\"', pos)
            second_quote = page.find('"', first_quote+1)
            url = page[first_quote+1:second_quote]
            lf.write(f'{url}\n')
            page = page[second_quote+1:]