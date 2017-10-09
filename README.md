# python-codepen
A Python wrapper for the unofficial CodePen API.

This library is a pure Python interface for the
[unofficial CodePen API](http://cpv2api.com/). It provides functionalities to
retrieve data for pens, blog posts, collections, and user profiles on
the CodePen website. Python versions 2.7+ and 3 are supported.

## Installation
Install using pip:
```
$ pip install codepen
```

## Basic Usage
```python
from codepen import User

user = User('connorkendrick')

# Get user's profile data
data = user.profile()

# Print profile data
for key in data:
    print(key + ': ' + str(data[key]))
```

## Models and Documentation
This library utilizes models to retrieve and represent various
groups of data returned by the API.  
These models are:
* codepen.Pens
* codepen.Posts
* codepen.Collections
* codepen.User
* codepen.Search

To read the documentation for any of these models, run:
```
$ pydoc codepen.[model]
```

## Local Development
Check out the latest development build:
```
$ git clone https://github.com/connorkendrick/python-codepen.git
$ cd python-codepen
```

Install dependencies:
```
$ pip install -r requirements.txt
```

Make changes, then run the test suite:
```
$ py.test
```

## Examples
Let's write a script that determines if any of our pens made the front page:
```python
from codepen import Pens

pens = Pens()

# Get a list of pens on page 1 of the 'picked pens' category
front_page = pens.list(category='picks')

# Search each pen's data for our username
for pen in front_page:
    if pen['user']['username'] == 'connorkendrick':
        print("Your pen made the front page! Way to go!")
```

Let's write one more script that's a little more complex. This script will
determine the average number of followers for users who are on the second page
of the 'picked posts' category:
```python
from codepen import Posts, User

posts = Posts()

# Get a list of blog posts on page 2 of the 'picked posts' category
picked_posts = posts.list(category='picks', page=2)

total_followers = 0

# For each post, get the user's follower count and add to a total
for post in picked_posts:
    # Create User object using the username in each post's data
    user = User(post['user']['username'])
    data = user.profile()
    # Remove commas from follower count and convert to int
    total_followers += int(data['followers'].replace(',', ''))

average_followers = total_followers // len(picked_posts)

print("Users on the second page of picked posts have an average of "
      + str(average_followers) + " followers.")
```

### License
This project is licensed under the MIT License. See the [LICENSE.md](https://github.com/connorkendrick/python-codepen/blob/master/LICENSE)
file for more information.

### Credits
* @natewiley for creating and providing the [API](https://github.com/natewiley/cpv2api)
* [CodePen](https://codepen.io/) for providing an amazing platform for front-end tech
