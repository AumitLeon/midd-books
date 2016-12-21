/**UTILIZES CASPERJS AND PHANTOM JS**/


var casper = require('casper').create();
var fs = require("fs");

var x = require('casper').selectXPath;
var books = []; 


casper.start('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552');
casper.page.injectJs('C:/Users/Aumit/Documents/Dev/importantJS/jquery-3.0.0');

casper.wait(3000, function() {
	//this.echo(this.getTitle());
	console.log("Beginning...");
});


/**Will visit website, and enter the input into the textbox, takes 
	screenshot, and pic is stored in same directory as script.

	Need to figure out how to actually submit a query and collect results.*/
casper.then(function() {

	//Returns list of departments
	/*var departmentNames = casper.getElementsInfo("li.result");
	this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[2]/input'));
	departmentNames.forEach(function(department) {
		//Save this to an array
		console.log(department.text);
	});
*/


	//need to figure out how to list courses....
	/*console.log("Entering test...");
	this.sendKeys('.deptSelectInput', '010');
	this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[3]/input'));
	*/

	//if(casper.exists('input.courseSelectInput.bncbTextInput')){








	/*var nameCount = this.evaluate(function() {
		var numbs = [];
    	$('li.result').each(function () {
    		numbs.push(this.text);
    	});
    	return numbs;
	});
	this.echo(nameCount);

	nameCount.forEach(function(course) {
		console.log(course);
	});

	/*casper.evaluate(function() {
		var names = $('li.result')
	});
	console.log(names.length);*/
	








	/**var lol = [];

	 var executer = casper.evaluate(function() {
	 	$('li.deptColumn').find('li').each(function(){
      //var a = $(this).prev().children().first();
     		var a = this.text;
     		lol.push(a);
     	});
     	return lol;
	 });
	 console.log(executer);

	var nameCount = this.evaluate(function() {
		var haha = [];
    	var names = $('input.deptSelectInput').nextAll('li.result');
    	//$('input.deptSelectInput').nextUntil('li.courseColumn').each(function(el) {
    	//	 haha.push(el.text);
    	//})
    		return names.text
		});
	//this.echo(nameCount);
	console.log(nameCount);	
	 /*executer.forEach(function(el){
	 	console.log(el);
	 });*/

	
/*
	__utils__.findAll('input.courseSelectInput.bncbTextInput').forEach(function(el){
            //console.log(el.querySelector("li.result").textContent.trim());
            console.log("Works!");
    });
*/

/*
	console.log("Just hit enter");
	casper.wait(5000);
	console.log("Done waiting 5 seconds");
	this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[3]/input'));
	casper.capture('test.png');
	casper.wait(1000);
	console.log("Image captured");
*/
	/*var x = casper.evaluate(function(){
   		//return Array.prototype.map.call(document.querySelectorAll('li.deptColumn'), function(li){li.text});
   		return Array.prototype.map.call(document.querySelectorAll('li.deptColumn'), function(li){return li.text});
	});
	console.log(x);*/

	/*x.forEach(function(course) {
			console.log(course.text);
	});	*/
	/*casper.evaluate(function(this) {
		var y = document.getElementsByClassName('deptColumn');
		var aNode = y[0];
		var x = aNode.casper.getElementsInfo("li.result"); 
		x.forEach(function(course) {
			console.log(course.text);
		});	
	});*/

	//console.log(x.length);
	//var i;
	//console.log("in the barracks");
	//var lol = document.querySelector('.deptColumn').text;
	//console.log(lol);
	/*for (i = 0; i < x.length; i++) {
    	console.log(x[i]);
	}*/

/*
	var courseNames = document.querySelectorAll('li.courseColumn ');
	console.log("Just got correct list");
	courseNames.forEach(function(course) {
		console.log(course.text);
	});	
*/




	console.log("Entering input");
	this.sendKeys('.deptSelectInput', '189');
	this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.sendKeys('.courseSelectInput', '102');
	this.sendKeys('.courseSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.sendKeys('.sectionSelectInput', '03');
	this.sendKeys('.sectionSelectInput', casper.page.event.key.Enter , {keepFocus: true});
});
/*.thenEvaluate(function(selector){
	/*console.log("Entering the evaluate phase....")
	__utils__.findAll(selector).forEach(function(el){
		console.log(el);
	});*
	//console.log("In the trenches");
	var lol = document.querySelector('.msgTopHead');
	console.log(lol.text);
});*/


/*
casper.thenEvaluate(function(term) {
    var y = document.querySelectorAll('li.deptColumn');
	var aNode = y[0];
	var x = aNode.casper.getElementsInfo("li.result"); 
	x.forEach(function(course) {
		console.log(course.text);
	});	
}, 'CasperJS');
*/

//var selector = 'li.deptColumn';
/*casper.evaluate(function(){
	/*console.log("Entering the evaluate phase....")
	__utils__.findAll(selector).forEach(function(el){
		console.log(el);
	});*
	var lol = document.querySelector('.deptColumn');
	console.log(lol);
});*/


casper.thenClick(x('//*[@id="findMaterialButton"]'), function () {
	console.log("Searching for books...");
});

casper.wait(10000, function () {
	casper.capture('test.png');
	console.log("Capturing image!");
	done = false;
	var books; 


	listItems = this.evaluate(function () {
        var nodes = document.querySelectorAll('.clr121');
        return [].map.call(nodes, function(node) {
            return node.textContent;
        });
    });

   fs.write('books.txt', JSON.stringify(this.getElementsAttribute('.clr121', 'title')), 'w');

   this.echo(require('utils').dump(this.getElementsAttribute('.clr121', 'title')));
  
	casper.exit();
});
 	
casper.run();


