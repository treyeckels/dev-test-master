# Cybrary Technical Interview
The purpose of this is to evaluate an interviewee’s technical knowledge and understanding in a day-to-day like scenario.

During this interview, the interviewee is given a group of articles in a JSON format. The interviewee must display all articles in a digestible format on page 1 and display each article in an easily readable format on page 2. The interviewee must also create a liking system for articles so the reader is able to express a positive reaction towards the article. Be sure to follow the requirements listed below.

**Note**
This interview is completely open book. During a work day you'll have access to anything on the internet so why not during the interview? Yes, that includes stackoverflow.

## Requirements
Be sure to tackle all the points specified under *Required*. Anything under *Optional* will **not** count against you.
Each Page can be interpreted as a navigable section of an application.

## Allowed
- Any Framework
- Any language

### Required
- [ ] Page 1 - The Landing Page
  * Display all articles in an easily digestible format on the page
    * The item should include the articles header image
    * The item should include the articles title
    * The item should include a short preview of the content
    * The item should include the date the article was published
  * No static items
    * Each item and its properties should be dynamic based on the provided data
  * Link the item to its article page when clicked on (see below)
    
- [ ] Page 2 - The Article Page
  * Display the article in an easily readable format
    * The page should include the article's header image
    * The page should include the article's title
    * The page should include the author of the article
    * The page should include the date the article was published
    * The page should include the full article
  * No static pages
    * The article and its related items should be dynamic based on the provided data
  * Add a liking system
    * Add a way to like the article (visually)
    * Keep track of the state to display if the user liked it or not
    * Can be stored client side for now
  * Responsiveness
    * Make the page responsive for a device of your choosing
    * Be prepared to explain why you chose this device and how you would make it responsive for other devices

### Optional
- [ ] Make pages fully responsive
- [ ] Create components and/or items from scratch
- [ ] Use of a database
  * Spin up a database of your choosing
  * Input the JSON data into the database
  * Connect to the database
  * Get data from the database
- [ ] List items by most liked
  * Introduce time decay to predict the heat-index-score of an article (Double Hypens === 'Hotness' # Right??)
