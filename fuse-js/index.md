## How To: Fuzzy Search
*I needed to reliably fuzzy search through a large list of items, and found that a popular library, fuse js, did not return reliable results out of the box*

### Using
* [fuse js](http://fusejs.io/)
* [lodash](https://lodash.com/docs/4.17.5)

### Settings
* **options**: *are standard fuse js properties*
* **minWordLength**: *the minimum word length used to search*
* **whiteList**: *a string of whitelisted words that are below minWordLength but still desired for search*
* **minScoreRequired**: *similar to options.threshold setting*
```json
{
  "minScoreRequired" : 0.4,
  "minWordLength" : 4,
  "whiteList" : "360 bim vue dwg cad git tag",
  "options" : {
    "caseSensitive" : false,
    "includeScore" : true,
    "keys" : [ "name", "tags" ],
    "shouldSort" : true,
    "threshold" : 1,
    "tokenize" : true
  }
}
```

### Implementation
#### Setup
```javascript
// import fuse, lodash, and create bucket for results
var _ = require('lodash');
var Fuse = require('fuse.js');
var results = [];
var search = 'some search query';

// filter search down to words specified by settings, return array of words to search with
var searchArray = search.split(' ');
var wordsToSearchWith = _.filter(wordsToSearchWith, (word) => { return word.length >= settings.minWordLength || settings.whiteList.includes(word) }); 
```
#### Search
```javascript
// define items to search as array of objects
var itemsToSearch = [{name: 'some name', tags: 'new'}, {name: 'other name', tags: 'old'}];

// create new fuse js constructor
var f = new Fuse(itemsToSearch, settings);

// search items with each search word
wordsToSearchWith.forEach((word) => {
  var result = f.search(word);
  result.forEach((record) => {
    if (record.score < settings.minScoreRequired) {
      results.push(record.item);
    }
  });
});

// log search results
uniqueResults = _.uniq(results)
console.log(uniqueResults);
```

[back](../README.md)
