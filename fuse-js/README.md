## How To: Fuzzy Search
*I needed to reliably fuzzy search through a large list of items, and found that a popular library, fuse js, did not return reliable results out of the box*

### Using
* [fuse js](http://fusejs.io/)
* [lodash](https://lodash.com/docs/4.17.5)

### Settings
*I wrapped a few default fuse js settings with new values that help me control results.  In this case, **options** holds the default fuse js settings*
```json
{
  "minScoreRequired" : 0.4,
  "minSubstringLength" : 4,
  "whiteList" : "360 bim vue dwg cad git tag",
  "options" : {
    "caseSensitive" : false,
    "includeScore" : true,
    "keys" : [ "question", "fileName" ],
    "shouldSort" : true,
    "threshold" : 1,
    "tokenize" : true
  }
}
```

### Implementation
```javascript
var results = [] // bucket to collect results
let searchArray = this.localSearch.split(' ') // splits a search query into seperate words
searchArray = _.filter(searchArray, (word) => { return word.length >= settings.minSubstringLength || settings.whiteList.includes(word) }) // filter search array down to desired words to search
var itemsToSearch = [] // a list of objects to search.  keys you want to search should be defined in settings.keys
var f = new Fuse(itemsToSearch, settings) // begin search
searchArray.forEach((substring) => { // search each word
  var result = f.search(substring) // run fuse js search algo
  result.forEach((record) => { // for each record returned
    if (record.score < settings.minScoreRequired) { // if it passes
      results.push(record.item) // add to results
    }
  })
})
```

[back](../)
