<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="static/images/movie.png" alt="Logo" width="80" height="80">

<h3 align="center">Actor Overlap</h3>

  <p align="center">
    A movie star trivia game!
    <br />
  </p>
</div>

#### Video Demo:  https://youtu.be/zhfVsKhxNv8

<!-- ABOUT THE PROJECT -->
## About The Project
Welcome to my CS50x final project! My idea was to create a movie trivia game where the player has to guess the shared name between two famous actors or directors. For example:

>Anna KENDRICK Lamar
<br/>Stockard CHANNING Tatum

The game provides the unshared names as well as headshots of each person as clues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Flask][Flask.com]][Flask-url]
* [![Sqlite][Sqlite.com]][sqlite-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Background

Like many people, I'm addicted to daily web games like Wordle and Connections, and I've always enjoyed movies, so I decided my project would be a marriage of the two in a way I hadn't seen done before. </br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Building the list
My first step was to create my list of actor/director pairs. To do this, I wrote a SQL query to access the movies.db database from week 7 of CS50x. It was... a little complex.
```
SELECT DISTINCT p2.name || p1.name
FROM (
    SELECT people.name
    FROM people
    JOIN stars ON people.id = stars.person_id
    JOIN movies ON stars.movie_id = movies.id
    JOIN ratings ON movies.id = ratings.movie_id
    WHERE movies.id IN (SELECT movie_id FROM ratings ORDER BY votes DESC LIMIT 5000)
) p1
JOIN (
    SELECT people.name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
JOIN ratings ON movies.id = ratings.movie_id
WHERE movies.id IN (SELECT movie_id FROM ratings ORDER BY votes DESC LIMIT 5000)
) p2 ON SUBSTR(p1.name, 1, INSTR(p1.name, ' ') - 1) = SUBSTR(p2.name, INSTR(p2.name, ' ') + 1);
```
Like I said, it's a lot. Because this database has no built in popularity metric for stars, I had to use the ratings metric for the actual films, which lead to some bloat in the query. It took about 10 minutes to generate (eek). </br>

In hindsight, I probably should've just used data from TMDB, which has built in popularity metrics on their persons data, but this was a good learning experience for complex queries. What wasn't fun was  going through ALL ~4500 pairs to weed out the unrecognizable names. I heard that the Wordle creator had to do something similar. No way around it but to go 'brute force'
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting photos

It was about here when I realized I'd want images, and after debating a few different techniques, I landed on using the TMDB api. It has an images endpoint based on their own TMDB person id's, so first I had to code my api request script. I thought about doing an api request each time a round was generated, but once I realized my actual list of actors was only about 500, I downloaded all of them at once into my own headshots directory.That way, in my table, I'd only have to have links to the image filepath for each person. Also, seeing that script fill my headshots folder with 500 images was VERY satisfying.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Building the database
Simultaneously I was building my SQLite database for the game itself. Decided to use a 3 table schema: person, pairs, and images.
```
CREATE TABLE person (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    TMDB_id INTEGER
);

CREATE TABLE image (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    filepath TEXT,
    person_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES person(person_id)
);

CREATE TABLE pairs (
    pairs_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id1 INTEGER,
    person_id2 INTEGER,
    shared_name TEXT,
    FOREIGN KEY (person_id1) REFERENCES person(person_id)
    FOREIGN KEY (person_id2) REFERENCES person(person_id)
);
```
 I found I preferred generating CSV's first so that I could easily look at the data before uploading to the database.
 <p align="right">(<a href="#readme-top">back to top</a>)</p>

## Building the front end

After that I began working on my Flask app. While I wanted to figure out how to make it a true SPA, I decided against learning AJAX for this project and focus on getting the game working. Maybe in the future I'll play with that. I borrowed a lot from the finance pset from Week 9, keeping the layout simple with bootstrap. Each 'turn' uses a SQL query to pull up a pair and generate the clues. Added what I call a 'quickplay' feature by letting the user toggle a new game quickly by hitting the enter button.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Final Thoughts

All in all, I'm happy with how this turned out. It was a good exercise in figuring out when to stop, to be honest. There are definitely  more features that could have been added, but the real goal was to build something complete I was proud of, and learn <b>some</b> new things along the way. The app itself isn't too complicated, but the setup, getting the images, building the database, that was where the bulk of the work ended up being focused, and I'm proud of the solutions I came up with. Initially didn't think I'd enjoy doing web dev, but building something you can use an interact with immediately, that is very satisfying.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Steven Bailey - [@IAMSTEVENBAILEY](https://twitter.com/IAMSTEVENBAILEY)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()Thank you to Harvard University for putting out such an INCREDIBLE resource!
* And thanks to <a href="https://github.com/othneildrew/Best-README-Template/pull/73">othneildrew</a> for the README template!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Sqlite.com]: https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[Sqlite-url]: https://sqlite.org
