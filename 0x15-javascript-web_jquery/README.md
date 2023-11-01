# Project: 0x15. JavaScript - Web jQuery | ALX Africa Intranet

## Overview

This project focuses on enhancing front-end development skills with a focus on JavaScript and the jQuery library. It covers various tasks that involve DOM manipulation, event handling, and making asynchronous requests. The project aims to provide a solid understanding of JavaScript in the browser and the advantages of using jQuery.

## Concepts

For this project, the key concepts include:

- JavaScript in the browser: Understanding the evolution and challenges.
- Dealing with data statically versus dynamically.
- DOM manipulation and event handling.
- jQuery usage and its advantages.

## Resources

Read or watch the following resources to gain a deeper understanding of the concepts covered in this project:

- [What is JavaScript?](https://intranet.alxswe.com/rltoken/NJ5XM_fzjlBKERHTkdF-uA)
- [Selector Get and set content](https://intranet.alxswe.com/rltoken/wsnVUxEcAzzlCx6ES1qc7g)
- [Manipulate CSS classes](https://intranet.alxswe.com/rltoken/IcM5kKVzssU0ibdUo-2gKQ)
- [Manipulate DOM elements](https://intranet.alxswe.com/rltoken/ve8UKsZLVw2t27PtWscZfQ)
- [API Introduction](https://intranet.alxswe.com/rltoken/ve8UKsZLVw2t27PtWscZfQ)
- [GET & POST request](https://intranet.alxswe.com/rltoken/Mbe7uoy0iMAfTVs2Tn4Pzg)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.alxswe.com/rltoken/gMwyXisSLu-kZicmGA0-LQ)
- [What went wrong? Troubleshooting JavaScript](https://intranet.alxswe.com/rltoken/4eYyJr72PO-cohImk93M3w)
- [JQuery](https://intranet.alxswe.com/rltoken/HnjBq6jf84S9S-C15Qi0vw)
- [JQuery API](https://intranet.alxswe.com/rltoken/jvibhq-8VEdQHNUWKTCI7w)
- [JQuery Ajax](https://intranet.alxswe.com/rltoken/rBZyrXxuRuISDfPBzO9Y7Q)

## Course to explore:
- [JQuery-Linkedin-Learning]( https://www.linkedin.com/learning/jquery-essential-training-2)

### General

- Explain why jQuery makes front-end programming easier.
- Select HTML elements using both pure JavaScript and jQuery.
- Understand the differences between ID, class, and tag name selectors.
- Modify HTML element styles using JavaScript and jQuery.
- Get and update HTML element content dynamically.
- Manipulate the DOM using JavaScript and jQuery.
- Make both GET and POST requests using jQuery Ajax.
- Listen/bind to DOM events and user events effectively.


### Import JQuery

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

```
## Tasks :

* **0. No jQuery**
  * [0-script.js](./0-script.js): JavaScript script that uses `document.querySelector`
  to update the text color of the HTML tag `HEADER` to red (`#ff0`).

* **1. With jQuery**
  * [1-script.js](./1-script.js): JavaScript script that uses jQuery to update the
  text color of the HTML tag `HEADER` to red (`#ff0`).

* **2. Click and turn red**
  * [2-script.js](./2-script.js): JavaScript script that uses jQuery to update the text color
  of the HTML tag `HEADER` to red (`#ff0`) when the user clicks on the tag `DIV#red_header`.

* **3. Add `.red` class**
  * [3-script.js](./3-script.js): JavaScript script that uses jQuery to add the class
  `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.
* **4. Toggle classes**
  * [4-script.js](./4-script.js): JavaScript script that uses jQuery to toggle the class
  of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag
  `DIV#red_header`.

* **5. List of elements**
  * [5-script.js](./5-script.js): JavaScript script that uses jQuery to add a `LI`
  element to a list when the user clicks on the tag `DIV#add_item`.
  * Adds the element `<li>Item</li>` to `UL.my_list`.

* **6. Change the text**
  * [6-script.js](./6-script.js): JavaScript script that uses jQuery to update the text
  of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag
  `DIV#update_header`.

* **7. Star wars character**
  * [7-script.js](./7-script.js): JavaScript script that uses jQuery to fetch the Star
  Wars API `https://swapi.co/api/people/5/?format=json` and display the name in the HTML
  tag `DIV#character`.

* **8. Star Wars movies**
  * [8-script.js](./8-script.js): JavaScript script that uses jQuery to fetch and list
  all movie titles from the Star Wars API `https://swapi.co/api/films/?format=json`.
  * Titles are listed in the HTML tag `UL#list_movies`.

* **9. Say Hello!**
  * [9-script.js](./9-script.js): JavaScript script that uses jQuery to fetch and display
  how to say "Hello" in French using the API
  `https://fourtonfish.com/hellosalut/?lang=fr`.
  * Displays the translation in the HTML tag `DIV#hello`.
  * Works when imported in the `HEAD` tag.

* **10. No jQuery - document loaded**
  * [100-script.js](./100-script.js): JavaScript script that uses `document.querySelector`
  to update the text color of the HTML tag `HEADER` to red (`#ff0`).
  * Works when imported in the `HEAD` tag.

* **11. List, add, remove**
  * [101-script.js](./101-script.js): JavaScript script that uses jQuery to add, remove,
  and clear `LI` elements from a list based on user click input.
  * Adds a new element when the user clicks `DIV#add_item`.
    * Adds `<li>Item</li>` to the HTML tag `UL.my_list`.
  * Removes the last element when the user clicks `DIV#remove_item`.
  * Clears all elements when the user clicks `DIV#clear_list`.
  * Works when imported in the `HEAD` tag.

* **12. Say hello to everybody!**
  * [102-script.js](./102-script.js): JavaScript script that uses jQuery to fetch and
  display how to say "Hello" in a given language using the API
  `https://www.fourtonfish.com/hellosalut/hello/`.
  * Fetches the translation for the language entered in the HTML tag `INPUT#language_code`.
  * Fetches the translation when the user clicks on the HTML tag `INPUT#btn_translate`.
  * Displays the translation in the HTML tag `DIV#hello`.
  * Works when imported in the `HEAD` tag.

* **13. And press ENTER**
  * [103-script.js](./103-script.js): JavaScript script that uses jQuery to fetch and
  display how to say "Hello" in a given language using the API
  `https://www.fourtonfish.com/hellosalut/hello/`.
  * Identical to [102-script.js](./102-script.js) except that the tranlsation is fetched
  when either the user clicks on the HTML tag `INPUT#btn_translate` or presses `ENTER`
  when hovering over the tag `INPUT#language_code`.

## Author:

* [Josh-techie](https://github.com/Josh-techie)
