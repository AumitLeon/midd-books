/**UTILIZES CASPERJS AND PHANTOM JS**/




/*phantom.casperPath = 'C:/Users/Aumit/Documents/Dev/phantomjs-2.1.1-windows/casperjs-1.1.1/bin';
phantom.injectJs(phantom.casperPath + '/bootstrap.js');*/

//var utils = require('utils');

/*var casper = require('casper').create();

casper.start('http://www.google.com');

casper.wait(3000, function() {
	this.echo(this.getTitle());
});

casper.then(function() {
	casper.exit();
});

casper.run();*/

/*var casper = require('casper').create();
casper.start('http://casperjs.org/');

casper.then(function() {
    this.echo('First Page: ' + this.getTitle());
});

casper.thenOpen('http://phantomjs.org', function() {
    this.echo('Second Page: ' + this.getTitle());
});

casper.run();*/

var casper = require('casper').create();

var x = require('casper').selectXPath;
var books = []; 

casper.start('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552');

casper.wait(3000, function() {
	//this.echo(this.getTitle());
	console.log("Beginning...");
});

function getBooks() {
    var books = document.querySelectorAll(".clr121")
    return Array.prototype.map.call(books_, function(e) {
        return e.textContent
    })
}

/**Will visit website, and enter the input into the textbox, takes 
	screenshot, and pic is stored in same directory as script.

	Need to figure out how to actually submit a query and collect results.*/
casper.then(function() {
	console.log("Entering input");
	this.sendKeys('.deptSelectInput', '010');
	this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.sendKeys('.courseSelectInput', '275');
	this.sendKeys('.courseSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.sendKeys('.sectionSelectInput', '03');
	this.sendKeys('.sectionSelectInput', casper.page.event.key.Enter , {keepFocus: true});
});

casper.thenClick(x('//*[@id="findMaterialButton"]'), function () {
	console.log("Searching for books...");
});

casper.wait(5000, function () {
	casper.capture('test.png');
    this.echo(require('utils').dump(this.getElementsAttribute('.clr121', 'title')));
	casper.exit();
});

casper.run();



//*[@id="jobs"]

