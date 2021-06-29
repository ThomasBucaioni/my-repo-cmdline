import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    m = re.findall('[0-9]{2}:[0-9]{2}', course)
    print('1:', m)


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    print(tweet)
    m = re.findall('(http:\S*\/?)|(#\S*){1}', tweet)
    L = []
    for item in m:
        if item[0]:
            L.append(item[0])
        if item[1]:
            L.append(item[1])
    print('2:', L)


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    m = re.search('<p>(.*?)</p>', html)
    print('3:', m[1])


extract_course_times()
get_all_hashtags_and_links()
get_all_hashtags_and_links(('PyBites My Reading List | 12 Rules for Life - #books '
                 'that expand the mind! '
                 'http://pbreadinglist.herokuapp.com/books/'
                 'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
                 ' #psychology #philosophy'))
match_first_paragraph()
