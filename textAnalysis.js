
var map = function() {
  var story = this.story;

  if (story) {
    words = story.split(" ");///\W+/);
    for (var i = 0; i < words.length; i++) {
      if (words[i]) {
        emit(words[i], 1);
      }
    }
  }
};

var reduce = function(key, values ) {

  var count = 0;

  values.forEach(function(v) {
    count += v
  })
  return count;
}

// full thing
db.globe_stories13.mapReduce(map, reduce, { out: "word_count3" })

// subset
//db.globe_stories12.mapReduce(map, reduce, {limit: 1000, out: "word_count" })
db.word_count3.find()//.sort({ value: -1 }).limit(100)

db.getCollectionNames().forEach(function(col) {
  db.col.findOne()
  db.col.mapReduce(map, reduce, { out: "wc_" + String.valueOf(col)})
})

db.getCollectionNames().forEach(function(col) {
  print(col)
})

db.getCollectionNames().forEach(function(col) {
  try {
    db[col].mapReduce(map, reduce, { out: "wc_" + col})
  }
  catch(err) {
    print(err)
  }
})
