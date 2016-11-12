phantom.casperPath = '/node_modules/casperjs';
phantom.injectJS(phantom.casperPath + '/node_modules/bin/bootstrap.js');

var Crawler = require("node-webcrawler");
var url = require('url');
var Spider = require('node-spider');
var casper = require('casper').create();
casper.start('http://casperjs.org/');

casper.then(function() {
    this.echo('First Page: ' + this.getTitle());
});

casper.thenOpen('http://phantomjs.org', function() {
    this.echo('Second Page: ' + this.getTitle());
});

casper.run();








/*var spider = new Spider({
	// How many requests can be run in parallel 
	concurrent: 5,
	// How long to wait after each request 
	delay: 0,
	// A stream to where internal logs are sent, optional 
	logs: process.stderr,
	// Re-visit visited URLs, false by default 
	allowDuplicates: false,
	// If `true` all queued handlers will be try-catch'd, errors go to `error` callback 
	catchErrors: true,
	// Called when there's an error, throw will be used if none is provided 
	error: function(err, url) {
	},
	// Called when there are no more requests 
	done: function() {
	},
	
	//- All options are passed to `request` module, for example: 
	//headers: { 'user-agent': 'node-spider' },
	//encoding: 'utf8'
});
 
var handleRequest = function(doc) {
	// new page crawled 
	//console.log(doc.res); // response object 
	console.log(doc.url); // page url 
	//console.log("success");
	// uses cheerio, check its docs for more info 
	doc.$('a').each(function(i, elem) {
		// do stuff with element 
		var href = elem.attr('href').split('#')[0];
		var url = doc.resolve(href);

		// crawl more 
		spider.queue(url, handleRequest);
	});




};
 
// start crawling 
spider.queue('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552', handleRequest);*/

 






/*
var c = new Crawler({
    maxConnections : 10,
    // This will be called for each crawled page 
    callback : function (error, result, $) {
        // $ is Cheerio by default 
        //a lean implementation of core jQuery designed specifically for the server 
        $('a').each(function(index, a) {
            var toQueueUrl = $(a).attr('href');
            c.queue(toQueueUrl);
        });
    }
});
 
// Queue just one URL, with default callback 
c.queue('http://joshfire.com');
 
// Queue a list of URLs 
//c.queue(['http://jamendo.com/','http://tedxparis.com']);
 
// Queue URLs with custom callbacks & parameters 
c.queue([{
    uri: 'http://parishackers.org/',
    jQuery: false,
 
    // The global callback won't be called 
    callback: function (error, result) {
        console.log('Grabbed', result.body.length, 'bytes');
    }
}]);
 

// Queue using a function 
var googleSearch = function(search) {
  return 'http://www.google.fr/search?q=' + search;
};
c.queue({
  uri: googleSearch('cheese')
});
 
// Queue some HTML code directly without grabbing (mostly for tests) 
c.queue([{
    html: '<p>This is a <strong>test</strong></p>'
}]);*/