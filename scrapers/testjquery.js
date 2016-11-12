var request = require("request");
var cheerio = require("cheerio");

/*urls = [];

request('https://www.reddit.com', function (error, resp, body) {
  if (!error && resp.statusCode == 200) {
    var $ = cheerio.load(body);
    $('a.title','#siteTable').each(function() {
    	var url = this.href;
    	urls.push[url];
    });
    console.log(urls);
  }
});*/

/*request('https://news.ycombinator.com', function (error, response, html) {
  if (!error && response.statusCode == 200) {
    var $ = cheerio.load(html);
    $('span.comhead').each(function(i, element){
      var a = $(this).prev();
      console.log(a.text());
    });
  }
});*/

request('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552', function (error, response, html) {
  if (!error && response.statusCode == 200) {
   
    console.log("enters the request");
    var $ = cheerio.load(html);

    //console.log($('h1').text)
    console.log($('li.deptColumn').html);

    if($('#result').length)
    {
      console.log("exists");
    }
    else
    {
      console.log("dsfdsdf");
    }


    console.log("before the core call");
    //$('input.deptSelectInput').each(function(i, element){
    $('li.deptColumn').find('li.result').each(function(){
     // console.log("before the call to children");
     // var a = $(this).children('li.result');
      var b = $(this).text;
      console.log(b);
      //console.log(a.text() + '\n');
      //console.log("test");
    });
  }
  else if (error)
  {
    console.log(error);
  }
});

 

//console.log("Success");

