// The map function reads the text and creates a bunch of intermediate key-value files.
// In this case, the key is the word and the value is '1'
var map = function() {
  var story = this.story;

  if (story) {
    words = story.split(/\W+/);
    for (var i = 0; i < words.length; i++) {
      if (words[i]) {
        emit(words[i], 1);
      }
    }
  }
};

// The reduce function takes every key-value pair with a given key and
// adds up their values (in this case, it's a count. So each instance of a word
// has value '1' -- so the result will be a word count)
var reduce = function(key, values ) {

  var count = 0;

  values.forEach(function(v) {
    count += v;
  })
  return count;
}

// We want to do a seperate word count for each neighborhood
db.getCollectionNames().forEach(function(col) {
  try { // run our map function, our reduce function, and write the results to a unique word count output table
    db[col].mapReduce(map, reduce, { out: "wc_" + col})
  }
  catch(err) {
    print(err)
  }
})
