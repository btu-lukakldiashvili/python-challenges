import urllib.request

template_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

remove_txt = "and the next nothing is "

def fetch(number, count):
    print(str(number))
    html = str(urllib.request.urlopen(template_url + str(number)).read().decode())

    if count >= 400:
        return html

    if remove_txt in html:
        try:
            f = int(html.replace(remove_txt, ''))

            return fetch(int(html.replace(remove_txt, '')), count+1)
        except:
            return html


# for num in range(0, 400):
print(fetch(63579, 0))


