var city_list = ['Boston', 'Jamaica']

// warning, this does not work correctly but it might do something partially correctly
var map = function() {
    var stories = this.items;
    if (stories) {
      for (var story = 0; story < stories.length; i++) {
        var keys = [];
        for (var sentence = 0; sentence < stories[story].length; j++) {
          words = stories[story][sentence].split(/\W+/);
          for (var k = 0; k < words.length; k++) {
            if (words[k])  {
              if (city_list.includes(words[k]) {
                keys.push(words[k])
              }
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
