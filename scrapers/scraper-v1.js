/**UTILIZES CASPERJS AND PHANTOM JS**/


var casper = require('casper').create();
var fs = require("fs");

var x = require('casper').selectXPath;
var books = []; 
var departments = []; 
var courses = [];


casper.start('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552');
casper.page.injectJs('C:/Users/Aumit/Documents/Dev/importantJS/jquery-3.0.0');

casper.wait(3000, function() {
	//this.echo(this.getTitle());
	console.log("Beginning...");
});


/**Will visit website, and enter the input into the textbox, takes 
	screenshot, and pic is stored in same directory as script.

	Needd to nest loops, for each. */
casper.then(function() {
	//Returns list of departments
	//Stores list of departments into array. 
	var departmentNames = casper.getElementsInfo("#FindCourse > div > div.campusSection > div:nth-child(2) > div.courseBookSelector > ul > li.deptColumn > ul > li");
	//this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[2]/input'));
	departmentNames.forEach(function(department) {
		//Save this to an array
		//console.log(department.text);
		departments.push(department.text);
	});


	this.sendKeys('.deptSelectInput', departments[1]); 
	this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});

	
	
	/**funciton works
	departments.forEach(function(dept) {
		console.log(dept);
	});*/

/**This is not working. Look at casper Docs to see maybe cant use casper object twice here.**
	this.sendKeys('.deptSelectInput', deparmtent[1]); 
	this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});*/
	/*var courses = this.getElementsInfo("#FindCourse > div > div.campusSection > div:nth-child(2) > div.courseBookSelector > ul > li.courseColumn > ul > li");
	courses.forEach(function(course) {
		console.log(course.text);
	});*/

	//var departmentNames = casper.getElementsInfo("#FindCourse > div > div.campusSection > div:nth-child(2) > div.courseBookSelector > ul > li.deptColumn > ul > li");
	/*departments.forEach(function(dept) {
		this.sendKeys('.deptSelectInput', dept); 
		this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});
		var courses = casper.getElementsInfo("#FindCourse > div > div.campusSection > div:nth-child(2) > div.courseBookSelector > ul > li.courseColumn > ul > li");
		this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[3]/input'));
		courseNames.forEach(function(course) {
			console.log(course.text);
		});
	});*/

	/* Primary algorithm for filling and submitting forms.

	department.forEach(function(dept) {
		/**Need to Figure out the logic hee....*
		this.sendKeys('.deptSelectInput', dept); 
		this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});
		var courses = casper.getElementsInfo("#FindCourse > div > div.campusSection > div:nth-child(2) > div.courseBookSelector > ul > li.courseColumn > ul > li");
		this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[3]/input'));
		courseNames.forEach(function(course) {
			this.sendKeys('.courseSelectInput', course.text);
			this.sendKeys('.courseSelectInput', casper.page.event.key.Enter , {keepFocus: true});
			var sections = casper.getElementsInfo("#FindCourse > div > div.campusSection > div.bookRowContainer.errorBoxDisplay > div.courseBookSelector > ul > li.sectionColumn > ul > li");
			this.click(x('//*[@id="FindCourse"]/div/div[1]/div[2]/div[1]/ul/li[4]/input[2]'));
			sections.forEach(function(section) {
				this.sendKeys('.courseSelectInput', section.text);
				this.sendKeys('.sectionSelectInput', casper.page.event.key.Enter , {keepFocus: true});
			});
		});
	});*/
	
/**COMMENT THIS PORTION OUT WHEN TESTING FUNCTIONALITY OF RETRIEIVNG COURSE/DEPT/SECTION INFO****/

	/*console.log("Entering input");
	this.sendKeys('.deptSelectInput', '189');
	this.sendKeys('.deptSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.sendKeys('.courseSelectInput', '102');
	this.sendKeys('.courseSelectInput', casper.page.event.key.Enter , {keepFocus: true});
	this.sendKeys('.sectionSelectInput', '03');
	this.sendKeys('.sectionSelectInput', casper.page.event.key.Enter , {keepFocus: true});*/
});

casper.then(function() {
	casper.capture('test.png');
});

casper.wait(5000, function() {
	/*WORKS HERE
	departments.forEach(function(dept) {
		console.log(dept);
	});*/

	var courseNames = casper.getElementsInfo("#FindCourse > div > div.campusSection > div:nth-child(2) > div.courseBookSelector > ul > li.courseColumn > ul > li");
	courseNames.forEach(function(course) {
		console.log(course.text);
		//courses.push(course.text);
	});

	/*courses.forEach(function(test) {
		console.log(test);
	});*/
});

/* Doesn't work atm
casper.then(function() {
	courses.forEach(function(test) {
		console.log(test);
	});
});

/*casper.thenClick(x('//*[@id="findMaterialButton"]'), function () {
	console.log("Searching for books...");
});*/

/**Results page. Will take a screensht of the results page while storing the content in json format. 
**
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
 	*/
casper.run();


