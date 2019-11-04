var map = function() {
    var items = this.items;
    if (items) {
      for (var i = 0; i < items.length; i++) {
        for (var j = 0; j < items[i].length; j++) {
          words = items[i][j].split(/\W+/);
          for (var k = 0; k < words.length; k++) {
            if (words[k])  {
              emit(words[k], 1);
            }
          }
        }
      }
    }
};

var reduce = function(key, values ) {
    var count = 0;
    values.forEach(function(v) {
        count += v;
    });
    return count;
}

// full thing
// db.support_emails.mapReduce(map, reduce, { out: "word_count" })

// subset
db.globe_stories.mapReduce(map, reduce, {limit: 1000, out: "word_count" })
db.word_count.find().sort({ value: -1 }).limit(10)
