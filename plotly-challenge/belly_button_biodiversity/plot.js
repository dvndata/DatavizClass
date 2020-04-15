// Main function to read data and load dropdown
function main() {

  // Get the data 
  d3.json("data/samples.json").then((data)=> {
  console.log(data)

  // select dropdown menu 
  var dropdown = d3.select("#SelectIDNo");

  // Populate dropdwown menu with ids
  data.names.forEach(function(ids) {
      dropdown.append("option").text(ids).property("value");
  });

  // Load data and charts to the page
  LoadChart(data.names[0]);
  LoadDetails(data.names[0]);
});
}

// Retrieve data and prepare charts

function LoadChart(id) {

  // read data from json
  d3.json("data/samples.json").then((data)=> {
      console.log(data)

      var wfreq = data.metadata.map(d => d.wfreq)

       // get data for the selected id 
      var samples = data.samples.filter(s => s.id.toString() === id)[0];
      
      //get test subjects ID and the ID's index
      sample_id = samples["id"];
      sample_index = data.names.indexOf(sample_id);

      // Get the top 10 for subject
      var samplevalues = samples.sample_values.slice(0, 10).reverse();

      // get top 10 otu ids for the plot OTU and reverse it. 
      var OTU_top = (samples.otu_ids.slice(0, 10)).reverse();
      
      // get the otu id's to the desired form for the plot
      var OTU_id = OTU_top.map(d => "OTU " + d)

      // get the top 10 labels for the plot
      var labels = samples.otu_labels.slice(0, 10);

      // create trace variable for the plot
      var trace = {
          x: samplevalues,
          y: OTU_id,
          text: labels,
          marker: {
            color: "royalblue"},
          type:"bar",
          orientation: "h",
      };

      // create data variable
      var data = [trace];

      // create layout variable to set plots layout
      var layout = {
          yaxis:{
          tickmode:"linear",
          },
          margin: {
              left: 10,
              right: 20,
              top: 20,
              bottom: 30
          }
      };

      // create the bar plot
      Plotly.newPlot("barchart", data, layout);

      // The bubble chart
      var traceb = {
          x: samples.otu_ids,
          y: samples.sample_values,
          mode: "markers",
          marker: {
              size: samples.sample_values,
              color: samples.otu_ids
          },
          text: samples.otu_labels
      };

      // layout for the bubble chart
      var layoutb = {
          height: 800,
          width: 1200
      };

      // data for plotting
      var datab = [traceb];

      // create the bubble plot
      Plotly.newPlot("bubblechart", datab, layoutb); 

      // create guage chart for wash frequency
      var data_g = [
        {
        domain: { x: [0, 1], y: [0, 1] },
        value: parseFloat(wfreq[sample_index]),
        title: { text: `Belly Button Washing Frequency - Scrubs per Week`, 'font': {'size': 16} },
        type: "indicator",
        
        mode: "gauge+number",
        gauge: { axis: { range: [null, 9] },
                 steps: [
                  { range: [0, 2], color: "cyan" },
                  { range: [2, 4], color: "royalblue" },
                  { range: [4, 6], color: "lightblue" },
                  { range: [6, 8], color: "RebeccaPurple" },
                  { range: [8, 9], color: "darkblue" },
                ],
                bar:{color:"lightred"}
              }
            
        }
      ];
      var layout_g = { 
          width: 600, 
          height: 500, 
          margin: { t: 20, b: 40, l:50, r:100 } 
        };
      Plotly.newPlot("gaugechart", data_g, layout_g);
    });
}  
// create the function to get data for table

function LoadDetails(id) {
  
  // read the json file to get data
  d3.json("data/samples.json").then((data)=> {
      
      // get the data info for table
      var metadata = data.metadata;

      console.log(metadata)

      // filter data info by id
      var result = metadata.filter(meta => meta.id.toString() === id)[0];

      console.log(result);

      // select the table
      var demographicInfo = d3.select("#sample-metadata");
      
      // make sure to empty the table before loading new info
      demographicInfo.html("");

      // use demographic data related to the id and append the info to the table
      Object.entries(result).forEach((key) => {   
              demographicInfo.append("h5").text(key[0] + ": " + key[1] + "\n");    
      });
  });
}

// create the function for the change event
function Changed(id) {
  console.log(id);
  LoadChart(id);
  LoadDetails(id);
}

main();