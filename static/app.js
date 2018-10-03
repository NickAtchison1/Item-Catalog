const numbers = [];
var prices = document.querySelectorAll('.price');
var sum = 0;


for ( var price of prices ) {
    numbers.push(parseFloat(price.innerText.replace('$', 0))
);

   
   // regular for loop was returning wrong result. Appeared to add 1 per every item in element
   // below code found at https://stackoverflow.com/questions/1230233/how-to-find-the-sum-of-an-array-of-numbers
    sum  = numbers.reduce((a, b) => a + b, 0);

    var avg = (sum / numbers.length).toFixed(2);

    
}

var avgDiv = document.createElement("div");
avgDiv.style.cssText = 'position:absolute;top:300px;right:300px;width:640px;height:200px;color:#0093B9;font-size:20px;line-height:24px;';
var totalNumContent = document.createTextNode("Number of items in this category: " + numbers.length + "  ");
var avgContent = document.createTextNode("The average price in this category is: $" + avg);
avgDiv.appendChild(totalNumContent);
 avgDiv.appendChild(avgContent);
document.body.appendChild(avgDiv);  