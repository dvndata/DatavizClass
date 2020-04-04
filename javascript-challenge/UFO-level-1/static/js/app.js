var sightings = data;

// Use D3 to select the table body
var tbody = d3.select("tbody");

// clear the table 
tbody.text("");

// load all data
sightings.forEach((sightings) => {
  var row = tbody.append("tr");
  Object.entries(sightings).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

// function filter data based on the date entered
function filteredbydate(sighting) {

  // Capture the date entered
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");
  console.log(inputValue);

  // Return the row if the date entered matches 
  return sighting.datetime === inputValue;
}


// Capture button event
var button = d3.select("#filter-btn");
button.on("click", function () {

  // clear the data 
  tbody.text("");

  // call the function to get the filtered rows.
  var selected = data.filter(filteredbydate);

  // Loop through selected rows and load the data
  selected.forEach((selected) => {
    var row = tbody.append("tr");
    Object.entries(selected).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
});